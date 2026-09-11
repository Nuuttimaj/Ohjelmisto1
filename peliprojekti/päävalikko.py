inventaario=[1,2,3,4,5,6,]


#Funktiot
def invi():
    print(inventaario)

def inviadd():
    Inviadd=input("Mitä haluat lisätä:")
    inventaario.append(Inviadd)







#Nimen ja Iän kysyminen
print("Pelaaja, anna nimesi ja ikäsi!")
user_name= str(input("Anna Nimesi: "))
user_age= float(input("Anna Ikäsi: "))

# Iän tarkistus
if user_age < 12:
    print("Alitat ikärajan")


#Päävalikko
while user_age > 12:
    print(" ")
    print("Hei,"+user_name+"!")
    print(" ")
    print("Aloita peli kirjoittamalla: 1")
    print(" ")
    print("XX: 2")
    print(" ")
    print("Tarkastele inventaariotasi: 3")       
    print(" ")
    print("Cheat Codes: 4")
    print(" ")
    print("Shutdown: X")
    print(" ")
    vastaus= str(input("Mihin haluat edetä? "))
    if vastaus == "3":
        print("Inventaariosi:")
        invi()
    if vastaus == "4":
        inviadd()
    if vastaus == "X":
            print("Shutdown")
            break

        