#!/usr/bin/env python3

import csv 
import random
import os


def generate_games(n:int):
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    os.chdir('games')
    with open('bgg_dataset.csv', 'r', encoding='utf8') as file:
        reader = csv.reader(file, delimiter=';')
        gry = list(reader)
        del gry[0]
        kolumny_do_usuniecia = [11, 9, 7, 0]
        for row in gry:
            for index in kolumny_do_usuniecia:
                del row[index]

        kolumny = [6, 7]
        for row in gry:
            for index in sorted(kolumny, reverse=True):
                row[index] = row[index].replace(",", ".")
                row[index] = float(row[index])
        kolumny_do_naprawy = [1, 2, 3, 4, 5]
        for row in gry:
            for index in kolumny_do_naprawy:
                try:
                    row[index] = int(row[index])
                except ValueError:
                    pass 

    numerki = random.sample(range(1, len(gry)), n)
    lista = []
    for element in numerki:
        lista.append(gry[element])
    return(lista)

if __name__ == "__main__":
    print(generate_games(2))



