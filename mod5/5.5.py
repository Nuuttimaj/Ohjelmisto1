#Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan. 
#Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen. 
#Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa. 
#Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty. 
#(Oikea käyttäjätunnus on python ja salasana rules).


username= input("Anna käyttäjänimesi: ")
password= input("Anna salasanasi: ")
yritykset=1

while yritykset< 5: 
    if username == "python":
        if password == "rules":
            print("Tervetuloa!")
            break
    yritykset=yritykset + 1
    input("Anna käyttäjänimesi: ")
    input("Anna salasanasi: ")
else:  
    print("Pääsy evätty!")