#Kirjoita while-toistorakennetta käyttävä ohjelma, joka tulostaa kolmella jaolliset luvut väliltä 1..1000.



luku = 3
while luku < 1000:
    print(luku)
    if luku % 3 ==0:
        luku = luku +3