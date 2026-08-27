
print("Kerro massa keskiaikaisina yksiköinä niin muutan sen kiloiksi grammoiksi!")

luoti_paino=13.3
naula_paino=luoti_paino * 32
leiviska_paino=naula_paino * 20 

#Kysytään arvot
leiviskat= float(input("Anna leivisköjen määrä: "))
naulat= float(input("Anna naulojen määrä: "))
luodit= float(input("Anna luotien määrä: "))

paino= (leiviskat * leiviska_paino + luodit * luoti_paino + naulat * naula_paino)

grammat= paino % 1000
kilot= paino // 1000 

print(f"Kilot: {kilot:.2f}, Grammat: {grammat:.2f}")