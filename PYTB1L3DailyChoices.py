print("---------------------------------------------------------------------------")
geldige_keuze = False
while not geldige_keuze:
    print("Je alarm gaat af ga je OPSTAAN of SNOOZEN")
    choice = input()
    if choice == 'OPSTAAN':
        print("je word wakker en bent klaar voor de dag")
        geldige_keuze = True 
    elif choice == 'SNOOZEN':
        print("je gaat weer lekker verder slapen.")
        geldige_keuze = True
    else:
        print("Dit is geen geldige keuze")

print("---------------------------------------------------------------------------")
    
    print("je staat op welk shirt doe je aan de ZWARTE of de RODE")
    choice = input()
    if choice == 'ZWARTE':
        print("Je doet het zwarte shirt aan en gaat naar beneden")
        geldige_keuze = True 
    elif choice == 'RODE':
        print("Je doet het rode shirt aan en gaat naar beneden")
        geldige_keuze = True
    else:
        print("Dit is geen geldige keuze")

print("---------------------------------------------------------------------------")
    print("je bent beneden wat ga je eten TOSTI of MUSLI")
    choice = input()
    if choice == 'TOSTI':
        print("Je maakt een tosti en maakt je klaar om naar school te gaan")
        geldige_keuze = True 
    elif choice == 'MUSLI':
        print("je pakt wat musli en maakt je klaar om naar school te gaan")
        geldige_keuze = True
    else:
        print("Dit is geen geldige keuze")

print("---------------------------------------------------------------------------")
    print("je hebt je klaar gemaakt en gaat naar buiten maar met wat ga je de FIETS of de SCOOTER")
    choice = input()
    if choice == 'FIETS':
        print("Je pakt de fiets en gaat naar school")
        geldige_keuze = True 
    elif choice == 'SCOOTER':
        print("Je pakt de scooter en gaat naar school")
        geldige_keuze = True
    else:
        print("Dit is geen geldige keuze")

print("---------------------------------------------------------------------------")
     print("Je bent op school je hebt nog een half uur voordat het begint wat ga je doen naar je VRIENDEN of VIDEO kijken")
    choice = input()
    if choice == 'VRIENDEN':
        print("Je gaat naar je vrienden en gaat gezellig praten")
        geldige_keuze = True 
    elif choice == 'VIDEO':
        print("Je pakt je telefoon en gaat een video kijken")
        geldige_keuze = True
    else:
        print("Dit is geen geldige keuze")
