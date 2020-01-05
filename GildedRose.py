

class GildedRose(object):

    def __init__(self,  items):
        self.NormalItems = items

    def updateQuality(self):
        for itemClass in self.NormalItems:
            itemClass.updateQuality()

    def show(self):
        for itemClass in self.NormalItems:
            itemClass.show()
