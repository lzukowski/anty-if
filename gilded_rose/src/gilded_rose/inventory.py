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

    class LessThan5Days:
        @staticmethod
        def update(quality: Quality, _: int) -> None:
            quality.increase()
            quality.increase()
            quality.increase()

    class LessThan10Days:
        @staticmethod
        def update(quality: Quality, _: int) -> None:
            quality.increase()
            quality.increase()

    @staticmethod
    def update(quality: Quality, _: int) -> None:
        quality.increase()

    @classmethod
    def build(cls, sell_in: int) -> Union[
        'BackstagePass', Expired, LessThan5Days, LessThan10Days,
    ]:
        if sell_in < 0:
            return BackstagePass.Expired()
        if sell_in < 5:
            return BackstagePass.LessThan5Days()
        if sell_in < 10:
            return BackstagePass.LessThan10Days()
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
