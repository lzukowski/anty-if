import unittest

from gilded_rose import GildedRose, Item


class GildedRoseTest(unittest.TestCase):
    def test_generic(self):
        self.assert_generic_quality(expected=0, sell_in=0, quality=0)
        self.assert_generic_quality(expected=-1, sell_in=0, quality=-1)
        self.assert_generic_quality(expected=1, sell_in=-1, quality=3)
        self.assert_generic_quality(expected=1, sell_in=0, quality=3)
        self.assert_generic_quality(expected=0, sell_in=0, quality=1)
        self.assert_generic_quality(expected=9, sell_in=1, quality=10)

    def assert_generic_quality(self, expected, sell_in, quality):
        item = Item("foo", sell_in=sell_in, quality=quality)
        GildedRose([item]).update_quality()
        self.assertEqual(expected, item.quality)

    def test_conjured(self):
        self.assert_conjured_quality(expected=0, sell_in=0, quality=0)
        self.assert_conjured_quality(expected=-1, sell_in=0, quality=-1)
        self.assert_conjured_quality(expected=0, sell_in=-1, quality=3)
        self.assert_conjured_quality(expected=0, sell_in=0, quality=3)
        self.assert_conjured_quality(expected=0, sell_in=0, quality=1)
        self.assert_conjured_quality(expected=8, sell_in=1, quality=10)

    def assert_conjured_quality(self, expected, sell_in, quality):
        item = Item("Conjured Mana Cake", sell_in=sell_in, quality=quality)
        GildedRose([item]).update_quality()
        self.assertEqual(expected, item.quality)

    def test_backstage_pass(self):
        self.assert_backstage_pass_quality(expected=22, sell_in=8, quality=20)
        self.assert_backstage_pass_quality(expected=23, sell_in=4, quality=20)
        self.assert_backstage_pass_quality(expected=0, sell_in=0, quality=20)
        self.assert_backstage_pass_quality(expected=23, sell_in=1, quality=20)
        self.assert_backstage_pass_quality(expected=22, sell_in=6, quality=20)
        self.assert_backstage_pass_quality(expected=23, sell_in=5, quality=20)
        self.assert_backstage_pass_quality(expected=22, sell_in=10, quality=20)
        self.assert_backstage_pass_quality(expected=21, sell_in=11, quality=20)
        self.assert_backstage_pass_quality(expected=51, sell_in=11, quality=51)

    def assert_backstage_pass_quality(self, expected, sell_in, quality):
        item = Item(
            "Backstage passes to a TAFKAL80ETC concert",
            sell_in=sell_in, quality=quality,
        )
        GildedRose([item]).update_quality()
        self.assertEqual(expected, item.quality)

    def test_aged_brie(self):
        self.assert_aged_brie_quality(expected=22, sell_in=0, quality=20)
        self.assert_aged_brie_quality(expected=21, sell_in=1, quality=20)

    def assert_aged_brie_quality(self, expected, sell_in, quality):
        item = Item("Aged Brie", sell_in=sell_in, quality=quality)
        GildedRose([item]).update_quality()
        self.assertEqual(expected, item.quality)
