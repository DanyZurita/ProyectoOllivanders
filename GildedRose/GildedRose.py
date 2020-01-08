from NormalItem import NormalItem


class GildedRose:

    def __init__(self,  items):
        self.items = items

    def updateQuality(self):
        listaItem = []
        for item in self.items:
            item.updateQuality()
            listaItem.append(item)
        return listaItem

