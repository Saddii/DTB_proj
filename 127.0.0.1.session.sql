SELECT game_id,title,first_name,last_name,MAX(won_num) best_player FROM (
SELECT games.game_id,games.title,first_name,last_name,
COUNT(list_of_players.customer_id) as won_num from list_of_players 
inner join tournaments on list_of_players.tournament_id=tournaments.tournament_id 
inner join games on tournaments.game_id=games.game_id 
inner join customers on list_of_players.customer_id=customers.customer_id 
WHERE place=1 GROUP BY list_of_players.customer_id ORDER BY COUNT(*) DESC) as sub1 
GROUP BY game_id



