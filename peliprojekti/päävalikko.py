import time
inventaario=[1,2,3,4,5,6,]


#Funktiot
def invi():
    print(inventaario)

def inviadd():
    Inviadd=input("Mitä haluat lisätä:")
    inventaario.append(Inviadd)

def tiedot():
    print(f"Nimesi: {user_name}")
    print(f"Ikäsi: {user_age}")





#Nimen ja Iän kysyminen
print("Pelaaja, anna nimesi ja ikäsi!")
user_name= str(input("Anna Nimesi: "))
user_age= int(input("Anna Ikäsi: "))

# Iän tarkistus
if user_age < 12:
    print("Alitat ikärajan")


#Päävalikko
while user_age > 12:
    time.sleep(1)
    print(f'''
    Hei,{user_name}!

    Start   Tietosi   Inventaario   Cheat Codes   Shutdown
    >
    ''')
    
    time.sleep(0.5)
    vastaus= str(input("Mihin haluat edetä? ")).lower()
    if vastaus == "start":
        tiedot()
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
    if vastaus == "shutdown":
        time.sleep(1.5)
        print("Shutdown")
        break



