#Tarvittavat funktiot
import time
from colours import värit
from pelaaja import user_name
import save

#Vastaukset lista, josta myöhemmin tarkistetaan mitä pelaaja on klikannut.
vastaukset = []

#Menu
time.sleep(2)
print(f'''{värit.BOLD}{värit.OKGREEN}
        The Organization
        
        Authorized use only

        You may be subjected to bodily harm or death, if you proceed unauthorized
        
        ''')

time.sleep(3)

#Haluatko jatkaa
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

    if password == "Password1":
        break
    print(f"{värit.ENDC}{user_name}: Let's try the usual one, maybe Password1")

#Menu
while True:
    sf_input=input(f'''{värit.BOLD}{värit.OKGREEN}
            Safe house 87
            > Personnel
            > Latest Log
            > Save current stage
            > Exit

            Where do you wish to proceed
            ''').lower()
    
    #Henkilöstö
    if sf_input == "personnel":
        time.sleep(1)
        print(f'''{värit.BOLD}{värit.OKGREEN}
        Doctor Collins, Medical supervisor
        General Fields, Director of security
        Classified, Classified
        ''')
        time.sleep(1)

    #Lokikirjoitus    
    if sf_input =="latest log":
        vastaukset.append("Latest Log")
        time.sleep(1)
        print(f'''{värit.BOLD}{värit.OKGREEN}
        Doctor Collins, Medical Supervisor

        The Plan has started, their wake up time has been set and "it" has been planted.

        We are moving to the safe room to observe and execute the final step of the plan if needed.

        All hail The Organization! 
        ''')
        time.sleep(5)
        print(f"{värit.ENDC}{user_name}: What plan?")

    #Tallennus    
    if sf_input =="save current stage":
        save.tallenna()
        print(f"{värit.ENDC}Saved")

    #Exit    
    if sf_input =="exit":
        break







