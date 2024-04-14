#!/usr/bin/env python3

def create_inventory(con):
    """
    funkcja tworząca tabelę inventory
    """
    cs = con.cursor()
    table = "CREATE OR REPLACE TABLE inventory(inventory_id SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,game_id SMALLINT UNSIGNED NOT NULL) COMMENT 'magazynek'"
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

    create_inventory(con)
    
    ##########
    #test czy działa wstawiając wartość i odczytując
    cs = con.cursor()
    insert = "INSERT INTO inventory (game_id) VALUES (%s)"
    

    val = [2]
    cs.execute(insert,val)
    con.commit()
    cs.fetchall()

    cs.execute("SELECT * FROM inventory")

    for i in cs:
        print(i)

    con.close()
