# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GeneralItemTest(unittest.TestCase):
    DEGRADE_BY = 1

    def setUp(self) -> None:
        self.item = Item("foo", sell_in=10, quality=20)
        self.gilded_rose = GildedRose([self.item])

    def test_degrades_quality_when_day_passes(self):
        yesterday_quality = self.item.quality
        self.gilded_rose.update_quality()
        self.assertEqual(self.item.quality, yesterday_quality - self.DEGRADE_BY)

    def test_degrades_twice_as_fast_when_sell_by_passes(self):
        self.item.sell_in = 0
        quality_after_sell_deadline = self.item.quality

        self.gilded_rose.update_quality()
        self.assertEqual(
            self.item.quality,
            quality_after_sell_deadline - (self.DEGRADE_BY * 2)
        )

    def test_quality_never_negative(self):
        self.item.quality = 1

        self.gilded_rose.update_quality()
        self.assertEqual(self.item.quality, 0)

        self.gilded_rose.update_quality()
        self.assertEqual(self.item.quality, 0)

        self.gilded_rose.update_quality()
        self.assertEqual(self.item.quality, 0)


class AgedBrieTest(unittest.TestCase):
    def setUp(self) -> None:
        self.item = Item("Aged Brie", sell_in=-1, quality=50)
        self.gilded_rose = GildedRose([self.item])

    def test_aged_brie_quality_hit_max(self):
        self.gilded_rose.update_quality()
        self.assertEqual(self.item.quality, 50)
