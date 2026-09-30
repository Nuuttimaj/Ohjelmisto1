# Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi. 
# Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta. 
# Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. 
# Rekisteritunnus luodaan seuraavasti “ABC-1”, “ABC-2” jne. Sitten kilpailu alkaa. 
# Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:

# Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä. 
# Tämä tehdään kutsumalla kiihdytä-metodia.
# Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
# Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä. 
# Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.
import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka
        

    def kiihdytä(self, muutos):
            if self.nopeus + muutos > self.huippunopeus:
                self.nopeus = self.huippunopeus
            elif self.nopeus + muutos < 0:
                self.nopeus = 0
            else:
                self.nopeus = self.nopeus + muutos
            return muutos

    def kulje(self, kulje):
        self.matka += kulje * self.nopeus

        return kulje


autot =[]

#Autot luodaan
for x in range(1,11):
    autot.append(Auto(f"ABC-{[x]}", random.randint (100,200)))



voittaja = False

while voittaja !=True:
    for x in range(len(autot)):
        autot[x].kiihdytä(random.randint(-10, 15))

    for x in range(len(autot)):
        autot[x].kulje(1)

    for x in range(len(autot)):
        if autot[x].matka >= 10000:
            print(f"{autot[x].rekisteritunnus} on voittanut kilpailu")
            voittaja = True
        
print("")
for x in range(len(autot)):
    print(autot[x].rekisteritunnus,autot[x].huippunopeus, autot[x].nopeus, autot[x].matka)