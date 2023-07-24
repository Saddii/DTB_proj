#!/usr/bin/env python3
import random
import os

def generate_person():
    '''
    Generuje krotkę z losowym imieniem i nazwiskiem losowej płci.
    Zwraca imie nazwisko i zmienną Sex która może przyjmować 0 dla mężczyzn i 1 dla kobiet
    zwraca również email zrobiony z imienia i nazwiska
    '''

    os.chdir(os.path.dirname(os.path.abspath(__file__))) #zmieniamy directory na to z projektem
    os.chdir('names')
    

    sex = random.randrange(0,2)
    if sex == 0:
        #generowanie dla male
        number_name = random.randrange(0,100)
        f = open("male_names.txt","r",encoding="utf8")
        for i in range(number_name-1):
            f.readline()
        name = f.readline()
        name = name[:-1]
        f.close()

        number_surname = random.randrange(0,42)
        f = open("male_surnames.txt","r",encoding="utf8")
        for i in range(number_surname-1):
            f.readline()
        surname = f.readline()
        surname = surname[:-1]
        f.close()
        

    else:
        #generowanie dla female
        number_name = random.randrange(0,100)
        f = open(f"female_names.txt","r",encoding="utf8")
        for i in range(number_name-1):
            f.readline()
        name = f.readline()
        name = name[:-1]
        f.close()
        
        number_surname = random.randrange(0,42)
        f = open("female_surnames.txt","r",encoding="utf8")
        for i in range(number_surname-1):
            f.readline()
        surname = f.readline()
        surname = surname[:-1]
        f.close()

    mails = ("gmail.com","interia.pl","gmail.com","wp.pl","gmail.com")
    number_mail = random.randrange(0,5)
    mail_ending = mails[number_mail]
    swapped = bool(random.getrandbits(1))

    if not swapped:
        mail = name.lower() + "." + surname.lower() + "@" + mail_ending
    else:
        mail = surname.lower() + "." + name.lower() + "@"  + mail_ending
    return(name,surname,mail,sex)
        
        
if __name__ == "__main__":
    osoba = generate_person()
    print(osoba[0])
    print(osoba[1])
    print(osoba[2])
    

