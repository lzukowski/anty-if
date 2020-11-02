from typing import List

from .inventory import GoodCategory, Quality
from .item import Item


class GildedRose:
    def __init__(self, items: List[Item]) -> None:
        self.items = items

    def update_quality(self) -> None:
        for item in self.items:
            if self._sulfuras(item):
                continue
            item.sell_in -= 1
            quality = Quality(item.quality)
            good = GoodCategory().build_for(item)
            good.update(quality, item.sell_in)
            item.quality = quality.amount

    @staticmethod
    def _sulfuras(item: Item) -> bool:
        return item.name == "Sulfuras, Hand of Ragnaros"
