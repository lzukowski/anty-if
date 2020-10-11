from typing import List, Text


class Item:
    def __init__(self, name: Text, sell_in: int, quality: int) -> None:
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self) -> Text:
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose:
    def __init__(self, items: List[Item]) -> None:
        self.items = items

    def update_quality(self) -> None:
        for item in self.items:
            if self._generic(item):
                if item.quality > 0:
                    item.quality = item.quality - 1
                item.sell_in = item.sell_in - 1
                if item.sell_in < 0:
                    if item.quality > 0:
                        item.quality = item.quality - 1
            elif self._aged_brie(item):
                if item.quality < 50:
                    item.quality = item.quality + 1
                item.sell_in = item.sell_in - 1
                if item.sell_in < 0:
                    if item.quality < 50:
                        item.quality = item.quality + 1
            elif self._backstage_pass(item):
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.sell_in < 11:
                        if item.quality < 50:
                            item.quality = item.quality + 1
                    if item.sell_in < 6:
                        if item.quality < 50:
                            item.quality = item.quality + 1
                item.sell_in = item.sell_in - 1
                if item.sell_in < 0:
                    item.quality = item.quality - item.quality

    @staticmethod
    def _generic(item: Item) -> bool:
        return not (
            GildedRose._aged_brie(item)
            or GildedRose._backstage_pass(item)
            or GildedRose._sulfuras(item)
        )

    @staticmethod
    def _aged_brie(item: Item) -> bool:
        return item.name == "Aged Brie"

    @staticmethod
    def _backstage_pass(item: Item) -> bool:
        return item.name == "Backstage passes to a TAFKAL80ETC concert"

    @staticmethod
    def _sulfuras(item: Item) -> bool:
        return item.name == "Sulfuras, Hand of Ragnaros"
