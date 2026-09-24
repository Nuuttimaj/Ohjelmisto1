# Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan. 
# Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä. 
# Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä. 
# Hissien lista tallennetaan talon ominaisuutena. 
# Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen.
# Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.



class Hissi:
    def __init__(self, kerros=0, alin_kerros=0, ylin_kerros=10):
        self.kerros = kerros
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros

    def siirry_kerrokseen(self, kerros_nro):
        if self.kerros < kerros_nro:
            for x in range(kerros_nro - self.kerros):
                self.kerros_ylös()
        else:
            for y in range(self.kerros - kerros_nro):
                self.kerros_alas()

    def kerros_ylös(self):
        self.kerros += 1
        print(self.kerros) 

    def kerros_alas(self):
        self.kerros -= 1
        print(self.kerros)


class Talo:
    def __init__(self,talon_alin=0, talon_ylin=10, hissien_määrä=5):
        self.talon_alin = talon_alin
        self.talon_ylin = talon_ylin
        self.hissien_määrä = hissien_määrä

    def aja_hissiä(self, hissin_numero, kohdekerros):
        

hissit=[]

talo1 = Talo()
for x in range(1,5):
    hissit.append(Hissi[x])
print (hissit)
