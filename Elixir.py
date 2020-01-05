from NormalItem import NormalItem
from Updateable import ItemInterface


class Elixir(NormalItem):

    def __init__(self, name, sellIn, quality):
        self.name = name
        self.sellIn = sellIn
        self.quality = quality
