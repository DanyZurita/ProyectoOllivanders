from NormalItem import NormalItem
from Updateable import ItemInterface


class BackstagePass(NormalItem):

    def __init__(self, name, sellIn, quality):
        self.name = name
        self.sellIn = sellIn
        self.quality = quality

    def setQuality(self):
        if self.sellIn >= 10:
            self.quality += 1
        if 10 > self.sellIn >= 5:
            self.quality += 2
        if 5 > self.sellIn >= 0:
            self.quality += 3
        if self.sellIn < 0:
            self.quality = 0

    def updateable(self):
        self.setsellIn()
        self.setQuality()
        self.checkQuality()
        self.show()
