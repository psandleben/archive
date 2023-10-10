# bei der AI schauen das der Computer dich nicht Überschreibt
import random
import time

#Variablen:

Feld1 = " "
Feld2 = " "
Feld3 = " "
Feld4 = " "
Feld5 = " "
Feld6 = " "
Feld7 = " "
Feld8 = " "
Feld9 = " "
Spieler = "None"
Gewinner = "None"
PC = "None"
weiter2  = "None"
weiter3 = "None"
#Begrüßung
#definitionen


        
#Spielbrett:
def spielbrett():
    print(" ___________")
    print("| "+ str(Feld1) + " | " + str(Feld2) + " | " + str(Feld3) +" | ")
    print("| "+ str(Feld4) + " | " + str(Feld5) + " | " + str(Feld6) +" | ")
    print("| "+ str(Feld7) + " | " + str(Feld8) + " | " + str(Feld9) +" | ")
    print(" ___________")
spielbrett()

#Spielablauf
while Gewinner == "None":
    weiter2  = "None"
    while weiter2 == "None":
        Spieler = input("Wo möchten sie setzen(1, 2, ..., 9)? ")
        if Spieler == "1" and Feld1 == " ":
            Feld1 = "+"
            weiter2 = "ja"
        elif Spieler == "2" and Feld2 == " ":
            Feld2 = "+"
            weiter2 = "ja"
        elif Spieler == "3" and Feld3 == " ":
            Feld3 = "+"
            weiter2 = "ja"
        elif Spieler == "4" and Feld4 == " ":
            Feld4 = "+"
            weiter2 = "ja"
        elif Spieler == "5" and Feld5 == " ":
            Feld5 = "+"
            weiter2 = "ja"
        elif Spieler == "6" and Feld6 == " ":
            Feld6 = "+"
            weiter2 = "ja"
        elif Spieler == "7" and Feld7 == " ":
            Feld7 = "+"
            weiter2 = "ja"
        elif Spieler == "8" and Feld8 == " ":
            Feld8 = "+"
            weiter2 = "ja"
        elif Spieler == "9" and Feld9 == " ":
            Feld9 = "+" 
            weiter2 = "ja"
        else:
            print("Dieses Feld ist bereits vergeben")
    print("der Computer setzt...")
    time.sleep(1)
    weiter3 = "None"
    while weiter3 == "None":
#waagrecht:
        #oben
        if weiter3 == "None" and Feld1 == "+" and Feld2 == "+" and Feld3 == "":
        	Feld3 = "-"
        	weiter3 = "ja"
        elif weiter3 == "None" and Feld2 == "+" and Feld3 == "+":
        	Feld1 = "-"
        	weiter3 = "ja"
        elif weiter3 == "None" and Feld1 == "+" and Feld3 == "+":
        	Feld2 = "-"
        	weiter3 = "ja"
        #mitte
        elif weiter3 == "None" and Feld4 == "+" and Feld5 == "+":
        	Feld6 = "-"
        	weiter3 = "ja"
        elif weiter3 == "None" and Feld5 == "+" and Feld6 == "+":
        	Feld4 = "-"
        	weiter3 = "ja"
        elif weiter3 == "None" and Feld4 == "+" and Feld6 == "+":
        	Feld5 = "-"
        	weiter3 = "ja"
        #unten
        elif weiter3 == "None" and Feld7 == "+" and Feld8 == "+":
        	Feld9 = "-"
        	weiter3 = "ja"
        elif weiter3 == "None" and Feld8 == "+" and Feld9 == "+":
        	Feld7 = "-"
        	weiter3 = "ja"
        elif weiter3 == "None" and Feld7 == "+" and Feld9 == "+":
        	Feld8 = "-"
        	weiter3 = "ja"
#senkrecht
        #links
        elif weiter3 == "None" and Feld1 == "+" and Feld4 == "+":
        	Feld7 = "-"
        	weiter3 = "ja"
        elif weiter3 == "None" and Feld4 == "+" and Feld7 == "+":
        	Feld1 = "-"
        	weiter3 = "ja"
        elif weiter3 == "None" and Feld1 == "+" and Feld7 == "+":
        	Feld4 = "-"
        	weiter3 = "ja"
        #mitte
        elif weiter3 == "None" and Feld2 == "+" and Feld5 == "+":
        	Feld8 = "-"
        	weiter3 = "ja"
        elif weiter3 == "None" and Feld8 == "+" and Feld5 == "+":
        	Feld2 = "-"
        	weiter3 = "ja"
        elif weiter3 == "None" and Feld8 == "+" and Feld2 == "+":
        	Feld5 = "-"
        	weiter3 = "ja"
        #rechts
        elif weiter3 == "None" and Feld3 == "+" and Feld6 == "+":
        	Feld9 = "-"
        	weiter3 = "ja"
        elif weiter3 == "None" and Feld6 == "+" and Feld9 == "+":
        	Feld3 = "-"
        	weiter3 = "ja"
        elif weiter3 == "None" and Feld3 == "+" and Feld9 == "+":
        	Feld6 = "-"
        	weiter3 = "ja"
#Kreuz
        #links-rechts
        elif weiter3 == "None" and Feld1 == "+" and Feld5 == "+":
        	Feld9 = "-"
        	weiter3 = "ja"
        elif weiter3 == "None" and Feld5 == "+" and Feld9 == "+":
        	Feld1 = "-"
        	weiter3 = "ja"
        elif weiter3 == "None" and Feld1 == "+" and Feld9 == "+":
        	Feld5 = "-"
        	weiter3 = "ja"
        #rechts-links
        elif weiter3 == "None" and Feld3 == "+" and Feld5 == "+":
        	Feld7 = "-"
        	weiter3 = "ja"
        elif weiter3 == "None" and Feld5 == "+" and Feld7 == "+":
        	Feld3 = "-"
        	weiter3 = "ja"
        elif weiter3 == "None" and Feld3 == "+" and Feld7 == "+":
        	Feld5 = "-"
        	weiter3 = "ja"
        else:
	        PC = random.randint(1, 10)
	        PC = str(PC)
	        if PC == "1" and Feld1 == " ":
	            Feld1 = "-"
	            weiter3 = "ja"
	        elif PC == "2" and Feld2 == " ":
	            Feld2 = "-"
	            weiter3 = "ja"
	        elif PC == "3" and Feld3 == " ":
	            Feld3 = "-"
	            weiter3 = "ja"
	        elif PC == "4" and Feld4 == " ":
	            Feld4 = "-"
	            weiter3 = "ja"
	        elif PC == "5" and Feld5 == " ":
	            Feld5 = "-"
	            weiter3 = "ja"
	        elif PC == "6" and Feld6 == " ":
	            Feld6 = "-"
	            weiter3 = "ja"
	        elif PC == "7" and Feld7 == " ":
	            Feld7 = "-"
	            weiter3 = "ja"
	        elif PC == "8" and Feld8 == " ":
	            Feld8 = "-"
	            weiter3 = "ja"
	        elif PC == "9" and Feld9 == " ":
	            Feld9 = "-" 
	            weiter3 = "ja"
    spielbrett()
    #Schaut ob computer gewinnt
    if (Feld1 == "-" and Feld2 == "-" and Feld3 == "-"):
        print("Der Computer hat Gewonnen, vieleicht nächstet mal...")
        Gewinner = "True"
    if (Feld4 == "-" and Feld5 == "-" and Feld6 == "-"):
        print("Der Computer hat Gewonnen, vieleicht nächstet mal...")
        Gewinner = "True"
    if (Feld6 == "-" and Feld7 == "-" and Feld9 == "-"):
        print("Der Computer hat Gewonnen, vieleicht nächstet mal...")
        Gewinner = "True"

    if (Feld1 == "-" and Feld4 == "-" and Feld7 == "-"):
        print("Der Computer hat Gewonnen, vieleicht nächstet mal...")
        Gewinner = "True"
    if (Feld2 == "-" and Feld5 == "-" and Feld7 == "-"):
        print("Der Computer hat Gewonnen, vieleicht nächstet mal...")
        Gewinner = "True"
    if (Feld3 == "-" and Feld6 == "-" and Feld9 == "-"):
        print("Der Computer hat Gewonnen, vieleicht nächstet mal...")
        Gewinner = "True"

    if (Feld1 == "-" and Feld5 == "-" and Feld9 == "-"):
        print("Der Computer hat Gewonnen, vieleicht nächstet mal...")
        Gewinner = "True"
    if (Feld3 == "-" and Feld5 == "-" and Feld6 == "-"):
        print("Der Computer hat Gewonnen, vieleicht nächstet mal...")
        Gewinner = "True"

    
    #Schaut ob Spieler gewinnt
    if (Feld1 == "+" and Feld2 == "+" and Feld3 == "+"):
        print("Du hast gewonnen, gut gemacht...")
        Gewinner = "True"
    if (Feld4 == "+" and Feld5 == "+" and Feld6 == "+"):
        print("Du hast gewonnen, gut gemacht...")
        Gewinner = "True"
    if (Feld6 == "+" and Feld7 == "+" and Feld9 == "+"):
        print("Du hast gewonnen, gut gemacht...")
        Gewinner = "True"
        
    if (Feld1 == "+" and Feld4 == "+" and Feld7 == "+"):
        print("Du hast gewonnen, gut gemacht...")
        Gewinner = "True"
    if (Feld2 == "+" and Feld5 == "+" and Feld7 == "+"):
        print("Du hast gewonnen, gut gemacht...")
        Gewinner = "True"
    if (Feld3 == "+" and Feld6 == "+" and Feld9 == "+"):
        print("Du hast gewonnen, gut gemacht...")
        Gewinner = "True"

    if (Feld1 == "+" and Feld5 == "+" and Feld9 == "+"):
        print("Du hast gewonnen, gut gemacht...")
        Gewinner = "True"
    if (Feld3 == "+" and Feld5 == "+" and Feld6 == "+"):
        print("Du hast gewonnen, gut gemacht...")
        Gewinner = "True"
