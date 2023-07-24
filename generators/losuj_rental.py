#!/usr/bin/env python3

import random
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def znajdz_duplikaty(lista):
    duplikaty = []
    for i in range(len(lista)):
        if lista.count(lista[i]) > 1 and lista[i] not in duplikaty:
            duplikaty.append(lista[i])
    return duplikaty

def zlicz_powtorzenia(lista):
    zliczenia = {}
    for element in lista:
        if element in zliczenia:
            zliczenia[element] += 1
        else:
            zliczenia[element] = 1
    return zliczenia

def spradz_czy_przekroj_pusty(daty):
    daty = sorted(daty, key=lambda x: x[0])
    for i in range(len(daty)):
        roznica = relativedelta(days = 0)
        for k in range(len(daty)):
            if k <= i:
                continue
            if daty[i][1] > daty[k][0]:
                roznica += relativedelta(days = (daty[i][1] - daty[k][0]).days) 
                daty[k][0] = daty[k][0] +  (roznica + relativedelta(days = 1))
                daty[k][1] = daty[k][1] +  (roznica + relativedelta(days = 1))
    return daty




def losuj_daty(ile_razy):
    start_date = datetime(2020, 1, 1)
    start_date = start_date.date() 
    wynik = []
    for i in range(ile_razy):
        rok = random.randint(0,2)
        s_date = start_date + relativedelta(years=rok) + relativedelta(months=random.randint(1, 12)) + relativedelta(days=random.randint(1, 28))
        e_date = s_date + timedelta(days=random.randint(2, 60))
        wynik.append([s_date, e_date])
    return(wynik)


def losuj_rental(p, k, ile_gier):
    wynik = []
    liczba_wypozyczen = random.randint(p, k)
    numerki = random.choices(range(1, ile_gier), k=liczba_wypozyczen)
    slownik = zlicz_powtorzenia(numerki)
    for klucz, wartosc in slownik.items():
        slownik[klucz] = spradz_czy_przekroj_pusty(losuj_daty(wartosc))
        for x in slownik[klucz]:
            wynik.append([klucz, x[0], x[1]])
    for w in wynik:
        w.append(random.randint(1,300))
        w.append(random.randint(1,5))
        w[1], w[3] = w[3], w[1]
        w[2], w[4] = w[4], w[2]
    return wynik

if __name__ == "__main__":
    dane = losuj_rental(4000,12000, 400)
    print(dane)


