from typing import Union

from .item import Item


class Quality:
    amount: int

    def __init__(self, amount: int) -> None:
        self.amount = amount

    def decrease(self) -> None:
        if self.amount > 0:
            self.amount -= 1


class Generic:
    sell_in: int

    def __init__(self, quality: int, sell_in: int) -> None:
        self._quality = Quality(quality)
        self.sell_in = sell_in

    @property
    def quality(self) -> int:
        return self._quality.amount

    def update(self) -> None:
        self._quality.decrease()
        self.sell_in = self.sell_in - 1
        if self.sell_in < 0:
            self._quality.decrease()


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
    ) -> Union[Generic, AgedBrie, BackstagePass, Sulfuras]:
        if self._sulfuras(item):
            return Sulfuras(item.quality, item.sell_in)
        if self._aged_brie(item):
            return AgedBrie(item.quality, item.sell_in)
        if self._backstage_pass(item):
            return BackstagePass(item.quality, item.sell_in)
        return Generic(item.quality, item.sell_in)

    @staticmethod
    def _aged_brie(item: Item) -> bool:
        return item.name == "Aged Brie"

    @staticmethod
    def _backstage_pass(item: Item) -> bool:
        return item.name == "Backstage passes to a TAFKAL80ETC concert"

    @staticmethod
    def _sulfuras(item: Item) -> bool:
        return item.name == "Sulfuras, Hand of Ragnaros"
