import math

print("Kerro suorakulmion kanta ja korkeus, niin lasken pinta alan sekä piirin!")
kanta= input("Anna Kanta: ")
korkeus= input("Anna Korkeus: ")

pinta_ala= (float(kanta)) * (float(korkeus))
piiri= (float(kanta) * 2) + (float(korkeus) * 2)

print("Pinta_ala: " + str(pinta_ala))
print("Piiri: " + str(piiri))