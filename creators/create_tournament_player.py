#!/usr/bin/env python3

def create_tournament_player(con):
    """
    funkcja tworząca tabelę tournament_player
    tabela służy do organizowania info o tym
    jaki zawodni brał udział w jakim turnieju
    """
    cs = con.cursor()
    table = "CREATE OR REPLACE TABLE tournament_player(tournament_id SMALLINT UNSIGNED,player_id SMALLINT UNSIGNED)"
    cs.execute(table)
    cs.fetchall()


if __name__ == "__main__":
    import mysql.connector
    con = mysql.connector.connect(
            host = "127.0.0.1",
            user = "root",
            password = "password",
            database = "clients_base",
            port= 3307
            )
    if con:
        print("connected")
    else:
        print("connection error")
    create_tournament_player(con)
    ##########
    #test czy działa wstawiając wartość i odczytując
    cs = con.cursor()
    insert = "INSERT INTO tournament_player (tournament_id, player_id) VALUES (%s, %s)"
    
    val = (1,3)
    cs.execute(insert,val)
    con.commit()
    cs.fetchall()

    cs.execute("SELECT * FROM tournament_player")

    for i in cs:
        print(i)

    con.close()






