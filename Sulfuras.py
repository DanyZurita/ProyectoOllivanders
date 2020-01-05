from NormalItem import NormalItem


class Sulfuras(NormalItem):

    def __init__(self, name, sellIn, quality):
        self.name = name
        self.sellIn = sellIn
        self.quality = quality

    def updateQuality(self):
        pass