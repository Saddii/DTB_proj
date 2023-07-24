#!/usr/bin/env python3

import random
import numpy as np
import os
import math

def address_gen():
    """
    zwraca losowy adres
    złożony z nazwy ulicy i numeru
    """
    
    #nazwa ulicy
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    os.chdir('addresses')

    number_street = random.randrange(0,42)
    f = open("addresses.txt","r",encoding="utf8")
    for i in range(number_street-1):
        f.readline()
    street = f.readline()
    street = street[:-1]
    f.close()
    #################################
    #numer

    token = False
    while token is not True:
        number = math.ceil(np.random.normal(10,9,None))
        if number >= 1 and number <= 60:
            token = True
    
    adres = street + " " + str(number)
    return(adres)
if __name__ == "__main__":
    adres = address_gen()
    print(adres)
    print(type(adres))
