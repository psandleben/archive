import pandas as pd

df = pd.read_csv('financial_data_sp500_companies.csv') # sp Standard & Poor

"""
Unternehmensbewertung: es existieren viele verschiedene wichtige Unternehmenseigenshaften:
- Einkommen / Gewinn
- Vermögenswerte
- Verbindlichkeiten
- Umsatz
- Geschichte / Vergangenheit
- Zukunft
- Markt Merkmale
- usw.
"""

def FullNetIncome(financial_data: list) -> float:
    
    i = 0

    Firm = financial_data['firm'].tolist()
    Net_Income = financial_data['Net Income'].tolist()
    #print(Firm)
    #for i in range(10):
        #print("--------------------------------------------------------------------------------------------------------------------------------")
    #print(Net_Income)

    while Firm[i] != "Activision Blizzard":
        i += 1

    Full_Net_Income = Net_Income[i] + Net_Income[i+1] + Net_Income[i+2] + Net_Income[i+3]
    print(Full_Net_Income)
 
    return Full_Net_Income

Full_Net_Income = FullNetIncome(df)

# eine neue Funktion definieren: die Funktion soll eine Unternehmensbewertung zurückgeben (also ein Float)
def unternehmen_bewerten(einkommen: float) -> float:
    # Inhalt angeben
    unternehmenswert: float
    # Beispiel: 20 mal "Net Income für ein Jahr"

    


    return unternehmenswert


# Ziel #1: welches Unternehmen sollte man kaufen (laut deiner Bewertung)?



# Ziel #2: welches Unternehmen sollte man "shorten" (laut deiner Bewertung)?

print(str(329000000 + 335000000 + 353000000 + 348000000))