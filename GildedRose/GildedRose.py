

class GildedRose(object):

    def __init__(self,  items):
        self.NormalItems = items

    def updateQuality(self):
        for itemClass in self.NormalItems:
            itemClass.updateQuality()
            itemClass.__repr__()

    def show(self):
        for itemClass in self.NormalItems:
            itemClass.show()
