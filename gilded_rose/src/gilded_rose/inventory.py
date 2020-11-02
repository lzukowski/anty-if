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


class Generic:
    def update(self, quality: Quality, sell_in: int) -> None:
        quality.decrease()
        if sell_in < 0:
            quality.decrease()


class AgedBrie:
    def update(self, quality: Quality, sell_in: int) -> None:
        quality.increase()
        if sell_in < 0:
            quality.increase()


class BackstagePass:
    def update(self, quality: Quality, sell_in: int) -> None:
        quality.increase()
        if sell_in < 10:
            quality.increase()
        if sell_in < 5:
            quality.increase()
        if sell_in < 0:
            quality.reset()


class GoodCategory:
    def build_for(self, item: Item) -> Union[Generic, AgedBrie, BackstagePass]:
        if self._aged_brie(item):
            return AgedBrie()
        if self._backstage_pass(item):
            return BackstagePass()
        return Generic()

    @staticmethod
    def _aged_brie(item: Item) -> bool:
        return item.name == "Aged Brie"

    @staticmethod
    def _backstage_pass(item: Item) -> bool:
        return item.name == "Backstage passes to a TAFKAL80ETC concert"
