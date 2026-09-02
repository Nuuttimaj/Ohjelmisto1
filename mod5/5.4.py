#Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10. 
#Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein. 
#Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein. 
#Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

import random
luku = int(random.randint(1,10))

arvaus= int(input("Anna luku: "))

while arvaus != luku:
    if arvaus > luku:
        print("Liian suuri arvaus")
        arvaus=int(input("Anna uusi luku: "))
    elif arvaus < luku: 
        print("Liian pieni arvaus")
        arvaus=int(input("Anna uusi luku: "))
    else: print("Luku on oikein")
else: print("Luku on oikein")
