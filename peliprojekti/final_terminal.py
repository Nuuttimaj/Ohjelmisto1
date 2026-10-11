import time
from colours import värit
from pelaaja import user_name


time.sleep(2)
print(f'''{värit.BOLD}{värit.OKGREEN}
        The Organization
        
        Authorized use only

        You may be subjected to bodily harm or death, if you proceed unauthorized
        
        ''')

time.sleep(3)
while True:
    proceed=input(f'''{värit.BOLD}{värit.OKGREEN}
            Press enter to proceed?
            ''')

    if proceed == "":
        break

while True:
    password=input(f'''{värit.BOLD}{värit.OKGREEN}
            Password?
            ''')

    if password == "root":
        break
    print(f"{värit.ENDC}{user_name}: Maybe it's the root password")


while True:
    sf_input=input(f'''{värit.BOLD}{värit.OKGREEN}
            Safe house 87
            > Start exit procedure

            Where do you wish to proceed
            ''')
    if sf_input =="Start exit procedure":
        break

    
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


password =0
while True:
    password = input(f"{värit.BOLD}{värit.OKGREEN}Password:")
    if password == "sesame":
        break
    print(f"{värit.ENDC}{user_name}: Think!")
    print(f"{värit.ENDC}{user_name}: Maybe it's a magic word for opening stuff")


# Ajanotto lopetetaan
end = time.time()


#Aika lasketaan
length = end - start

time.sleep(3)
print(f"{värit.BOLD}{värit.OKGREEN}It took, {length: .2f}, seconds!")
time.sleep(1)
if length >60:
    print(f"{värit.BOLD}{värit.OKGREEN}Thank you for your collaboration, Good Bye!")
    time.sleep(3)
    print("We thank you for playing Safe House 87")
    quit()
if length <60:
    print(f"{värit.BOLD}{värit.OKGREEN}Thank you for your collaboration, have a nice afterlife")

