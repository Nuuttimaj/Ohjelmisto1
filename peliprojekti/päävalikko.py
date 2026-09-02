

print("Pelaaja, anna nimesi ja ikäsi!")
user_name= str(input("Anna Nimesi: "))
user_age= float(input("Anna Ikäsi: "))


# Iän tarkistus
while user_age < 12:
    print("Alitat ikärajan")
    break


while user_age > 12:
    print("Hei,"+user_name+"!")
    print("Aloita peli kirjoittamalla: 1")
    print("Asetukset kirjoittamalla: 2")
    print("Pääset pois kirjoittamalla: lopeta")
    vastaus= str(input("Mihin haluat edetä? "))
    if vastaus == "lopeta":
        break
    elif vastaus == 1: print("Aloitetaan peli")
    elif vastaus == 2: print("Asetukset")


        