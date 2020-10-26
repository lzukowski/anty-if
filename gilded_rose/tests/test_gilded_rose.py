import unittest

from gilded_rose import GildedRose, Item


class GildedRoseTest(unittest.TestCase):
    def test_generic(self):
        item = Item("foo", sell_in=0, quality=0)
        GildedRose([item]).update_quality()
        self.assertEqual("foo", item.name)

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
