#!/usr/bin/env python3

import mysql.connector
from creators.create_customers import create_customers
from creators.create_inventory import create_inventory
from creators.create_tournaments import create_tournaments
from creators.create_games import create_games
from creators.create_staff import create_staff
from creators.create_rental import create_rental
from creators.create_payment import create_payment
from creators.create_players import create_players
from creators.create_list_of_players import create_list_of_players
from creators.create_tournament_player import create_tournament_player
from creators.alter_table import alter_table
from fill import fill_customers, fill_staff, fill_inventory, fill_games, fill_tournaments, fill_list_of_players, fill_rental, fill_payment

def bob_the_builder():
    """
    creates and fills all tables.
    """

    try:
        con = mysql.connector.connect(
                host = "127.0.0.1",
                user = "root",
                password = "password",
                database = "clients_base",
                )
    except:
        con = mysql.connector.connect(
                host = "127.0.0.1",
                user = "root",
                password = "password",
                )
        cs = con.cursor()
        cs.execute("CREATE DATABASE clients_base")
        

    if not con:
        raise Exception("connection error")
    
    cs = con.cursor()
    cs.execute("SET FOREIGN_KEY_CHECKS=0")
    cs.fetchall()
    
    cs.execute("DROP TABLE IF EXISTS customers,inventory,tournaments,games,staff,rental,payment,players,tournament_player")

    create_customers(con)
    create_inventory(con)
    create_tournaments(con)
    create_games(con)
    create_staff(con)
    create_rental(con)
    create_payment(con)
    create_list_of_players(con)
    #create_players(con)
    #create_tournament_player(con)

    alter_table(con)

    fill_customers(con,300)
    fill_staff(con, 15)
    games = fill_games(con, 40)
    inventory = fill_inventory(con, games[0])
    tournaments = fill_tournaments(con, games[1])
    fill_list_of_players(con, tournaments)
    rental = fill_rental(con, inventory)
    fill_payment(con, rental)
    cs.execute("SET FOREIGN_KEY_CHECKS=1")
    con.close()

if __name__ == "__main__":
    bob_the_builder()
