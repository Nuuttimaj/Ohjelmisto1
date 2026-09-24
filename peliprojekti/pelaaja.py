import päävalikko

from päävalikko import inventaario

from päävalikko import user_name
from päävalikko import user_age

class Pelaaja_class:
    def __init__(self, nimi =user_name, ikä = user_age, sijainti=0, inventaario=inventaario):
        self.nimi = nimi
        self.ikä = ikä
        self.sijainti = sijainti
        self.inventaario = inventaario
    
user=Pelaaja_class



