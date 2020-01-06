from NormalItem import NormalItem


class GildedRose:

    def __init__(self,  items):
        self.items = items

    def updateQuality(self):
        for itemClass in self.items:
            itemClass.updateQuality()
            itemClass.__repr__()
            itemClass.show()

    def showInventori(self):
        for itemClass in self.items:
            itemClass.show()
