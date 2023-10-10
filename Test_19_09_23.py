import random
"""
Eine Klasse AmazonProdukt erstellen: die Klasse besitzt mindestesns 4 Attribute
(Type-Hints verwenden) und die __eq__ und __hash__ Methoden.
"""

produkt_id_set: set = set([])


class AmazonProduct:
    def __init__(self, name: str = "Untitled", price: float = 0.99, description: str = "", category: str = "No category"):
        
        finished: bool = False
        
        liste: list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "o", "p", "q", "r", "s", "t", "u", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        while finished != True:
            product_id: str = [random.choice(liste) for i in range(10)]
            if not(product_id in produkt_id_set):
                produkt_id_set.add(product_id)
                finished = True
        
        self.name = name
        self.price = price
        self.description = description
        self.category = category
        self.product_id = product_id

    
    def __eq__(self, other) -> bool:
        return self.product_id == other.product_id
    
    def __hash__(self) -> int:
        return hash((self.product_id)) 
    
    def __repr__(self) -> str:
        return f"{self.name}: \nprice: {self.price}, category: {self.category}, product_id: {self.product_id}, description: {self.description},"


product_1: AmazonProduct = AmazonProduct("FireTVStick 4K", 49.99, "Fire TV Stick 4K, for better Video quality and faster Performance", "Media Devices")
product_2: AmazonProduct = AmazonProduct("FireTVStick 2K", 29.99, "Fire TV Stick 2K, for good Video quality and nice Performance", "Media Devices")
    
print(product_1)

print()

print(product_2)