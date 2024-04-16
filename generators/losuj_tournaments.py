import mysql.connector
import csv 
import random
from datetime import datetime, timedelta
import math
#from losuje_games import generate_games

def ile_spotkan(k):
    liczba_graczy_w_jednej_grze = k
    if liczba_graczy_w_jednej_grze <= 3:
        liczba_graczy_w_sumie = liczba_graczy_w_jednej_grze**(3)
        return(int(sum([liczba_graczy_w_sumie/liczba_graczy_w_jednej_grze**x  for x in range(1,4)])),liczba_graczy_w_sumie)
    elif liczba_graczy_w_jednej_grze <=7:
        liczba_graczy_w_sumie = liczba_graczy_w_jednej_grze**(2)
        return(int(sum([liczba_graczy_w_sumie/liczba_graczy_w_jednej_grze**x  for x in range(1,4)])),liczba_graczy_w_sumie)
    elif liczba_graczy_w_jednej_grze <=10: 
        liczba_graczy_w_sumie = liczba_graczy_w_jednej_grze
        return(1, liczba_graczy_w_sumie)
    else: 
        liczba_graczy_w_sumie = 20 + random.randint(-7,7)
        return(1, liczba_graczy_w_sumie) 
    

#to potrzebuje danych z losuj_games


def losuj_tournament(dane):
    lista = []
    list_pomoc = []
    numerki = random.choices(range(0, 40), k=random.randint(500,600))
    for i in range(len(numerki)):
        while dane[numerki[i]][3] == 1 or dane[numerki[i]][3] == 0:
            numerki[i] = random.randint(0, 39)   
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2022, 12, 31)
    for i in range(len(numerki)):
        lista.append([numerki[i]+1])
        s_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days)) + timedelta(hours = 20) + timedelta(minutes = random.randint(-10,10)) + timedelta(seconds= random.randint(0,59))
        lista[i].append(s_date)
        liczba_dni_i_ludzi = ile_spotkan(dane[numerki[i]][3])
        liczba_dni = liczba_dni_i_ludzi[0]
        list_pomoc.append(liczba_dni_i_ludzi[1])
        e_date = s_date + timedelta(days = liczba_dni - 1) + timedelta(minutes=dane[numerki[i]][4] - random.randint(-7,7))
        lista[i].append(e_date)
        lista[i].append(random.randint(300,700))
    return(lista,list_pomoc) #zwracam tylko jedną liste ta pomocnicza jest mi potrzebna do innej tabeli

if __name__ == "__main__":
    pass
    #dane = generate_games(40)
    #print(len(losuj_tournament(dane)[0]))