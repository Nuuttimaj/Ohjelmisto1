print("Pelaaja, anna nimesi ja ikäsi!")
user_name= str(input("Anna Nimesi: "))
user_age= int(input("Anna Ikäsi: "))

inventaario=[1,2,3,4,5,6,]



class Pelaaja_class:
    def __init__(self, nimi =user_name, ikä = user_age, hp=100, taso=0):
        self.nimi = nimi
        self.ikä = ikä
        self.hp = hp
        self.taso = taso

    def hp_muutos(self, muutos):
        if muutos > 0:
            self.hp = self.hp - muutos
        if muutos < 0:
            self.hp = self.hp + muutos
        return muutos



user=Pelaaja_class(user_name, user_age)


