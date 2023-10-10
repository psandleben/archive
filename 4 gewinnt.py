#die dimensionen von 4 gewinnt sind 6*7 
#senkrechtgewinnt : check
#Listen
gameboard = [["0", "0", "0", "0", "0", "0", "0"] for i in range(6)]

#Variablen
victory = False
weiter1 = False
weiter2 = False
weiter3 = False
reihe = 0
spalte = 0

#Funktionen

def game_board():
	print("|", gameboard[5][0], "|", gameboard[5][1], "|", gameboard[5][2], "|", gameboard[5][3], "|", gameboard[5][4], "|", gameboard[5][5], "|", gameboard[5][6], "|" )
	print()
	print("|", gameboard[4][0], "|", gameboard[4][1], "|", gameboard[4][2], "|", gameboard[4][3], "|", gameboard[4][4], "|", gameboard[4][5], "|", gameboard[4][6], "|" )
	print()
	print("|", gameboard[3][0], "|", gameboard[3][1], "|", gameboard[3][2], "|", gameboard[3][3], "|", gameboard[3][4], "|", gameboard[3][5], "|", gameboard[3][6], "|" )
	print()
	print("|", gameboard[2][0], "|", gameboard[2][1], "|", gameboard[2][2], "|", gameboard[2][3], "|", gameboard[2][4], "|", gameboard[2][5], "|", gameboard[2][6], "|" )
	print()
	print("|", gameboard[1][0], "|", gameboard[1][1], "|", gameboard[1][2], "|", gameboard[1][3], "|", gameboard[1][4], "|", gameboard[1][5], "|", gameboard[1][6], "|" )
	print()
	print("|", gameboard[0][0], "|", gameboard[0][1], "|", gameboard[0][2], "|", gameboard[0][3], "|", gameboard[0][4], "|", gameboard[0][5], "|", gameboard[0][6], "|" )
#0 ist ganz unten, 5 ist ganz oben

def gewinner_senkrecht(spieler : str, victory : bool):
	if spieler == "+":
		name = "Spieler1"
	else: name = "Spieler2"
	reihe = 0
	spalte = 0
	while spalte != 3 or reihe != 6:
		if spalte == 3: 
			spalte = 0
			reihe += 1
		if gameboard[spalte][reihe] == spieler and gameboard[spalte+1][reihe] == spieler and gameboard[spalte+2][reihe] == spieler and gameboard[spalte+3][reihe] == spieler:
			print(str(name) +" hat gewonnen.")
			victory = True
			return victory
		else: 
			spalte +=1 
	return victory

def gewinner_waagerecht(spieler : str, victory : bool):
	if spieler == "+":
		name = "Spieler1"
	else: name = "Spieler2"
	reihe2 = 0 
	spalte2 = 0
	while spalte2 != 5 or reihe2 != 3:
		if reihe2 == 3:
			reihe2 = 0
			spalte2 += 1
		if gameboard[spalte2][reihe2] == spieler and gameboard[spalte2][reihe2+1] == spieler and gameboard[spalte2][reihe2+2] == spieler and gameboard[spalte2][reihe2+3] == spieler:
			print(str(name) +" hat gewonnen.")
			victory = True
			break
		else: reihe2 += 1 
	return victory

def gewinner_schraek_rechts_links(spieler : str, victory : bool):
	if spieler == "+":
		name = "Spieler1"
	else: name = "Spieler2"
	reihe = 0 
	spalte = 0
	while not(spalte >= 3):
		if reihe == 4: 
			reihe = 0
			spalte += 1
			print("pass2")
		if gameboard[spalte][reihe] == spieler and gameboard[spalte+1][reihe+1] == spieler and gameboard[spalte+2][reihe+2] == spieler and gameboard[spalte+3][reihe+3] == spieler:
			print(str(name) +" hat gewonnen.")
			victory = True
			break
		else: 
			reihe += 1
			print("pass1")
	return victory

def gewinner_schraek_links_rechts(spieler : str, victory : bool):
	if spieler == "+":
		name = "Spieler1"
	else: name = "Spieler2"
	reihe = 6 
	spalte = 0
	while not(spalte >= 3):
		if reihe == 2: 
			reihe = 6
			spalte += 1
			print("pass2")
		if gameboard[spalte][reihe] == spieler and gameboard[spalte+1][reihe-1] == spieler and gameboard[spalte+2][reihe-2] == spieler and gameboard[spalte+3][reihe-3] == spieler:
			print(str(name) +" hat gewonnen.")
			victory = True
			break
		else: 
			reihe -= 1
			print("pass1")
	return victory

# Spiel
while victory != True:
	#Spieler1
	game_board()
	weiter2 = False
	spalte = int(input("Wo möchte Spieler1 setzen? ")) -1
	if not (spalte >= 0 and spalte <= 6):
		while weiter2 != True:
			spalte = int(input("Diese Zahl gibt es nicht. Wähle eine Zahl zwischen 1-7. ")) -1
			if spalte >= 0 and spalte <= 6:
				weiter2 = True
	
	while weiter3 != True:
		if gameboard[reihe][spalte] == "0":
			gameboard[reihe][spalte] = "+"
			weiter3 = True
			reihe = 0
		else:
			reihe += 1
	weiter3 = False  

	#Nach Gewinner Suchen:
	#victory = gewinner_waagerecht("+", victory)
	#victory = gewinner_senkrecht("+", victory)
	#victory = gewinner_schraek_rechts_links("+", victory)
	victory = gewinner_schraek_links_rechts("+", victory)
	if victory == True:
		game_board()
		break
	
	#Spieler2
	game_board()
	weiter2 = False
	spalte = int(input("Wo möchte Spieler2 setzen? ")) -1
	if not (spalte >= 0 and spalte <= 6):
		while weiter2 != True:
			spalte = int(input("Diese Zahl gibt es nicht. Wähle eine Zahl zwischen 1-7. ")) -1
			if spalte >= 0 and spalte <= 6:
				weiter2 = True

	while weiter3 != True:
		if gameboard[reihe][spalte] == "0":
			gameboard[reihe][spalte] = "-"
			weiter3 = True
			reihe = 0
		else:
			reihe += 1
	weiter3 = False
	# Nach Gewinner suchen:
	#victory = gewinner_waagerecht("-", victory)
	#1victory = gewinner_senkrecht("-", victory)
	#victory = gewinner_schraek_rechts_links("+", victory)
	if victory == True:
		game_board()
		break
