SELECT distinct(staff_id) from payment 
SELECT distinct YEAR(payment_date) as "Year", MONTH(payment_date) as "Month" from payment ORDER BY YEAR DESC,MONTH DESC
SELECT staff_id,sum(amount) FROM payment WHERE staff_id=1 and payment_date LIKE "2022-04%" LIMIT 10;
select * from tournaments limit 10 
SELECT staff.first_name,staff.last_name,sum(amount) as earn from payment inner join staff on payment.staff_id=staff.staff_id WHERE payment_date LIKE '2022-04%' GROUP BY staff.staff_id ORDER BY earn DESCSELECT staff.staff_id,staff.first_name,staff.last_name,sum(amount) as earn from payment inner join staff on payment.staff_id=staff.staff_id WHERE payment_date LIKE '2022-04%' GROUP BY staff.staff_id ORDER BY earn DESC 
SELECT distinct game_id from tournaments
SELECT * from tournaments WHERE game_id=37
SELECT * from tournaments
SELECT * from tournaments WHERE game_id=1
SELECT list_of_players.customer_id,COUNT(list_of_players.customer_id) from list_of_players WHERE place=1 GROUP BY list_of_players.customer_id

SELECT games.title,first_name,last_name,COUNT(list_of_players.customer_id) 
from list_of_players 
inner join tournaments on list_of_players.tournament_id=tournaments.tournament_id 
inner join games on tournaments.game_id=games.game_id
inner join customers on list_of_players.customer_id=customers.customer_id 
WHERE place=1 and games.game_id=1 GROUP BY list_of_players.customer_id

SELECT games.title as Game_title,list_of_players.customer_id,COUNT(list_of_players.customer_id) as Num_of_wins from list_of_players inner join games WHERE place=1 and game_id=20 GROUP BY list_of_players.customer_id ORDER BY COUNT(list_of_players.customer_id) DESC LIMIT 10 

select * from games LIMIT 10 

SELECT * from inventory LIMIT 30
SELECT rental_id_or_last_rental_id from payment WHERE rental_id_or_last_rental_id LIKE "l%" limit 1000

SELECT substring(rental_id_or_last_rental_id,16) from payment WHERE rental_id_or_last_rental_id LIKE "l%" limit 1000

SELECT games.title,amount from payment
inner join inventory on substring(payment.rental_id_or_last_rental_id,16)=inventory.inventory_id
inner join games on inventory.game_id=games.game_id
WHERE payment.rental_id_or_last_rental_id LIKE "l%" 

select * from payment WHERE amount < 0


SELECT games.title as "Game title",sum(payment.amount) as "Sum of rental" from payment
inner join inventory on payment.rental_id_or_last_rental_id=inventory.inventory_id
inner join games on inventory.game_id=games.game_id
WHERE rental_id_or_last_rental_id LIKE "___" 
GROUP BY games.game_id
ORDER by sum(payment.amount) DESC

SELECT games.title as "Game title",sum(payment.amount) as "Sum of sold" from payment
inner join inventory on substring(payment.rental_id_or_last_rental_id,16)=inventory.inventory_id
inner join games on inventory.game_id=games.game_id
WHERE rental_id_or_last_rental_id LIKE "l%" 
GROUP BY games.game_id
ORDER by sum(payment.amount) DESC

select rental_date,return_date from rental LIMIT 10 
SELECT rental_id,DATEDIFF(return_date,rental_date) as "Liczba dni w wypożyczeniu" FROM rental 

SELECT games.title,TIMESTAMPDIFF(MINUTE,tournaments.start_date,tournaments.end_date) as 'Czas_trwania_turnieju[min]' from tournaments 
inner join games on tournaments.game_id=games.game_id 
GROUP BY games.title
ORDER BY TIMESTAMPDIFF(MINUTE,tournaments.start_date,tournaments.end_date) DESC

SELECT games.title,TIMESTAMPDIFF(MINUTE,tournaments.start_date,tournaments.end_date) as 'Czas_trwania_turnieju[min]' from tournaments 
inner join games on tournaments.game_id=games.game_id
ORDER BY TIMESTAMPDIFF(MINUTE,tournaments.start_date,tournaments.end_date) DESC

SELECT games.game_id,games.title,TIMESTAMPDIFF(MINUTE,tournaments.start_date,tournaments.end_date) as 'Czas_trwania_turnieju[min]' from tournaments 
inner join games on tournaments.game_id=games.game_id GROUP BY games.title ORDER BY TIMESTAMPDIFF(MINUTE,tournaments.start_date,tournaments.end_date) DESC

SELECT game_id, COUNT(*) AS wystapienia
FROM tournaments
GROUP BY game_id;

