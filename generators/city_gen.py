#!/usr/bin/env python3

import random
import os

def generate_city()-> str:
    """
    generuje losowe miasto
    Jako że zakładamy że sklep mieści się we wrocku
    to najczęsciej będzie wypadał wrocław oraz
    miasta w pobliżu, ale jest też szansa na Wawę czy Kraków
    """

    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    os.chdir('cities')

    number_city = random.randrange(0,44)
    f = open("city_names.txt","r",encoding="utf8")
    for i in range(number_city-1):
        f.readline()
    city = f.readline()
    city = city[:-1]
    f.close()

    return(city)


if __name__ == "__main__":
    city = generate_city()
    print(city)
