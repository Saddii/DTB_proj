#!/usr/bin/env python3

def create_rental(con):
    """
    funkcja tworząca tabelę rental
    """
    cs = con.cursor()
    table = "CREATE OR REPLACE TABLE rental(rental_id SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,inventory_id SMALLINT UNSIGNED NOT NULL,customer_id SMALLINT UNSIGNED NOT NULL,staff_id SMALLINT UNSIGNED NOT NULL,rental_date DATE NOT NULL,return_date DATE DEFAULT NULL)"
    cs.execute(table)
    cs.fetchall()
    
    alter1 = "ALTER TABLE rental ADD CONSTRAINT rental_date_in_bounds CHECK (rental_date <= '2022-12-29' AND rental_date >= '2014-01-01')"
    alter2 = "ALTER TABLE rental ADD CONSTRAINT return_date_in_bounds CHECK (return_date >= rental_date)"

    #cs.execute(alter1)
    cs.execute(alter2)
    
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
    create_rental(con)
    ##########
    #test czy działa wstawiając wartość i odczytując
    cs = con.cursor()
    insert = "INSERT INTO rental (inventory_id, customer_id, staff_id, rental_date,return_date) VALUES (%s, %s, %s, %s, %s)"
    
    
    val = (40,3,2,"2018-06-14","2018-07-09")
    cs.execute(insert,val)
    con.commit()
    cs.fetchall()

    cs.execute("SELECT * FROM rental")

    for i in cs:
        print(i)

    con.close()






