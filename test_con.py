import mysql.connector
con = mysql.connector.connect(
            host = "127.0.0.1",
            user = "root",
            password = "password",
            database = "clients_base",
            port= 3307
            )