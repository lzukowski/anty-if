from typing import Union

from .item import Item


class Quality:
    amount: int

    def __init__(self, amount: int) -> None:
        self.amount = amount

    def decrease(self) -> None:
        if self.amount > 0:
            self.amount -= 1

    def increase(self) -> None:
        if self.amount < 50:
            self.amount += 1

    def reset(self) -> None:
        self.amount = 0

    def less_then_50(self):
        return self.amount < 50


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
    sell_in: int

    def __init__(self, quality: int, sell_in: int) -> None:
        self._quality = Quality(quality)
        self.sell_in = sell_in

    @property
    def quality(self) -> int:
        return self._quality.amount

    def update(self) -> None:
        self._quality.increase()
        self.sell_in = self.sell_in - 1
        if self.sell_in < 0:
            self._quality.increase()


class BackstagePass:
    sell_in: int

    def __init__(self, quality: int, sell_in: int) -> None:
        self._quality = Quality(quality)
        self.sell_in = sell_in

    @property
    def quality(self) -> int:
        return self._quality.amount

    def update(self) -> None:
        self._quality.increase()
        if self._quality.less_then_50():
            if self.sell_in < 11:
                self._quality.increase()
            if self.sell_in < 6:
                self._quality.increase()
        self.sell_in = self.sell_in - 1
        if self.sell_in < 0:
            self._quality.reset()


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
