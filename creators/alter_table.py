#!/usr/bin/env python3

def alter_table(con):
    """
    funkcja dodająca klucz obcy do tabeli tournaments
    musi być osobno bo coś nie mogę go dodać zanim powstaną inne
    tabele
    """

    cs = con.cursor()
    alter1 = "ALTER TABLE tournaments ADD CONSTRAINT FK_games_TO_tournaments FOREIGN KEY (game_id) REFERENCES games(game_id)"

    alter2 = "ALTER TABLE rental ADD CONSTRAINT FK_inventory_TO_torental FOREIGN KEY (inventory_id) REFERENCES inventory (inventory_id)"
    
    alter3 = "ALTER TABLE inventory ADD CONSTRAINT FK_games_TO_inventory FOREIGN KEY (game_id) REFERENCES games (game_id)"

    alter4 = "ALTER TABLE rental ADD CONSTRAINT FK_customer_TO_rental FOREIGN KEY (customer_id) REFERENCES customers (customer_id)"

    alter5 = "ALTER TABLE rental ADD CONSTRAINT FK_staff_TO_rental FOREIGN KEY (staff_id) REFERENCES staff (staff_id)"

    alter6 = "ALTER TABLE payment ADD CONSTRAINT FK_customers_TO_payment FOREIGN KEY (customer_id) REFERENCES customers (customer_id)"

    alter7 = "ALTER TABLE payment ADD CONSTRAINT FK_staff_TO_payment FOREIGN KEY (staff_id) REFERENCES staff (staff_id)"

    alter8 = "ALTER TABLE players ADD CONSTRAINT FK_customers_TO_players FOREIGN KEY (customer_id) REFERENCES customers (customer_id) ON DELETE CASCADE"

    alter9 = "ALTER TABLE payment ADD CONSTRAINT FK_rental_TO_payment FOREIGN KEY (rental_id) REFERENCES rental (rental_id)"

    alter10 = "ALTER TABLE tournament_player ADD CONSTRAINT FK_tournaments_TO_tournaments FOREIGN KEY (tournament_id) REFERENCES tournaments (tournament_id),ADD CONSTRAINT KF_players_TO_players FOREIGN KEY (player_id) REFERENCES players (customer_id)"

    alter11 =  "ALTER TABLE list_of_players ADD CONSTRAINT FK_customers_TO_list_of_players FOREIGN KEY (customer_id) REFERENCES customers (customer_id)"

    alter12 = "ALTER TABLE list_of_players ADD CONSTRAINT FK_tournaments_TO_list_of_players FOREIGN KEY (tournament_id) REFERENCES tournaments (tournament_id)"

    cs.execute(alter1)
    cs.execute(alter2)
    cs.execute(alter3)
    cs.execute(alter4)
    cs.execute(alter5)
    cs.execute(alter6)
    cs.execute(alter7)
    #cs.execute(alter8)
    #cs.execute(alter9)
    #cs.execute(alter10)
    cs.execute(alter12)
    cs.execute(alter11)
