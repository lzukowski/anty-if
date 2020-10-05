import unittest

from gilded_rose import GildedRose, Item


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
    ENHANCE_BY = 1

    def setUp(self) -> None:
        self.item = Item("Aged Brie", sell_in=2, quality=0)
        self.gilded_rose = GildedRose([self.item])

    def test_increase_quality_when_day_passes(self):
        yesterday_quality = self.item.quality
        self.gilded_rose.update_quality()
        self.assertEqual(self.item.quality, yesterday_quality + self.ENHANCE_BY)

    def test_increase_twice_as_fast_when_sell_by_passes(self):
        self.item.sell_in = 0
        quality_after_sell_deadline = self.item.quality

        self.gilded_rose.update_quality()
        self.assertEqual(
            self.item.quality,
            quality_after_sell_deadline + (self.ENHANCE_BY * 2)
        )

    def test_quality_never_more_than_50_even_after_sell_in(self):
        self.item.sell_in = -1

        self.item.quality = 48
        self.gilded_rose.update_quality()
        self.assertEqual(self.item.quality, 50)

        self.item.quality = 49
        self.gilded_rose.update_quality()
        self.assertEqual(self.item.quality, 50)

    def test_quality_never_more_than_50(self):
        max_quality = 50
        self.item.quality = max_quality - 1

        self.gilded_rose.update_quality()
        self.assertEqual(self.item.quality, max_quality)

        self.gilded_rose.update_quality()
        self.assertEqual(self.item.quality, max_quality)

        self.gilded_rose.update_quality()
        self.assertEqual(self.item.quality, max_quality)


class BackstagePassesTest(unittest.TestCase):
    def setUp(self) -> None:
        self.item = Item(
            'Backstage passes to a TAFKAL80ETC concert',
            sell_in=15,
            quality=20,
        )
        self.gilded_rose = GildedRose([self.item])

    def test_increase_quality_when_day_passes(self):
        yesterday_quality = self.item.quality
        self.gilded_rose.update_quality()
        self.assertEqual(self.item.quality, yesterday_quality + 1)

    def test_quality_increases_by_2_when_10_days_left_to_sell(self):
        self.item.sell_in = 10
        yesterday_quality = self.item.quality

        self.gilded_rose.update_quality()
        self.assertEqual(self.item.quality, yesterday_quality + 2)

    def test_quality_increases_by_3_when_5_days_left_to_sell(self):
        self.item.sell_in = 5
        yesterday_quality = self.item.quality

        self.gilded_rose.update_quality()
        self.assertEqual(self.item.quality, yesterday_quality + 3)

    def test_quality_drops_to_0_when_day_after_sell_in_passes(self):
        self.item.sell_in = 0
        self.gilded_rose.update_quality()
        self.assertEqual(self.item.quality, 0)


class SulfurasTest(unittest.TestCase):
    def setUp(self) -> None:
        self.item = Item('Sulfuras, Hand of Ragnaros', sell_in=2, quality=80)
        self.gilded_rose = GildedRose([self.item])

    def test_never_sold_out_or_decreases_quality(self):
        sell_in = self.item.sell_in
        quality = self.item.quality

        self.gilded_rose.update_quality()
        self.assertEqual(self.item.sell_in, sell_in)
        self.assertEqual(self.item.quality, quality)

        self.gilded_rose.update_quality()
        self.assertEqual(self.item.sell_in, sell_in)
        self.assertEqual(self.item.quality, quality)

        self.gilded_rose.update_quality()
        self.assertEqual(self.item.sell_in, sell_in)
        self.assertEqual(self.item.quality, quality)
