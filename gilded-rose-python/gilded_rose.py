# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self): 
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                break
            if item.name == "Aged Brie":
                self.increment_quality(item)
                self.decrement_sell_in(item)
                break
            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.sell_in <= 0:
                    item.quality = 0
                    self.decrement_sell_in(item)
                    break
                elif item.sell_in <= 5:
                    self.increment_quality(item, 3)
                    self.decrement_sell_in(item)
                    break
                elif item.sell_in <= 10:
                    self.increment_quality(item, 2)
                    self.decrement_sell_in(item)
                    break
                else:
                    self.increment_quality(item)
                    self.decrement_sell_in(item) 
                    break

            self.decrement_quality(item)
            self.decrement_sell_in(item)

    def increment_quality(self, item, amount = 1):
        if item.quality < 50:
            item.quality += amount

    def decrement_quality(self, item):
        if item.quality > 0:
            item.quality -= 1
            if item.sell_in <= 0:
               item.quality -= 1

    def decrement_sell_in(self, item):
        item.sell_in -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
