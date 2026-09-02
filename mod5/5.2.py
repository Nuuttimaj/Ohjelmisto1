#Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän. 
#Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm

komento = float(input("Anna tuumien määrä niin muutan sen senttimetreiksi: "))
while komento  >0 :
    print(komento * 2.54)
    komento= float(input("Anna tuumien määrä niin muutan sen senttimetreiksi: "))
print("Toiminto lopetettu")
