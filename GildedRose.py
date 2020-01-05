from Item import Item
from NormalItem import NormalItem
from AgedBrie import AgedBrie
from Sulfuras import Sulfuras
from Dexterity import Dexterity
from Elixir import Elixir


class GildedRose(NormalItem):

    def __init__(self,  NormalItems):
        self.NormalItems = NormalItems

    def updateQuality(self):
        for itemClass in self.NormalItems:
            itemClass.updateQuality()
