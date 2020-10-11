from abc import ABC, abstractmethod

from .item import Item


class Good(ABC):
    quality: int
    sell_in: int

    def __init__(self, quality: int, sell_in: int) -> None:
        self.quality = quality
        self.sell_in = sell_in

    @abstractmethod
    def update(self) -> None:
        raise NotImplementedError


class Generic(Good):
    def update(self) -> None:
        if self.quality > 0:
            self.quality = self.quality - 1
        self.sell_in = self.sell_in - 1
        if self.sell_in < 0:
            if self.quality > 0:
                self.quality = self.quality - 1


class AgedBrie(Good):
    def update(self) -> None:
        if self.quality < 50:
            self.quality = self.quality + 1
        self.sell_in = self.sell_in - 1
        if self.sell_in < 0:
            if self.quality < 50:
                self.quality = self.quality + 1


class BackstagePass(Good):
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


class Sulfuras(Good):
    def update(self) -> None:
        pass


class GoodCategory:
    def build_for(self, item: Item) -> Good:
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
