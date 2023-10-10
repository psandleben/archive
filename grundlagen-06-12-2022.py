# Erstelle eine Variable produkt_preis (mit einen Type-Hint) und weise ihr den Wert 20.99 zu
'''
produkt_preis                 : float = 20.99

# Eine Bedingung schreiben so dass wenn produkt_preis größer 30.50 ist "Happy Holidays" ausgedruckt wird.

if produkt_preis > 30.50:
    print("Happy Holidays")

# eine leere Liste (mit type-Hint) names zoo erstellen

zoo: list = []

# Zu der Liste zoo ein Element (ein String), mit dem Namen von einem Tier, hinzufügen.

zoo.append("Mensch")

# Zu der Liste zoo zwei weiter Elemente(Tier) hizufügen

zoo.append("Blobfisch")
zoo.append("Elefant")

# Ein Element aus der Liste zoo entfernen

zoo.remove("Elefant")

# Erstelle eine Fuktion print_1000_helloworlds die 1000 mal "Hello World" ausdruckt

def print_1000_helloworlds():
    weiter = 0
    while weiter != 1000:
        print("Hello World")
        weiter += 1

# Die Fuktion print_1000_helloworlds ausführen

print_1000_helloworlds()

# Erstelle eine Funktion namens print_1000_zahlen, die die Zahlen 6 1006 ausdrucken

def print_1000_zahlen():
    weiter2 = 6
    while weiter2 != 1007:
        print(weiter2)
        weiter2 += 1

# Die Funktion namens print_1000_zahlen ausführen

print_1000_zahlen()
'''

# Erstelle eine Fuktion namens wahrscheinlichkeit die die Wahrscheinlichkeit ausrechnet, dass man bei einem nomalen 6-seitigen würfel 10 mal nacheinander 6 würfelt
'''

def wahrscheinlichkeit():
    weiter = 0
    ergebnis = 1/6
    while weiter != 9:
        ergebnis *= 1/6
        weiter += 1
    print(ergebnis)

# Die Fuktion wahrscheinlichkeit ausführen

wahrscheinlichkeit() 
'''

# Erstelle eine Fuktion namens wahrscheinlichkeit die die Wahrscheinlichkeit ausrechnet, dass man bei einem nomalen 6-seitigen würfel n mal nacheinander 6 würfelt; n wird in der Funktion als Eingabeparameter übergeben

'''
def wahrscheinlichkeit(n):
    n -= 1
    ergebnis = 1/6
    weiter = 0
    while weiter < n:
        ergebnis *= 1/6
        weiter += 1
    print(ergebnis)

wahrscheinlichkeit(10)
'''

# Erstelle eine Fuktion namens fibonacci_zahlen die die ersetn 20 fibonacci Zahlen als Liste abspeichern und ausdruckt

def fibonacci_zahlen():
    summe = 1
    summe2 = 1
    liste = [0, 1]
    for i in range(0, 21):
        liste.append(summe)
        summe = summe2
        summe2 = summe 
    print(liste)

fibonacci_zahlen()