# Mit Eingabeparameter: Youan in Euro konvertieren
# allgemein zu Eingabeparameter:
# def name_funktion(eingabe_parameter_1, ....)


def euro_zu_yen():
    # Euro in Yen konvertieren mkit einer Eingabe durch die Konsole:
    euro = input("Euro: ")
    # um ein String in einen Float umzuwandeln verwendet man die fuktion float()
    euro = float(euro)
    yen = euro * 137.51
    print(str(yen))



def bitcoin_zu_euro():
    Euro = input("Euro:")
    Euro = float(Euro)
    Bitcoin = Euro * 0.000051
    print(str(Bitcoin))

bitcoin_zu_euro()
