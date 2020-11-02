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
    def __init__(self, quality: Quality) -> None:
        self.quality = quality

    def update(self, sell_in: int) -> None:
        self.quality.decrease()
        if sell_in < 0:
            self.quality.decrease()


class AgedBrie:
    def __init__(self, quality: Quality) -> None:
        self.quality = quality

    def update(self, sell_in: int) -> None:
        self.quality.increase()
        if sell_in < 0:
            self.quality.increase()


class BackstagePass:
    def __init__(self, quality: Quality) -> None:
        self.quality = quality

    def update(self, sell_in: int) -> None:
        self.quality.increase()
        if sell_in < 10:
            self.quality.increase()
        if sell_in < 5:
            self.quality.increase()
        if sell_in < 0:
            self.quality.reset()


class GoodCategory:
    def build_for(
            self, item: Item, quality: Quality,
    ) -> Union[Generic, AgedBrie, BackstagePass]:
        if self._aged_brie(item):
            return AgedBrie(quality)
        if self._backstage_pass(item):
            return BackstagePass(quality)
        return Generic(quality)

    @staticmethod
    def _aged_brie(item: Item) -> bool:
        return item.name == "Aged Brie"

    @staticmethod
    def _backstage_pass(item: Item) -> bool:
        return item.name == "Backstage passes to a TAFKAL80ETC concert"
