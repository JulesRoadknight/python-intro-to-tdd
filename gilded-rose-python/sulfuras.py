from item import Item

class Sulfuras(Item):

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def update(self): 
        pass
