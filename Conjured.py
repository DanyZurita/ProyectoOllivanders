from NormalItem import NormalItem


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
