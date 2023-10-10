spielbrett = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
def PRINT():
    print(spielbrett[0])
    print(spielbrett[1])
    print(spielbrett[2])
    print("")

#oben links
spielbrett[0][0] = "+"
PRINT()

# unten rechts
spielbrett[2][2] = "-"
PRINT()


# mitte mitte
spielbrett[1][1] = "+"
PRINT()

# oben rechts
spielbrett[0][2] = "-"
PRINT()

# unten links
spielbrett[2][0] = "+" 
PRINT()

# mitte rechts
spielbrett[1][2] = "-"
PRINT()

# mitte links
spielbrett[1][0] = "+"
PRINT()
