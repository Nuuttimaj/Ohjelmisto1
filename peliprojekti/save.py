#Tarvittavat importit
import json
import pelaaja


#Tallenna funktio
def tallenna():
    tallennus_data = {
        "pelaaja": pelaaja.user.nimi,
        "ika": pelaaja.user.ikä,
        "HP": pelaaja.user.hp,
    }

    with open("save.json", "w") as tiedosto:
        json.dump(tallennus_data, tiedosto)

#Lataa funktio
def lataa():
    with open("save.json", "r") as tiedosto:
        data_luettu = json.load(tiedosto)
    return data_luettu
