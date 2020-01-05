from Item import Item
from Updateable import ItemInterface


class NormalItem(Item, ItemInterface):

    def __init__(self, name, sellIn, quality):
        self.name = name
        self.sellIn = sellIn
        self.quality = quality

    def setSellIn(self):
        self.sellIn = self.sellIn - 1

    def checkQuality(self):
        if self.quality > 50:
            self.quality = 50
        if self.quality < 0:
            self.quality = 0

    def setQuality(self):
        if self.sellIn > 0:
            self.quality -= 1
        else:
            self.quality -= 2

    def updateQuality(self):
        self.setSellIn()
        self.setQuality()
        self.checkQuality()

    def show(self):
        print(self)

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sellIn, self.quality)
