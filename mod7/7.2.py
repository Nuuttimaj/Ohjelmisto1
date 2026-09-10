#Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän. 
#Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa. 
#Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku, 
#joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random

maksimi= int(input("Mikä on nopan maksimiluku: "))

def heitto():
    x=random.randint(1,maksimi)
    return x

while True:
    luku= heitto()
    print(luku)
    if luku ==maksimi:
       break