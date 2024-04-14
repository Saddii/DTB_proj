#!/usr/bin/env python3

def create_tournaments(con):
    """
    funkcja tworząca tabelę tournaments
    """
    cs = con.cursor()
    table = "CREATE OR REPLACE TABLE tournaments(tournament_id SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,game_id SMALLINT UNSIGNED NOT NULL,start_date TIMESTAMP NOT NULL,end_date TIMESTAMP NOT NULL,prize FLOAT UNSIGNED DEFAULT NULL)"
    cs.execute(table)
    cs.fetchall()
    
    alter1 = "ALTER TABLE tournaments ADD CONSTRAINT start_date_in_bounds CHECK (start_date <= '2022-12-31' AND start_date >= '2016-01-01')"
    alter2 = "ALTER TABLE tournaments ADD CONSTRAINT end_date_in_bounds CHECK (DATE(end_date) >= DATE(start_date))"
    cs.execute(alter1)
    cs.execute(alter2)
    

if __name__ == "__main__":
    import time
    import datetime
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
    create_tournaments(con)
    ##########
    #test czy działa wstawiając wartość i odczytując
    cs = con.cursor()
    insert = "INSERT INTO tournaments (game_id, start_date, end_date, prize) VALUES (%s, %s, %s, %s)"

    
    date1 = datetime.datetime(2021,6,14)
    date1_formatted = date1.strftime('%Y-%m-%d')
    date2 = datetime.datetime(2021,6,23)
    date2_formatted = date2.strftime('%Y-%m-%d')

    val = (4,date1_formatted,date2_formatted, 350.50)
    cs.execute(insert,val)
    con.commit()
    cs.fetchall()

    cs.execute("SELECT * FROM tournaments")
    
    for i in cs:
        print(i)

    con.close()
