

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
            itemClass.listItems()

    def listItems(self):
        listItems = []
        for itemClass in self.NormalItems:
            listItems.append(itemClass)
        return listItems
