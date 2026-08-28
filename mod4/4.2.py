#Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C) ja tulostaa sen sanallisen kuvauksen alla olevan luettelon mukaisesti. Tehtävässä on käytettävä if/elif/else-toistorakennetta.
#LUX on parvekkeellinen hytti yläkannella.
#A on ikkunallinen hytti autokannen yläpuolella.
#B on ikkunaton hytti autokannen yläpuolella.
#C on ikkunaton hytti autokannen alapuolella.
#Jos käyttäjä syöttää kelvottoman hyttiluokan, ohjelma tulostaa Virheellinen hyttiluokka.


hytti= input("Anna hyttisi: ").lower()

if hytti == "a":
    print("A on ikkunallinen hytti autokannen yläpuolella")
elif hytti == "b":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hytti == "c":
    print("C on ikkunaton hytti autokannen alapuolella.")
elif hytti =="lux":
    print("LUX on parvekkeellinen hytti yläkannella.")
else:
    print ("Virheellinen hyttiluokka!")