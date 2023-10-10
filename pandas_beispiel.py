import pandas as pd

i = 0

# df: dataframe 
# csv: comma separated values
df = pd.read_csv('financial_data_sp500_companies.csv') # sp Standard & Poors

# die ersten Zeilen der Datei ausdrucken
#print(df.head())

# Spalte einlesen als Liste
common_shares_liste = df['Net Income Applicable To Common Shares'].tolist()
#print(f"{common_shares_liste=}") # f"" ist ein formatierter String
#print(f"{common_shares_liste[0]=}")


Firm = df['firm'].tolist()
Net_Income = df['Net Income'].tolist()
print(Firm)
for i in range(10):
    print("--------------------------------------------------------------------------------------------------------------------------------")
print(Net_Income)

while Firm[i] != "Activision Blizzard":
    i += 1

Full_Net_Income = Net_Income[i] + Net_Income[i+1] + Net_Income[i+2] + Net_Income[i+3]

print(Full_Net_Income)
