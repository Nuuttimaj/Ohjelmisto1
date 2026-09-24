print("Pelaaja, anna nimesi ja ikäsi!")
user_name= str(input("Anna Nimesi: "))
user_age= int(input("Anna Ikäsi: "))

inventaario=[1,2,3,4,5,6,]



class Pelaaja_class:
    def __init__(self, nimi =user_name, ikä = user_age, sijainti=0, inventaario=inventaario):
        self.nimi = nimi
        self.ikä = ikä
        self.sijainti = sijainti
        self.inventaario = inventaario
    
user=Pelaaja_class



