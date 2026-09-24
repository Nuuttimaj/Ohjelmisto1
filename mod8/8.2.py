# Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon. 
# Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan, 
# syötettiinkö nimi ensimmäistä kertaa. 
# Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä. 
# Käytä joukkotietorakennetta nimien tallentamiseen.

nimet = set()

vastaus= 0

while vastaus != "":
    vastaus = input("Anna nimi: ")
    if vastaus in nimet:
        print ("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        nimet.add(vastaus)

nimet.remove("")
for x in nimet:
    print(x)