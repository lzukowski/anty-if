from collections import namedtuple

from pytest import mark

from gilded_rose import GildedRose, Item


class TestGildedRose:
    DataSet = namedtuple("TestSet", "expected, sell_in, quality")

    @mark.xfail(raises=NotImplementedError, strict=True)
    @mark.parametrize(
        "expected, sell_in, quality",
        [
            DataSet(expected=0, sell_in=0, quality=0),
            DataSet(expected=-1, sell_in=0, quality=-1),
            DataSet(expected=1, sell_in=-1, quality=3),
            DataSet(expected=1, sell_in=0, quality=3),
            DataSet(expected=0, sell_in=0, quality=1),
            DataSet(expected=9, sell_in=1, quality=10),
        ]
    )
    def test_generic(self, expected: int, sell_in: int, quality: int):
        item = Item("foo", sell_in=sell_in, quality=quality)
        GildedRose([item]).update_quality()
        assert expected == item.quality

    @mark.xfail(raises=NotImplementedError, strict=True)
    @mark.parametrize(
        "expected, sell_in, quality",
        [
            DataSet(expected=0, sell_in=0, quality=0),
            DataSet(expected=-1, sell_in=0, quality=-1),
            DataSet(expected=0, sell_in=-1, quality=3),
            DataSet(expected=0, sell_in=0, quality=3),
            DataSet(expected=0, sell_in=0, quality=1),
            DataSet(expected=8, sell_in=1, quality=10),
        ]
    )
    def test_conjured(self, expected: int, sell_in: int, quality: int):
        item = Item("Conjured Mana Cake", sell_in=sell_in, quality=quality)
        GildedRose([item]).update_quality()
        assert expected == item.quality

    @mark.xfail(raises=NotImplementedError, strict=True)
    @mark.parametrize(
        "expected, sell_in, quality",
        [
            DataSet(expected=22, sell_in=8, quality=20),
            DataSet(expected=23, sell_in=4, quality=20),
            DataSet(expected=0, sell_in=0, quality=20),
            DataSet(expected=23, sell_in=1, quality=20),
            DataSet(expected=22, sell_in=6, quality=20),
            DataSet(expected=23, sell_in=5, quality=20),
            DataSet(expected=22, sell_in=10, quality=20),
            DataSet(expected=21, sell_in=11, quality=20),
            DataSet(expected=51, sell_in=11, quality=51),
        ]
    )
    def test_backstage_pass(self, expected: int, sell_in: int, quality: int):
        item = Item(
            "Backstage passes to a TAFKAL80ETC concert",
            sell_in=sell_in, quality=quality,
        )
        GildedRose([item]).update_quality()
        assert expected == item.quality

    @mark.xfail(raises=NotImplementedError, strict=True)
    @mark.parametrize(
        "expected, sell_in, quality",
        [
            DataSet(expected=22, sell_in=0, quality=20),
            DataSet(expected=21, sell_in=1, quality=20),
        ]
    )
    def test_aged_brie(self, expected: int, sell_in: int, quality: int):
        item = Item("Aged Brie", sell_in=sell_in, quality=quality)
        GildedRose([item]).update_quality()
        assert expected == item.quality
