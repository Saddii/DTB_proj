#!/usr/bin/env python3

def create_list_of_players(con):
    """
    funkcja tworząca tabelę tournaments
    """
    cs = con.cursor()
    table = "CREATE OR REPLACE TABLE list_of_players(customer_id SMALLINT UNSIGNED NOT NULL, tournament_id SMALLINT UNSIGNED NOT NULL, place TINYINT DEFAULT NULL, PRIMARY KEY (customer_id, tournament_id))"
  
    cs.execute(table)
    cs.fetchall()