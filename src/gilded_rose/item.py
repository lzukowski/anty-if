from dataclasses import dataclass
from typing import Text


@dataclass
class Item:
    name: Text
    sell_in: int
    quality: int
