import random
import time

lijstje = ' appel_1 '

print("je hebt" + (lijstje) + "in je inventory")

geldige_keuze = False
while not geldige_keuze:
    print("wil je nog een appel in je invetory JA of NEE")
    choice = input()
    if choice == 'JA':
        lijstje.append("appel_2")
        lijstje.remove("appel_1")
        print("je hebt nu" + (lijstje) + "in je inventorie")
        geldige_keuze = True 
    elif choice == 'NEE':
        print("je hebt geen nieuwe appels in je inventory")
        geldige_keuze = True
    else:
        print("Dit is geen geldige keuze")
        
        
