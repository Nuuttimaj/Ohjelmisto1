#Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l). 
# Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.
#Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
#Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.



hb = float(input("Anna Hemoglobiiniarvosi: "))

g= input("Kerro sukupuolesi: ").lower()

if g == "mies":
    if hb <= 134:
        print("Hemoglobiinisi on matala")
    elif hb >= 195:
        print("Hemoglobiinisi on korkea")
    else: print("Hemoglobiinisi on normaali")

if g == "nainen":
    if hb <= 117:
        print("Hemoglobiinisi on matala")
    elif hb >= 175:
        print("Hemoglobiinisi on korkea")
    else: print("Hemoglobiinisi on normaali")
