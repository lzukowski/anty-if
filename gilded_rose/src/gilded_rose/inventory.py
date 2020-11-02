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
    def __init__(self, quality: int) -> None:
        self._quality = Quality(quality)

    @property
    def quality(self) -> int:
        return self._quality.amount

    def update(self, sell_in: int) -> None:
        self._quality.decrease()
        if sell_in < 0:
            self._quality.decrease()


class AgedBrie:
    def __init__(self, quality: int) -> None:
        self._quality = Quality(quality)

    @property
    def quality(self) -> int:
        return self._quality.amount

    def update(self, sell_in: int) -> None:
        self._quality.increase()
        if sell_in < 0:
            self._quality.increase()


class BackstagePass:
    def __init__(self, quality: int) -> None:
        self._quality = Quality(quality)

    @property
    def quality(self) -> int:
        return self._quality.amount

    def update(self, sell_in: int) -> None:
        self._quality.increase()
        if sell_in < 10:
            self._quality.increase()
        if sell_in < 5:
            self._quality.increase()
        if sell_in < 0:
            self._quality.reset()


class GoodCategory:
    def build_for(self, item: Item) -> Union[Generic, AgedBrie, BackstagePass]:
        if self._aged_brie(item):
            return AgedBrie(item.quality)
        if self._backstage_pass(item):
            return BackstagePass(item.quality)
        return Generic(item.quality)

    @staticmethod
    def _aged_brie(item: Item) -> bool:
        return item.name == "Aged Brie"

    @staticmethod
    def _backstage_pass(item: Item) -> bool:
        return item.name == "Backstage passes to a TAFKAL80ETC concert"
