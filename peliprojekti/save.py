import json
import pelaaja


def tallenna():
    tallennus_data = {
        "pelaaja": pelaaja.user.nimi,
        "ika": pelaaja.user.ikä,
        "taso": pelaaja.user.taso,
        "HP": pelaaja.user.hp,
    }

    with open("save.json", "w") as tiedosto:
        json.dump(tallennus_data, tiedosto)

def lataa():
    with open("save.json", "r") as tiedosto:
        data_luettu = json.load(tiedosto)
    return data_luettu
    

# print(f"Pelaaja: {data_luettu['pelaaja']}, ikä: {data_luettu['ikä']}, taso: {data_luettu['taso']}, HP: {data_luettu['HP']}")
