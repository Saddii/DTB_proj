#!/usr/bin/env python3

def create_staff(con):
    """
    funkcja tworząca tabelę staff
    """
    cs = con.cursor()
    table = "CREATE OR REPLACE TABLE staff(staff_id SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,first_name VARCHAR(40) NOT NULL,last_name VARCHAR(45) NOT NULL,email VARCHAR(50) NOT NULL,address VARCHAR(50) NOT NULL,city VARCHAR(50) NOT NULL,salary FLOAT UNSIGNED NOT NULL) COMMENT 'lista pracowników'"

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
    create_staff(con)
    ##########
    #test czy działa wstawiając wartość i odczytując
    cs = con.cursor()
    insert = "INSERT INTO staff (first_name, last_name, salary) VALUES (%s, %s, %s)"
    

    val = ("andrzej","ziomal",640)
    cs.execute(insert,val)
    con.commit()
    cs.fetchall()

    cs.execute("SELECT * FROM staff")

    for i in cs:
        print(i)

    con.close()






