from typing import List, Text, Union


class Item:
    def __init__(self, name: Text, sell_in: int, quality: int) -> None:
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self) -> Text:
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose:
    class Generic:
        quality: int
        sell_in: int

        def __init__(self, quality: int, sell_in: int) -> None:
            self.quality = quality
            self.sell_in = sell_in

        def update(self) -> None:
            if self.quality > 0:
                self.quality = self.quality - 1
            self.sell_in = self.sell_in - 1
            if self.sell_in < 0:
                if self.quality > 0:
                    self.quality = self.quality - 1

    class AgedBrie:
        quality: int
        sell_in: int

        def __init__(self, quality: int, sell_in: int) -> None:
            self.quality = quality
            self.sell_in = sell_in

        def update(self) -> None:
            if self.quality < 50:
                self.quality = self.quality + 1
            self.sell_in = self.sell_in - 1
            if self.sell_in < 0:
                if self.quality < 50:
                    self.quality = self.quality + 1

    class BackstagePass:
        quality: int
        sell_in: int

        def __init__(self, quality: int, sell_in: int) -> None:
            self.quality = quality
            self.sell_in = sell_in

        def update(self) -> None:
            if self.quality < 50:
                self.quality = self.quality + 1
                if self.sell_in < 11:
                    if self.quality < 50:
                        self.quality = self.quality + 1
                if self.sell_in < 6:
                    if self.quality < 50:
                        self.quality = self.quality + 1
            self.sell_in = self.sell_in - 1
            if self.sell_in < 0:
                self.quality = self.quality - self.quality

    class Sulfuras:
        quality: int
        sell_in: int

        def __init__(self, quality: int, sell_in: int) -> None:
            self.quality = quality
            self.sell_in = sell_in

        def update(self) -> None:
            pass

    class GoodCategory:
        def build_for(
                self, item: Item
        ) -> Union[
            'GildedRose.Generic',
            'GildedRose.AgedBrie',
            'GildedRose.BackstagePass',
            'GildedRose.Sulfuras',
        ]:
            if self._sulfuras(item):
                return GildedRose.Sulfuras(item.quality, item.sell_in)
            elif self._aged_brie(item):
                return GildedRose.AgedBrie(item.quality, item.sell_in)
            elif self._backstage_pass(item):
                return GildedRose.BackstagePass(item.quality, item.sell_in)
            return GildedRose.Generic(item.quality, item.sell_in)

        @staticmethod
        def _aged_brie(item: Item) -> bool:
            return item.name == "Aged Brie"

        @staticmethod
        def _backstage_pass(item: Item) -> bool:
            return item.name == "Backstage passes to a TAFKAL80ETC concert"

        @staticmethod
        def _sulfuras(item: Item) -> bool:
            return item.name == "Sulfuras, Hand of Ragnaros"

    def __init__(self, items: List[Item]) -> None:
        self.items = items

    def update_quality(self) -> None:
        for item in self.items:
            good = GildedRose.GoodCategory().build_for(item)
            good.update()
            item.quality = good.quality
            item.sell_in = good.sell_in
