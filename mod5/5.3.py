#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. 
#Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

luvut=[]

komento=(input("Anna luku: "))
luvut.append(komento)

while True:
    if komento =="":
        break
    komento=(input("Anna luku: "))
    luvut.append(komento)

luvut.sort()

print(luvut[1])
print(luvut[-1])