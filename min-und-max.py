import random

#Erstelle eine Liste liste1 mit 12 zufälligen float Werten zwischen 0 und 50

liste1 = [random.randint(0, 50) for i in range(12)]

print(liste1)

# Erstelle eine Funktion die den maximal Wert der Liste liste1 ausdruckt

def größte_zahl_einer_liste(liste):
    zähler = len(liste) -1

    speicher = zähler
    ergebnis = liste[zähler]
    while zähler != -1:
        if liste[speicher] < liste[zähler]:
            ergebnis = liste[zähler]
            speicher = zähler
        zähler -= 1

    print(ergebnis)

größte_zahl_einer_liste(liste1)

# Erstelle eine Fuktion die den minimalen Wert der Liste ausdruckt

def kleinste_zahl_einer_liste(liste):
    zähler = len(liste) -1

    speicher = zähler
    ergebnis = liste[zähler]
    while zähler != -1:
        if liste[speicher] > liste[zähler]:
            ergebnis = liste[zähler]
            speicher = zähler
        zähler -= 1

    print(ergebnis)

kleinste_zahl_einer_liste(liste1) 

# Sortiere die Liste liste1 aufsteigend
"""
liste2 = []

while liste1 != []:
    zähler = len(liste1) -1
    speicher = zähler
    while zähler != -1:
        if liste1[speicher] >= liste1[zähler]:
            speicher = zähler
        zähler -= 1
    liste2.append(liste1[speicher])
    liste1.remove(liste1[speicher])

print(liste2)

# absteigend

liste3 = []

while liste2 != []:
    zähler = len(liste2) -1
    speicher = zähler
    while zähler != -1:
        if liste2[speicher] <= liste2[zähler]:
            speicher = zähler
        zähler -= 1
    liste3.append(liste2[speicher])
    liste2.remove(liste2[speicher])

print(liste3)
"""
# Sortiere die Liste aufsteigend ohne 2. Liste

liste2 = []
continue1 = -1

while continue1 != len(liste1) -1:
    zähler = len(liste1) + continue1
    speicher = zähler
    print()
    while zähler != -1:
        if liste1[speicher] >= liste1[zähler]:
            speicher = zähler
        zähler -= 1
    liste1.insert(0, liste1[speicher])
    liste1.pop(speicher +1)
    print(liste1)
    continue1 += 1

print(liste1)

