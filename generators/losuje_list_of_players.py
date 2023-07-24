import mysql.connector
import csv 
import random
from datetime import datetime, timedelta
import math
#ta funkcja potrzebuje losuj_tournaments(dane)[1] (drugi element przy returnie)


def losuj_list_of_players(dane):
    wynik = []
    for i in range(len(dane)):
        lista = random.sample(range(1, 301), dane[i])
        for k in range(len(lista)):
            wynik.append([lista[k],i+1,k+1])
    return wynik


if __name__ == "__main__":
    pass
