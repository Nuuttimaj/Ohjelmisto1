# Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän. 
# Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt. 
# Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. 
# Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka
        

    def kiihdytä(self, muutos):
        muutos > 0
        self.nopeus = self.nopeus + muutos
        if float(self.nopeus) > float(self.huippunopeus):
            self.nopeus = self.huippunopeus
        return muutos

    def kulje(self, kulje):
        kulje > 0
        self.matka = kulje * self.nopeus
        return kulje


auto1=Auto("ABC-123", 142, 60)


kiihdytys1 = auto1.kulje(+2)

print(f"kuljettu matka: {auto1.matka}")

