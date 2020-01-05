from NormalItem import NormalItem
from Updateable import ItemInterface


class Conjured(NormalItem):

    def __init__(self, name, sellIn, quality):
        self.name = name
        self.sellIn = sellIn
        self.quality = quality

    def setQuality(self):
        if self.sellIn >= 0:
            self.quality -= 2
        else:
            self.quality -= 4

    def updateQuality(self):
        self.setsellIn()
        self.setQuality()
        self.checkQuality()
        self.show()
