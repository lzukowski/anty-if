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
            if self._sulfuras(item):
                pass
            elif self._generic(item):
                if self._quality_more_then_0(item):
                    self._decrease_quality(item)
            else:
                if self._quality_less_than_50(item):
                    self._increase_quality(item)
                    if self._backstage_pass(item):
                        if item.sell_in < 11:
                            if self._quality_less_than_50(item):
                                self._increase_quality(item)
                        if item.sell_in < 6:
                            if self._quality_less_than_50(item):
                                self._increase_quality(item)
            if not self._sulfuras(item):
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if not self._aged_brie(item):
                    if not self._backstage_pass(item):
                        if self._quality_more_then_0(item):
                            if not self._sulfuras(item):
                                self._decrease_quality(item)
                    else:
                        self._quality_to_zero(item)
                else:
                    if self._quality_less_than_50(item):
                        self._increase_quality(item)

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

    @staticmethod
    def _quality_to_zero(item):
        item.quality = item.quality - item.quality

    @staticmethod
    def _quality_more_then_0(item: Item) -> bool:
        return item.quality > 0

    @staticmethod
    def _quality_less_than_50(item: Item) -> bool:
        return item.quality < 50

    @staticmethod
    def _increase_quality(item: Item) -> None:
        item.quality = item.quality + 1

    @staticmethod
    def _decrease_quality(item: Item) -> None:
        item.quality = item.quality - 1
