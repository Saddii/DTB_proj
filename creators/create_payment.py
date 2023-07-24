#!/usr/bin/env python3

def create_payment(con):
    """
    funkcja tworząca tabelę payment
    """
    cs = con.cursor()
    table = "CREATE OR REPLACE TABLE payment(payment_id SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY, rental_id_or_last_rental_id VARCHAR(40) DEFAULT NULL,customer_id SMALLINT UNSIGNED NOT NULL,staff_id SMALLINT UNSIGNED NOT NULL,payment_date DATE NOT NULL,amount SMALLINT NOT NULL)"
    cs.execute(table)
    cs.fetchall()

    #alter1 = "ALTER TABLE payment ADD CONSTRAINT payment_date_in_bounds CHECK (payment_date <= '2022-12-01' AND payment_date >= '2014-01-01')"
    #cs.execute(alter1)


if __name__ == "__main__":
    pass






