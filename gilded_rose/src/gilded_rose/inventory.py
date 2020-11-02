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
    class Expired:
        @staticmethod
        def update(quality: Quality, _: int) -> None:
            quality.decrease()
            quality.decrease()

    @staticmethod
    def update(quality: Quality, _: int) -> None:
        quality.decrease()

    @classmethod
    def build(cls, sell_in: int) -> Union['Generic', Expired]:
        if sell_in < 0:
            return Generic.Expired()
        return Generic()


class AgedBrie:
    class Expired:
        @staticmethod
        def update(quality: Quality, _: int) -> None:
            quality.increase()
            quality.increase()

    @staticmethod
    def update(quality: Quality, _: int) -> None:
        quality.increase()

    @classmethod
    def build(cls, sell_in: int) -> Union['AgedBrie', Expired]:
        if sell_in < 0:
            return AgedBrie.Expired()
        return AgedBrie()


class BackstagePass:
    class Expired:
        @staticmethod
        def update(quality: Quality, _: int) -> None:
            quality.reset()

    @staticmethod
    def update(quality: Quality, sell_in: int) -> None:
        quality.increase()
        if sell_in < 10:
            quality.increase()
        if sell_in < 5:
            quality.increase()

    @classmethod
    def build(cls, sell_in: int) -> Union['BackstagePass', Expired]:
        if sell_in < 0:
            return BackstagePass.Expired()
        return BackstagePass()


class GoodCategory:
    def build_for(self, item: Item) -> Union[Generic, AgedBrie, BackstagePass]:
        if self._aged_brie(item):
            return AgedBrie.build(item.sell_in)
        if self._backstage_pass(item):
            return BackstagePass.build(item.sell_in)
        return Generic.build(item.sell_in)

    @staticmethod
    def _aged_brie(item: Item) -> bool:
        return item.name == "Aged Brie"

    @staticmethod
    def _backstage_pass(item: Item) -> bool:
        return item.name == "Backstage passes to a TAFKAL80ETC concert"
