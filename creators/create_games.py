#!/usr/bin/env python3

def create_games(con):
    """
    funkcja tworząca tabelę games
    """
    cs = con.cursor()
    table = "CREATE OR REPLACE TABLE games(game_id SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,title VARCHAR(400) NOT NULL,year_published SMALLINT UNSIGNED NOT NULL,min_players TINYINT UNSIGNED NOT NULL,max_players TINYINT UNSIGNED NOT NULL,play_time SMALLINT UNSIGNED NOT NULL, min_age SMALLINT UNSIGNED NOT NULL,users_rated FLOAT NOT NULL COMMENT 'skala 0-5',difficulty SMALLINT UNSIGNED NOT NULL ,mechanics VARCHAR(250) DEFAULT NULL,type VARCHAR(60) DEFAULT NULL)"
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
    create_games(con)
    ##########
    #test czy działa wstawiając wartość i odczytując
    cs = con.cursor()
    insert = "INSERT INTO games (title, year_published, min_players, max_players, play_time, min_age, users_rated, difficulty) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"


    

    val = ("gobliny",1999,2,6,6,12,3.5,4)
    cs.execute(insert,val)
    con.commit()
    cs.fetchall()

    cs.execute("SELECT * FROM games")

    for i in cs:
        print(i)

    con.close()






