from sulfuras import Sulfuras
from normal_item import NormalItem
from backstage_passes import BackstagePasses
from aged_brie import AgedBrie
from gilded_rose import GildedRose
from item import Item

class TestGildedRose:
    def test_update_decrements_normal_sell_in(self):
        original_sell_in = 0
        items = [NormalItem("potion bottle", sell_in=original_sell_in, quality=5)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert items[0].sell_in == original_sell_in - 1
    
    def test_update_decrements_normal_item_quality(self):
        original_sell_in = 10
        original_quality = 10
        items = [NormalItem("potion bottle", sell_in=original_sell_in, quality=original_quality)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert items[0].sell_in == original_sell_in - 1
        assert items[0].quality == original_quality - 1

        
    def test_item_quality_cannot_be_below_0(self):
        original_sell_in = 14
        original_quality = 0
        items = [NormalItem("potion bottle", sell_in=original_sell_in, quality=original_quality)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert items[0].sell_in == original_sell_in - 1
        assert items[0].quality == original_quality
    
    def test_normal_item_quality_decrements_faster_after_sell_in(self):
        original_sell_in = 0
        original_quality = 5
        items = [NormalItem("potion bottle", sell_in=original_sell_in, quality=original_quality)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert items[0].sell_in == original_sell_in - 1
        assert items[0].quality == original_quality - 2

    def test_aged_brie_quality_increases_over_time(self):
        original_sell_in = 5000
        original_quality = 5
        items = [AgedBrie("Aged Brie", sell_in=original_sell_in, quality=original_quality)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert items[0].sell_in == original_sell_in - 1
        assert items[0].quality == original_quality + 1

    def test_quality_cannot_exeed_50(self):
        original_sell_in = 42
        original_quality = 50
        items = [AgedBrie("Aged Brie", sell_in=original_sell_in, quality=original_quality)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert items[0].sell_in == original_sell_in - 1
        assert items[0].quality == original_quality

    def test_sulfuras_properties_do_not_change(self):
        original_sell_in = 0
        original_sell_in = 1
        original_quality = 40
        original_item = Sulfuras("Sulfuras, Hand of Ragnaros", sell_in=original_sell_in, quality=original_quality)
        items = [original_item]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()
        gilded_rose.update_quality()

        assert items[0].sell_in == original_sell_in
        assert items[0].quality == original_quality

    def test_concert_tickets_lose_all_quality_after_sell_in(self):
        original_sell_in = 0
        original_item = BackstagePasses("Backstage passes to a TAFKAL80ETC concert", sell_in=original_sell_in, quality=40)
        items = [original_item]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert items[0].sell_in == original_sell_in - 1
        assert items[0].quality == 0

    def test_concert_tickets_gain_quality_long_before_sell_in(self):
        original_sell_in = 11
        original_quality = 40
        original_item = BackstagePasses("Backstage passes to a TAFKAL80ETC concert", sell_in=original_sell_in, quality=original_quality)
        items = [original_item]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert items[0].sell_in == original_sell_in - 1
        assert items[0].quality == original_quality + 1

    def test_concert_tickets_gain_quality_10_days_before_sell_in(self):
        original_sell_in = 10
        original_quality = 10
        original_item = BackstagePasses("Backstage passes to a TAFKAL80ETC concert", sell_in=original_sell_in, quality=original_quality)
        items = [original_item]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        quality_gained = 2
        assert items[0].sell_in == original_sell_in - 1
        assert items[0].quality == original_quality + quality_gained

    def test_concert_tickets_gain_more_quality_5_days_before_sell_in(self):
        original_sell_in = 5
        original_quality = 10
        original_item = BackstagePasses("Backstage passes to a TAFKAL80ETC concert", sell_in=original_sell_in, quality=original_quality)
        items = [original_item]
        gilded_rose = GildedRose(items)

        quality_gained = 3
        gilded_rose.update_quality()

        assert items[0].sell_in == original_sell_in - 1
        assert items[0].quality == original_quality + quality_gained
