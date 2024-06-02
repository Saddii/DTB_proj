-- SELECT games.game_id,games.title,
-- AVG(TIMESTAMPDIFF(MINUTE,tournaments.start_date,tournaments.end_date)) as avg_tournament_time from tournaments 
-- inner join games on tournaments.game_id=games.game_id 
-- GROUP BY games.title 
-- ORDER BY avg_tournament_time
--  DESC LIMIT 10;


-- SELECT *,count(*) FROM payment GROUP BY rental_id_or_last_rental_id;
;
--GAMES BOUGHT
SELECT games.title from games where title not in(
SELECT games.title as 'Game title'
 from payment 
inner join inventory on 
substring(payment.rental_id_or_last_rental_id,16)=inventory.inventory_id 
inner join games on inventory.game_id=games.game_id 
WHERE rental_id_or_last_rental_id LIKE 'l%' GROUP BY games.game_id 
 )
 

--GAMES RENTED
SELECT games.title as 'Game title',
COUNT(payment.amount) as 'Num of rental' 
from payment inner join inventory on 
payment.rental_id_or_last_rental_id=inventory.inventory_id 
inner join games on inventory.game_id=games.game_id 
WHERE rental_id_or_last_rental_id LIKE '___' GROUP BY games.game_id 
ORDER by COUNT(payment.amount) DESC;


SELECT * FROM (
SELECT * FROM (SELECT games.title as title,
COUNT(payment.amount) as num_of_sells from payment 
inner join inventory on 
substring(payment.rental_id_or_last_rental_id,16)=inventory.inventory_id 
inner join games on inventory.game_id=games.game_id 
WHERE rental_id_or_last_rental_id LIKE 'l%' GROUP BY games.game_id 
) as games_bought
FULL OUTER JOIN (SELECT games.title as title,
COUNT(payment.amount) as num_of_rental 
from payment inner join inventory on 
payment.rental_id_or_last_rental_id=inventory.inventory_id 
inner join games on inventory.game_id=games.game_id 
WHERE rental_id_or_last_rental_id LIKE '___' GROUP BY games.game_id) as games_rented
ON games_rented.title=games_bought.title
ORDER BY num_of_sells DESC,num_of_rental DESC
) as sub;



SELECT *,case WHEN title in (
    select games.title as title
    from payment 
    inner join games on substring(rental_id_or_last_rental_id,16) = games.game_id
    where rental_id_or_last_rental_id LIKE 'l%') then "YES" ELSE "NO" END
 FROM (
SELECT games.title as title,
COUNT(*) as num 
from payment 
inner join inventory 
on payment.rental_id_or_last_rental_id=inventory.inventory_id 
inner join games on inventory.game_id=games.game_id 
WHERE rental_id_or_last_rental_id LIKE '___' GROUP BY games.game_id 
ORDER by num DESC
) as sub1;


;

SELECT title,num_of_sells,num_of_rental FROM(
SELECT COALESCE(games_bought.title, games_rented.title) as title,
       COALESCE(games_bought.num_of_sells, 0) as num_of_sells,
       COALESCE(games_rented.num_of_rental, 0) as num_of_rental
FROM 
    (SELECT games.title as title,
            COUNT(payment.amount) as num_of_sells 
     FROM payment 
     INNER JOIN inventory ON substring(payment.rental_id_or_last_rental_id,16) = inventory.inventory_id 
     INNER JOIN games ON inventory.game_id = games.game_id 
     WHERE rental_id_or_last_rental_id LIKE 'l%' 
     GROUP BY games.game_id) as games_bought
LEFT JOIN 
    (SELECT games.title as title,
            COUNT(payment.amount) as num_of_rental 
     FROM payment 
     INNER JOIN inventory ON payment.rental_id_or_last_rental_id = inventory.inventory_id 
     INNER JOIN games ON inventory.game_id = games.game_id 
     WHERE rental_id_or_last_rental_id LIKE '___' 
     GROUP BY games.game_id) as games_rented
ON games_bought.title = games_rented.title

UNION

SELECT COALESCE(games_bought.title, games_rented.title) as title,
       COALESCE(games_bought.num_of_sells, 0) as num_of_sells,
       COALESCE(games_rented.num_of_rental, 0) as num_of_rental
FROM 
    (SELECT games.title as title,
            COUNT(payment.amount) as num_of_sells 
     FROM payment 
     INNER JOIN inventory ON substring(payment.rental_id_or_last_rental_id,16) = inventory.inventory_id 
     INNER JOIN games ON inventory.game_id = games.game_id 
     WHERE rental_id_or_last_rental_id LIKE 'l%' 
     GROUP BY games.game_id) as games_bought
RIGHT JOIN 
    (SELECT games.title as title,
            COUNT(payment.amount) as num_of_rental 
     FROM payment 
     INNER JOIN inventory ON payment.rental_id_or_last_rental_id = inventory.inventory_id 
     INNER JOIN games ON inventory.game_id = games.game_id 
     WHERE rental_id_or_last_rental_id LIKE '___' 
     GROUP BY games.game_id) as games_rented
ON games_bought.title = games_rented.title
ORDER BY COALESCE(num_of_sells, 0) DESC, COALESCE(num_of_rental, 0) DESC
) as sub
;








--sprzedane
SELECT num_of_rental,sum(BOUGHT) FROM (
SELECT wyp.inventory_id,num_of_rental,CASE WHEN sold.inventory_id is null then 0 ELSE 1 END as BOUGHT
FROM (
    SELECT inventory_id
    FROM payment 
    INNER JOIN rental ON substring(payment.rental_id_or_last_rental_id, 16) = rental.rental_id
    WHERE payment.rental_id_or_last_rental_id LIKE 'l%' 
    GROUP BY inventory_id
) AS sold
RIGHT JOIN (
    SELECT inventory_id, COUNT(*) AS num_of_rental
    FROM payment
    RIGHT JOIN rental ON payment.rental_id_or_last_rental_id = rental.rental_id
    GROUP BY inventory_id
) AS wyp
ON sold.inventory_id = wyp.inventory_id
) as sub
GROUP BY num_of_rental


select * from rental;



SELECT num_of_rental,count(*) FROM 
(SELECT inventory_id,0 as num_of_rental,1 as BOUGHT
FROM inventory
WHERE inventory_id NOT IN (
    SELECT DISTINCT (inventory_id)
    FROM rental)
UNION 
SELECT wyp.inventory_id,num_of_rental,CASE WHEN sold.inventory_id is null then 0 ELSE 1 END as BOUGHT
FROM (
    SELECT inventory_id
    FROM payment 
    INNER JOIN rental ON substring(payment.rental_id_or_last_rental_id, 16) = rental.rental_id
    WHERE payment.rental_id_or_last_rental_id LIKE 'l%' 
    GROUP BY inventory_id
) AS sold
RIGHT JOIN (
    SELECT inventory_id, COUNT(*) AS num_of_rental
    FROM payment
    RIGHT JOIN rental ON payment.rental_id_or_last_rental_id = rental.rental_id
    GROUP BY inventory_id
) AS wyp
ON sold.inventory_id = wyp.inventory_id) as sub1
where BOUGHT =1
GROUP BY num_of_rental

;


WITH zero_rentals AS (
    SELECT inventory_id
    FROM inventory
    WHERE inventory_id NOT IN (
        SELECT DISTINCT (inventory_id)
        FROM rental
    ))