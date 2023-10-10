# eine Funktion (globlále_func) erstellen die eine Funktionen definieren und zurückgibt

def global_func():

    def func_1(name: str = "No Name"):
        print("Hi,", name, "nice to meet you" )
        
    def func_2(name: str = "No Name"):
        print("Goodbye, ", name )

    return func_1, func_2

# global_func ausführen und den Rückgabewert in einer Variable f abspeichern

f = global_func()

print("global_func: ", str(f))

# die Variable f ausführen

f[0]("Philipp")
f[1]("Philipp")

# eine Funktion (global_func) erstellen die eine Klasse definiert und zurückgibt

def global_func_2():

    class Class_1:
        
        def __init__(self, name: str = "No Name"):
            self.name = name

    return Class_1

# global_func_2 ausführen und den Rückgabewert in einer Variable Klasse abspeichern

Klasse = global_func_2()

# Zwei Objekte der Klasse (der Variable Klasse) erstellen 

objekt_1 = Klasse("Philipp")

objekt_2 = Klasse("Christopher")