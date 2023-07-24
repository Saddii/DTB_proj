#!/usr/bin/env python3

import numpy as np
import math

def random_age_worker():
    '''
    zwraca losowy wiek z rozkładu normalnego 
    o średniej 30 który musi być większy niż 17 i mniejszy niż 60
    '''
    token = False
    while token is not True:
        age = math.ceil(np.random.normal(25,5,None))
        if age >= 18 and age <= 60:
            token = True
    return age

def random_age_customer():
    '''
    zwraca losowy wiek osoby kupującej lub grającej w gry
    '''
    token = False
    while token is not True:
        age = math.ceil(np.random.normal(24,9,None))
        if age >= 14 and age <= 90:
            token = True
    return age


if __name__ == "__main__":
    print(f"worker age:{random_age_worker()}")
    print(f"customer age:{random_age_customer()}")
