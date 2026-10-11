#Nimen ja iän kysyminen
print("Pelaaja, anna nimesi ja ikäsi!")
user_name= str(input("Anna Nimesi: "))
user_age= int(input("Anna Ikäsi: "))

#Inventaario
inventaario=["Wedding Ring", "Watch"]


#Pelaajan class
class Pelaaja_class:
    def __init__(self, nimi =user_name, ikä = user_age, hp=100):
        self.nimi = nimi
        self.ikä = ikä
        self.hp = hp

    def hp_muutos(self, muutos):
        self.hp = self.hp - muutos
        return muutos



user=Pelaaja_class(user_name, user_age)


