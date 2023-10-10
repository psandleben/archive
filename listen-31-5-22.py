"""
einkaufs_liste = ["Milch", "Mehl", "Obst", "Nudeln"]

print(einkaufs_liste)

# am Ende der Liste die Zahl 199 hinzufügen
einkaufs_liste.append("Eier")

print(einkaufs_liste)

# das element Mehl aus der Liste entfernen
einkaufs_liste.remove("Mehl")

print(einkaufs_liste)

print(einkaufs_liste[2])

"""
# erstelle eine neue leere liste namens liste_1

liste_1 = []

# füge 5 neue Elemente der Liste  liste_1 hinzu

liste_1.append("Imac")
liste_1.append("Iphone_14_Pro_Plus")
liste_1.append("Mac_Pro")
liste_1.append("Airpods_Pro_2")
liste_1.append("Ipad_Pro_12.9_M2")

# das zweite Elemente der Liste liste_ ausdrucken

print(liste_1[1])

# das vierte element der Liste liste_1 ausdrucken
print(liste_1[3])

# das vierte element der Liste liste_1 den Wert 550 zuweisen

liste_1[3] = 550

print(liste_1)

# die liste liste_1 überschreiben mit einer neuen liste, welche 5 float Werte enthält

liste_1 = [1.4]
print(liste_1)

# die länge einer liste
len(liste_1)
# ein Algorithmus schreiben welcher ermittelt was da kleinte Element in 
# der Liste liste_1 ist und danach sollst du das kleinste Element ausdrucken

parabel = [] 

def kleinste_zahl_einer_liste(liste_1):
    zähler = len(liste_1) -1

    if zähler == -1:
        print(" in der Liste" + liste_1 + "sind keine Zahlen vorhanden")
    else:
        speicher = zähler
        ergebnis = liste_1[zähler]
        while zähler != -1:
            if liste_1[speicher] > liste_1[zähler]:
                ergebnis = liste_1[zähler]
                speicher = zähler
            zähler -= 1

        print(ergebnis) 

kleinste_zahl_einer_liste(parabel)