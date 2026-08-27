import math

print("Kerro 3 kokonaislukua, niin lasken niiden summan, tulon ja keskiarvon!")

ensimmäinen= input("Anna Ensimmäinen Luku: ")
toinen= input("Anna Toinen Luku: ")
kolmas= input("Anna Kolmas Luku: ")

summa= (float(ensimmäinen)) + (float(toinen)) + (float(kolmas))
tulo= (float(ensimmäinen)) * (float(toinen)) * (float(kolmas))
keskiarvo= (float(summa)) / 3

print("Summa: " + str(summa))
print("Tulo: " + str(tulo))
print("Keskiarvo: " + str(keskiarvo))