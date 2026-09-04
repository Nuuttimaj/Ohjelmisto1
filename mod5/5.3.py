#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. 
#Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

luvut=[]

while True:
    komento=input("Anna luku: ")
    if komento == "":
            break
    luvut.append(komento)

luvut.sort()

print(luvut[0])
print(luvut[-1])