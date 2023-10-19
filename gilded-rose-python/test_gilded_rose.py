from gilded_rose import Item, GildedRose

class TestGildedRose:
    def test_update_decrements_normal_sell_in(self):
        original_sell_in = 5
        items = [Item("potion bottle", sell_in=original_sell_in, quality=5)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        assert items[0].sell_in == original_sell_in - 1
    
    def test_update_decrements_normal_item_quality(self):
        original_quality = 10
        items = [Item("potion bottle", sell_in=50, quality=original_quality)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        assert items[0].quality == original_quality - 1

        
    def test_item_quality_cannot_be_below_0(self):
        original_quality = 0
        items = [Item("potion bottle", sell_in=0, quality=original_quality)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        assert items[0].quality == original_quality
    
    def test_normal_item_quality_decrements_faster_after_sell_in(self):
        original_quality = 5
        items = [Item("potion bottle", sell_in=0, quality=original_quality)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        assert items[0].quality == original_quality - 2

    def test_aged_brie_quality_increases_over_time(self):
        original_quality = 5
        items = [Item("Aged Brie", sell_in=5, quality=original_quality)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        assert items[0].quality == original_quality + 1

    def test_quality_cannot_exeed_50(self):
        original_quality = 50
        items = [Item("Aged Brie", sell_in=5, quality=original_quality)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        assert items[0].quality == original_quality

    def test_sulfuras_quality_does_not_change(self):
        original_quality = 40
        original_item = Item("Sulfuras, Hand of Ragnaros", sell_in=1, quality=original_quality)
        items = [original_item]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        gilded_rose.update_quality()

        assert items[0].quality == original_quality
