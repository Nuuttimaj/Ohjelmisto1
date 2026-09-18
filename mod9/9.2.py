# Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden muutoksen (km/h). 
# Jos nopeuden muutos on negatiivinen, auto hidastaa. Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa. 
# Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi. 
# Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h. 
# Tulosta tämän jälkeen auton nopeus. Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus.
# Kuljettua matkaa ei tarvitse vielä päivittää.


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka
        

    def kiihdytä(self, muutos):
        self.nopeus = self.nopeus + muutos
        if float(self.nopeus) > float(self.huippunopeus):
            self.nopeus = self.huippunopeus
        if float(self.nopeus) < 0:
                    self.nopeus = 0
        return muutos


auto1=Auto("ABC-123", 142)

kiihdytys1 = auto1.kiihdytä(+30)
kiihdytys2 = auto1.kiihdytä(+70)
kiihdytys3 = auto1.kiihdytä(+50)


print(f"Nopeus: {auto1.nopeus}")
jarrutus = auto1.kiihdytä(-200)
print(f"Nopeus: {auto1.nopeus}")
