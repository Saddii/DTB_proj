#!/usr/bin/env python3

import random
import datetime
import pandas as pd

#Założenia
#uznajemy że sklep działa od 201? do 2022
#żeby nie było problemu z datami których nie było
#Zakładamy że sklep pracuje w weekendy

def date_gen(start_date:str = "2014-01-01",s:int = 0,k:int = 3287) -> str:
    """
    start_date:str data od której tworzymy przedział
    deafaultowo 2014-01-01 jako pierwsza data od której działa sklep
    s:int początek przedziału z którego losujemy
    s = 0 oznacza że losujemy od start_date
    defaultowo 0
    
    k:int ile dni zawiera przedział
    defaultowo 3287 bo tyle jest dni do 2022-12-31 
    
    
    """
    start_date = datetime.datetime.strptime(start_date,"%Y-%m-%d")
    #w kalkulatorze dat tyle dni jest między startem a końcem
    #pandas generuje listę możliwych dat
    date_generated=pd.date_range(start_date, periods = k)
    random_date = random.randrange(s,k,1)
    return(date_generated[random_date].strftime("%Y-%m-%d"))
    


if __name__ == "__main__":
    
    print(date_gen())
