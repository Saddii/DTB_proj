#!/usr/bin/env python3

def drop_all(con):
    cs = con.cursor()
    cs.execute("SET FOREIGN_KEY_CHECKS=0")
    cs.fetchall()

    cs.execute("DROP TABLE IF EXISTS customers, inventory, tournaments, games, staff, rental, payment, players, tournament_player")

    cs.fetchall()
    cs.execute("SET FOREIGN_KEY_CHECKS=1")

if __name__ == "__main__":
    import mysql.connector
    con = mysql.connector.connect(
            host = "giniewicz.it",
            user = "team04"
            password = "te@m0a",
            database = "team04",
            )
    if not con:
        raise Exception("connnection error")
    drop_all(con)
