import unittest

from gilded_rose import GildedRose, Item


class AcceptanceTests(unittest.TestCase):
    EXPECTED_STATE_BY_DAYS = {
        0: [
            '+5 Dexterity Vest, 10, 20',
            'Aged Brie, 2, 0',
            'Elixir of the Mongoose, 5, 7',
            'Sulfuras, Hand of Ragnaros, 0, 80',
            'Sulfuras, Hand of Ragnaros, -1, 80',
            'Backstage passes to a TAFKAL80ETC concert, 15, 20',
            'Backstage passes to a TAFKAL80ETC concert, 10, 49',
            'Backstage passes to a TAFKAL80ETC concert, 5, 49',
        ],
        1: [
            '+5 Dexterity Vest, 9, 19',
            'Aged Brie, 1, 1',
            'Elixir of the Mongoose, 4, 6',
            'Sulfuras, Hand of Ragnaros, 0, 80',
            'Sulfuras, Hand of Ragnaros, -1, 80',
            'Backstage passes to a TAFKAL80ETC concert, 14, 21',
            'Backstage passes to a TAFKAL80ETC concert, 9, 50',
            'Backstage passes to a TAFKAL80ETC concert, 4, 50',
        ],
    }

    def setUp(self) -> None:
        self.items = [
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(
                name="Backstage passes to a TAFKAL80ETC concert",
                sell_in=15,
                quality=20
            ),
            Item(
                name="Backstage passes to a TAFKAL80ETC concert",
                sell_in=10,
                quality=49,
            ),
            Item(
                name="Backstage passes to a TAFKAL80ETC concert",
                sell_in=5,
                quality=49,
            ),
        ]
        self.gilded_rose = GildedRose(self.items)

    def test_verify_results_by_days(self):
        for day in range(2):
            day_results = self.EXPECTED_STATE_BY_DAYS[day]
            for i, item in enumerate(self.items):
                expected = day_results[i]
                with self.subTest(day=day, item=item, expected=expected):
                    self.assertEqual(str(item), expected)
            self.gilded_rose.update_quality()
