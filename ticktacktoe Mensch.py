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
Spieler1 = "None"
Gewinner = "None"
Spieler2 = "None"
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
    weiter3 = "None"
    #spieler1 wählt
    while weiter2 == "None":
        Spieler = input("Wo möchten sie(Spieler1) setzen(1, 2, ..., 9)? ")
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
        time.sleep(0.5) 
    spielbrett()
    #Schaut ob Spieler 1 Gewinnt
    if (Feld1 == "+" and Feld2 == "+" and Feld3 == "+"):
        print("Spieler1 hat Gewonnen")
        Gewinner = "True"
    if (Feld4 == "+" and Feld5 == "+" and Feld6 == "+"):
        print("Spieler1 hat Gewonnen")
        Gewinner = "True"
    if (Feld6 == "+" and Feld7 == "+" and Feld9 == "+"):
        print("Spieler1 hat Gewonnen")
        Gewinner = "True"
            
    if (Feld1 == "+" and Feld4 == "+" and Feld7 == "+"):
        print("Spieler1 hat Gewonnen")
        Gewinner = "True"
    if (Feld2 == "+" and Feld5 == "+" and Feld8 == "+"):
        print("Spieler1 hat Gewonnen")
        Gewinner = "True"
    if (Feld3 == "+" and Feld6 == "+" and Feld9 == "+"):
        print("Spieler1 hat Gewonnen")
        Gewinner = "True"

    if (Feld1 == "+" and Feld5 == "+" and Feld9 == "+"):
        print("Spieler1 hat Gewonnen")
        Gewinner = "True"
    if (Feld3 == "+" and Feld5 == "+" and Feld6 == "+"):
        print("Spieler1 hat Gewonnen")
        Gewinner = "True"
            
        #Person2 wählt
    while weiter3 == "None" and Gewinner == "None":
        Spieler2 = input("Wo möchten sie(Spieler1) setzen(1, 2, ..., 9)? ")
        if Spieler2 == "1" and Feld1 == " ":
            Feld1 = "-"
            weiter3 = "ja"
        elif Spieler2 == "2" and Feld2 == " ":
            Feld2 = "-"
            weiter3 = "ja"
        elif Spieler2 == "3" and Feld3 == " ":
            Feld3 = "-"
            weiter3 = "ja"
        elif Spieler2 == "4" and Feld4 == " ":
            Feld4 = "-"
            weiter3 = "ja"
        elif Spieler2 == "5" and Feld5 == " ":
            Feld5 = "-"
            weiter3 = "ja"
        elif Spieler2 == "6" and Feld6 == " ":
            Feld6 = "-"
            weiter3 = "ja"
        elif Spieler2 == "7" and Feld7 == " ":
            Feld7 = "-"
            weiter3 = "ja"
        elif Spieler2 == "8" and Feld8 == " ":
            Feld8 = "-"
            weiter3 = "ja"
        elif Spieler2 == "9" and Feld9 == " ":
            Feld9 = "-" 
            weiter3 = "ja"
        else:
            print("Dieses Feld ist bereits vergeben")
        spielbrett()
    #Schaut ob Spieler2 gewinnt
    if (Feld1 == "-" and Feld2 == "-" and Feld3 == "-"):
        print("Spieler2 hat Gewonnen")
        Gewinner = "True"
    if (Feld4 == "-" and Feld5 == "-" and Feld6 == "-"):
        print("Spieler2 hat Gewonnen")
        Gewinner = "True"
    if (Feld6 == "-" and Feld7 == "-" and Feld9 == "-"):
        print("Spieler2 hat Gewonnen")
        Gewinner = "True"

    if (Feld1 == "-" and Feld4 == "-" and Feld7 == "-"):
        print("Spieler2 hat Gewonnen")
        Gewinner = "True"
    if (Feld2 == "-" and Feld5 == "-" and Feld8 == "-"):
        print("Spieler2 hat Gewonnen")
        Gewinner = "True"
    if (Feld3 == "-" and Feld6 == "-" and Feld9 == "-"):
        print("Spieler2 hat Gewonnen")
        Gewinner = "True"

    if (Feld1 == "-" and Feld5 == "-" and Feld9 == "-"):
        print("Spieler2 hat Gewonnen")
        Gewinner = "True"
    if (Feld3 == "-" and Feld5 == "-" and Feld6 == "-"):
        print("Spieler2 hat Gewonnen")
        Gewinner = "True"