from gilded_rose import Item, GildedRose

class TestGildedRose:
    def test_items_have_name_property(self):
        items = [Item("potion bottle", sell_in=0, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert "potion bottle" == items[0].name

    def test_update_decrements_normal_sell_in(self):
        original_item = Item("potion bottle", sell_in=5, quality=10)
        updated_item = Item("potion bottle", sell_in=4, quality=9)
        items = [original_item]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        assert items[0].sell_in == updated_item.sell_in
    
    def test_update_decrements_normal_quality(self):
        original_item = Item("potion bottle", sell_in=5, quality=10)
        updated_item = Item("potion bottle", sell_in=4, quality=9)
        items = [original_item]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        assert items[0].quality == updated_item.quality

        
    def test_item_quality_cannot_be_below_0(self):
        original_item = Item("potion bottle", sell_in=5, quality=0)
        updated_item = Item("potion bottle", sell_in=4, quality=0)
        items = [original_item]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        assert items[0].quality == updated_item.quality
    
    def test_normal_item_quality_decrements_faster_after_sell_in(self):
        original_item = Item("potion bottle", sell_in=0, quality=5)
        updated_item = Item("potion bottle", sell_in=-1, quality=0)
        items = [original_item]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        assert items[0].quality == updated_item.quality
