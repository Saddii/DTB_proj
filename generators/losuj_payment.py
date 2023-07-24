#!/usr/bin/env python3
import math
from scipy.stats import arcsine
import numpy as np
import random
from datetime import datetime, timedelta
#from losuj_rental import losuj_rental


def last_rental_id(dane, wartosc):
    ostania_data = datetime(2000, 1, 1).date()
    wynik = 0
    for i in dane:
        if i[5] > ostania_data and i[1] == wartosc :
            ostania_data = i[5]
            wynik = i[0]
    return wynik, ostania_data



def wywnioskuj_dane(dane):
    wynik = {}
    dane_nowe = []
    for wartosci in dane:
        dane_nowe.append([wartosci[0],(wartosci[4] - wartosci[3]).days])
    for wartosci in dane_nowe:
        if wartosci[0] in wynik:
            wynik[wartosci[0]] += wartosci[1] 
        else:
            wynik[wartosci[0]] = wartosci[1]
    return dane_nowe,wynik


def znajdz_najblizsza_wartosc(lista, zadana_wartosc):
    return min(lista, key=lambda x: abs(x - zadana_wartosc))

def znajdz_klucze_wedlug_wartosci(slowo, wartosc):
    klucze = []
    for klucz, wart in slowo.items():
        if wart == wartosc:
            klucze.append(klucz)
    return klucze


def losuj_do_kupna(dane):
    do_kupna = []
    wynik = []
    praca = wywnioskuj_dane(dane)[1]
    lista = list(praca.values())
    posortowana_lista = sorted(lista)
    a = min(posortowana_lista)
    b = max(posortowana_lista)
    sample = arcsine.rvs(a, b, size = math.floor(0.7 * len(posortowana_lista)))
    for x in sample:
        do_kupna.append(znajdz_najblizsza_wartosc(posortowana_lista, x))
    for x in do_kupna:
        wynik.append(znajdz_klucze_wedlug_wartosci(praca,x))
    wynik = list(set(sum(wynik, [])))
    return wynik


def znizka(dni):
    return 200 - dni

def losuj_payment(dane):
    wynik = []
    dni = wywnioskuj_dane(dane)[1]
    numerki = losuj_do_kupna(dane)
    for i in range(0,len(dane)):
        dane[i].insert(0, i+1)
    for krok in dane:
        wynik.append([krok[0],krok[1],krok[2],krok[3],krok[5],(krok[5]-krok[4]).days])
    for krok in wynik:
        if krok[1] in numerki:
            pomoc = last_rental_id(dane, krok[1])
            if random.randint(0, 1) == 1:
                c = pomoc[1]
                b = krok[2]
            else:
                c = pomoc[1] + timedelta(days = random.randint(1, 50))
                b = random.randint(1, 300)
            wynik.append([f"last rental_id {pomoc[0]}",b,random.randint(1, 5),c,znizka(dni[krok[1]])])
            numerki.remove(krok[1])
            krok.remove(krok[1])
        elif not isinstance(krok[0], int):
            pass
        else:
            krok.remove(krok[1])         
    return(wynik)

#dane = losuj_rental(400, 600, 400)
#print(losuj_payment(dane))

if __name__ == "__main__":
    pass 