#!/usr/bin/env python3

def create_players(con):
    """
    tworzy tabelę z info o graczach turniejów
    każdy gracz jest też klientem
    """
    cs = con.cursor()
    table = "CREATE OR REPLACE TABLE players(customer_id SMALLINT UNSIGNED PRIMARY KEY,winner BOOL DEFAULT false)"
    cs.execute(table)
    cs.fetchall()


if __name__ == "__main__":
    import mysql.connector
    con = mysql.connector.connect(
            host = "giniewicz.it",
            user = "team04",
            password = "te@m0a",
            database = "team04",
            )
    if con:
        print("connected")
    else:
        print("connection error")
    create_players(con)
    ##########
    #test czy działa wstawiając wartość i odczytując
    cs = con.cursor()
    insert = "INSERT INTO players (customer_id,winner) VALUES (%s, %s)"
    

    val = (81,True)
    cs.execute(insert,val)
    con.commit()
    cs.fetchall()

    cs.execute("SELECT * FROM players")

    for i in cs:
        print(i)

    con.close()






