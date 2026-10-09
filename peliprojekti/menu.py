import time

from pelaaja import inventaario
from pelaaja import user
import save


#Funktiot
def invi():
    print(inventaario)

def inviadd():
    Inviadd=input("Mitä haluat lisätä:")
    inventaario.append(Inviadd)

def tiedot():
    print(f"Nimesi: {user.nimi}")
    print(f"Ikäsi: {user.ikä}")
    print(f"HP: {user.hp} ")


def menu():
        if user.ikä < 12:
            print("Alitat ikärajan")
            quit()
        while user.ikä > 12:
            time.sleep(1)
            print(f'''
        Hei,{user.nimi}!

        Start   Tietosi   Inventaario   Cheat Codes   Load   Shutdown
        >
        ''')
    
            time.sleep(0.5)
            vastaus= str(input("Mihin haluat edetä? ")).lower()
            if vastaus == "start":
                break
            if vastaus == "tietosi":
                time.sleep(0.5)
                tiedot()
            if vastaus == "inventaario":
                time.sleep(0.5)
                print("Inventaariosi:")
                time.sleep(0.5)
                invi()
            if vastaus == "cheat codes":
                time.sleep(0.5)
                inviadd()
            if vastaus =="load":
                tallennus_data = save.lataa()
                user.nimi = tallennus_data["pelaaja"]
                user.ikä = tallennus_data["ika"]
                user.hp = tallennus_data["HP"]

            if vastaus == "shutdown":
                time.sleep(1.5)
                print("Shutdown")
                quit()

#Tarvitaan, jotta päävalikko toimii
menu()

