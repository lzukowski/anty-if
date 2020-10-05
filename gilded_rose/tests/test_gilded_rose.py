import unittest

from gilded_rose import Item, GildedRose


class GeneralItemTest(unittest.TestCase):
    def setUp(self) -> None:
        self.item = Item("foo", sell_in=0, quality=0)
        self.gilded_rose = GildedRose([self.item])

    def test_foo(self):
        self.gilded_rose.update_quality()
        self.assertEqual("foo", self.item.name)


class AgedBrieTest(unittest.TestCase):
    def setUp(self) -> None:
        self.item = Item("Aged Brie", sell_in=-1, quality=50)
        self.gilded_rose = GildedRose([self.item])

    def test_aged_brie_quality_hit_max(self):
        self.gilded_rose.update_quality()
        self.assertEqual(self.item.quality, 50)
