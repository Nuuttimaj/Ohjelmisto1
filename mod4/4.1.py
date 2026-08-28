#Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä. 
# Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle
# ,montako senttiä alimmasta sallitusta pyyntimitasta puuttuu. 
# Kuha on alamittainen, jos sen pituus on alle 37 cm.

pituus = float(input("Anna kuhan pituus senttimetreinä:"))
if pituus >= 37:
    print("Onneksi Olkoon, Kalamies")

if pituus < 37:
    print("Kuha pitää päästää järveen, koska se on alimittainen")

if pituus < 37:
    erotus = 37 - float(pituus)
    print(f"Kuha on {erotus:.2}cm alimittainen")