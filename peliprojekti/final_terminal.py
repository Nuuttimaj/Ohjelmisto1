#Tarvittavat importit
import time
from colours import värit
from pelaaja import user_name
from pelaaja import inventaario
import os

#Terminaalin aloitus
time.sleep(2)
print(f'''{värit.BOLD}{värit.OKGREEN}
        The Organization
        
        Authorized use only

        You may be subjected to bodily harm or death, if you proceed unauthorized
        
        ''')

#Haluatko, jatkaa eteenpäin
time.sleep(3)
while True:
    proceed=input(f'''{värit.BOLD}{värit.OKGREEN}
            Press enter to proceed?
            ''')

    if proceed == "":
        break

#Salasana
while True:
    password=input(f'''{värit.BOLD}{värit.OKGREEN}
            Password?
            ''')

    if password == "root":
        break
    #Salasanaa ehdotetaan, jos aikaisemmin löydetty note lisättiin inventaarioon.
    if "Note" in inventaario:
        print(f"{värit.ENDC}{user_name}: Maybe root")
    else:
        print(f"{värit.ENDC}{user_name}: What did that note say?")


#Mihin haluat jatkaa
while True:
    sf_input=input(f'''{värit.BOLD}{värit.OKGREEN}
            Safe house 87
            > Start exit procedure

            Where do you wish to proceed
            ''').lower()
    if sf_input =="start exit procedure":
        break

#Exit procedure
time.sleep(2)
print(f'''{värit.BOLD}{värit.OKGREEN}
General Fields, Director of security

You have exactly 60 seconds to type in the correct password.

Otherwise the room will be filled with gas and you will be killed.

Good luck!
''')

# Ajanotto aloitetaan
time.sleep(1)
start = time.time()


time.sleep(3)
print(f"{värit.ENDC}{user_name}: I'm so close!")
time.sleep(1)
print(f"{värit.ENDC}{user_name}: Let's think about everything we have seen")

#Salasana
password =0
while True:
    password = input(f"{värit.BOLD}{värit.OKGREEN}Password:")
    if password == "sesame":
        break
    print(f"{värit.ENDC}{user_name}: Think!")
    #Salasanaa ehdotetaan, jos aikaisemmin löydetty note lisättiin inventaarioon.
    if "Note" in inventaario:
        print(f"{värit.ENDC}{user_name}: Maybe sesame")
    else:
        print(f"{värit.ENDC}{user_name}: Maybe it's a magic word for opening stuff")

# Ajanotto lopetetaan
end = time.time()



#Aika lasketaan
length = end - start


#Pelaaja kuolee välittömästi, jos aika on yli 60s. Pelaaja saa jatkaa matkaa, jos aika on alle 60s
time.sleep(3)
print(f"{värit.BOLD}{värit.OKGREEN}It took, {length: .2f}, seconds!")
time.sleep(1)
if length >60:
    time.sleep(1)
    print(".")
    print(f"{user_name}: What's happening?")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(f"{user_name}: What's that gas?")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(f"{user_name}: I can't breathe!")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(f"{user_name}: You sons of........")
    time.sleep(2)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(3)
    os.system('say "The plan has been completed, there are no more future for mankind"')
    print("We thank you for playing Safe House 87")
    quit()
if length <60:
    print(f"{värit.BOLD}{värit.OKGREEN}Thank you for your collaboration, have a nice afterlife")

