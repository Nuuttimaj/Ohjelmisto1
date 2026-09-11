#Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän. 
#Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. 
#Käytä for-toistorakennetta.
import random


lukumäärä= int(input("Anna arpakuutioiden määrä: "))
heitot=0
luvut= []


while heitot < lukumäärä:
    luku=int(random.randint(1,6))
    luvut.append(luku)
    heitot= heitot + 1

for x in luvut:
    print (x)
    