import random
import time

#Variablen

wiederholung = "ja"
punkte = 0
cpunkte = 0
cheat = False

# Fragt nach dem Namen.
name = input("Hallo was ist dein Name? ")
time.sleep(1)
print("Hallo " + str(name) + ", herzlich willkommen zu Schere Stein Papier")
time.sleep(1)

# Fragt ob er die Spielanleitung erklären soll
frage = input("Möchtest du die Spielanleitung wissen(Ja oder Nein)? ").lower()
if frage == "ja":
    print("Der Computer wählt entweder Schere, Stein oder Papier.") 
    print("Du musst dann  auch etwas wählen ohne das du das Ergebnis von Computer kennst.") 
    print("Der Gewinner wird ganz einfach entschieden : Stein schlägt Schere, Schere schlägt Papier und Papier schlägt Stein.")
    time.sleep(5)
if frage == "cheat":
    cheat = True
    print("cheat on")
    time.sleep(1)

while wiederholung == "ja":
    # Computer wählt
    computer = random.choice(["Schere", "Stein", "Papier", "Brunnen"])
    
    if cheat == True:
        print("hacking...")
        time.sleep(1)
        print("hacking...")
        time.sleep(1)
        print("hacking...")
        time.sleep(1)
        print("Das Symbol vom Computer ist " + str(computer))

    # Fragt Spieler
    spieler = input("Welchen, Gegenstand möchtest du Einsetzen(Schere, Stein oder Papier)? ").strip().title()


    # Auswertung

    if spieler != "Schere" and spieler != "Stein" and spieler != "Papier" and spieler != "Brunnen":
        print("Diesen Gegenstand gibt es nicht.")

    if computer == spieler:
        print("Computer hat " + str(computer) + " gewählt: Unentschieden. ")
        print("Du hast " + str(punkte) + " Punkte.")
    
    if computer == "Stein" and spieler == "Papier":
        print("Computer wählt Stein: Gewonnen")
        punkte = punkte + 1
        print("Du hast " + str(punkte) + " Punkte.")
        
    if computer == "Stein" and spieler == "Schere":
        print("Computer wählt Stein: Verloren")
        cpunkte = cpunkte + 1
        print("Du hast " + str(punkte) + " Punkte.")
        
    if computer == "Papier" and  spieler == "Schere":
        print("Computer wählt Papier: Gewonnen")
        punkte = punkte + 1
        print("Du hast " + str(punkte) + " Punkte.")
       
    if computer == "Papier" and spieler == "Stein":
        print("Computer wählt Papier: Verloren")
        cpunkte = cpunkte + 1
        print("Du hast " + str(punkte) + " Punkte.")
        
    if computer == "Schere" and  spieler == "Stein":
        print("Computer wählt Schere: Gewonnen")
        punkte = punkte + 1
        print("Du hast " + str(punkte) + " Punkte.")
        
    if computer == "Schere" and spieler == "Papier":
        print("Computer wählt Schere: Verloren")
        cpunkte = cpunkte +1
        print("Du hast " + str(punkte) + " Punkte.")

    if computer == "Brunnen" and spieler == "Papier":
        print("Computer wählt Brunnen: Gewonnen")
        punkte = punkte + 1
        print("Du hast " + str(punkte) + " Punkte.")

    if computer == "Brunnen" and (spieler == "Schere" or spieler == "Stein"):
        print("Computer wählt Brunnen: Verloren")
        cpunkte = cpunkte + 1
        print("Du hast " + str(punkte) + " Punkte.")

    if (computer == "Schere" or computer ==  "Stein") and spieler == "Brunnen":
        print("Computer wählt" + str(computer) + ": Gewonnen")
        punkte = punkte + 1
        print("Du hast " + str(punkte) + "Punkte.")

    if computer == "Papier" and  spieler == "Brunnen":
        print("Computer wählt Papier: Verloren")
        cpunkte = cpunkte + 1
        print("Du hast " + str(punkte) + " Punkte.")

    if cpunkte == 3:
        wiederholung = "Nein"
        print("Der Computer hat Gewonnen. Viel Glück das nächste mal, " + str(name))

        if punkte == 3:
            wiederholung = "Nein"
            print("Du hast Gewonnen. Viel Glück das nächste mal, " + str(name))