from item import Item

class AgedBrie(Item):

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def update(self): 
        self.update_quality()
        self.decrement_sell_in()

    def update_quality(self):
        if self.quality < 50:
            self.quality += 1

    def decrement_sell_in(self):
        self.sell_in -= 1
