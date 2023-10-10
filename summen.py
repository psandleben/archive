#Die Summe aller Zahlen zwischen 1 und 100 in einer Variable summe1 abspeichern
"""
weiter1 = False
zähler1 = 0
summe1 = 0

while weiter1 != True:
    if zähler1 == 100:
        weiter1 = True
    else:
        zähler = zähler + 1
        summe1 = summe1 + zähler
print(summe1)
"""
#Die Summe aller geraden Zahlen zwischen 0 10400 in einer Variable summe2 abspeichern
"""
weiter2 = False
zähler2 = 0
summe2 = 0

while weiter2 != True:
    if zähler2 == 10400:
        weiter2 = True
    else:
        zähler2 += 2
        summe2 = summe2 + zähler2
print(summe2)
"""

# eine Zufallszahl zwischen 2 und 39 ausdrucken
"""
import random

summe3 = 0

summe3 = random.randint(2, 39)
print(summe3)
"""

# 10 Zufallszahlen zwischen 0 und 870 ausdrucken
"""
import random

zähler4 = 0
weiter4 = False

while weiter4 != True:
    if zähler4 == 9:
        weiter4 = True
    else:
        zähler4 += 1
    print(random.randint(0, 870))
"""

#Berechne die Summe von 100 Zufallszahlen zwischen 0 und 1
"""
import random

summe5 = 0
zähler5 = 0
weiter5 = False

while weiter5 != True:
    if zähler5 == 100:
        weiter5 = True
    else:
        zähler5 += 1
    summe5 += random.randint(0, 1)
print(summe5)
"""
#Berechne die Summe aller zweierpotenzen von 4 bis 8192; diesen Wert sollen sie der Variable summe6 zuweisen
"""
test =  4
summe6 = 0

while test <= 8192:
    summe6 += test
    test *= 2
print(summe6)
"""
# Berechne die Summe aller Zahlen zwischen -100 und 101 und speichere diesen Wert in der Variable Summe ab.
"""
zähler7 = -100
summe7 = 0

while zähler7 != 102:
    summe7 += zähler7
    zähler7 += 1
print(summe7)
"""
#Berechne die Summe aller Zahlen zwischen -1920 und 8890 und speichere diesen Wert in der Variable Summe ab.
"""
zaehler8 = -1920
summe8 = 0

while zaehler8 != 8891:
    summe8 += zaehler8
    zaehler8 += 1
print(summe8)

"""
# Berechne die Summe aller 5er Potenzen zwischen 1 und 625 und speichere diesen Wert in der Variable Summe ab.

"""
test9 =  1
summe9 = 0

while test9 <= 626:
    summe9 += test9
    test9 *= 5
print(summe9)
"""

# Multipliziere alle Zahlen zwischen 1 und 20 und speicher das Ergebnis in der Vaeiable x ab.
"""
i = 1
x = 1

while i < 21:
    x *= i
    i += 1
print(x)
"""
