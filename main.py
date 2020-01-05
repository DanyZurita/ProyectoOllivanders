from Item import Item
from NormalItem import NormalItem
from AgedBrie import AgedBrie
from Sulfuras import Sulfuras
from Dexterity import Dexterity
from Elexir import Elixir
from GildedRose import GilderRose


def main(passedDays):

    AgedBrie0 = AgedBrie("Aged Brie", 2, 0)
    Sulfuras0 = Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80)
    Sulfuras1 = Sulfuras("Sulfuras, Hand of Ragnaros", -1, 80)
    Dexterity0 = Dexterity("+5 Dexterity Vest", 10, 20)
    Elixir0 = Elixir("Elixir of Mongoose", 5, 7)
    listaInventario = [AgedBrie0, Sulfuras0, Sulfuras1, Dexterity0, Elixir0]
    tienda = GilderRose(listaInventario)
    for day in range(1, passedDays+1):
        print('\n' + '----------' + str(day) + '----------')
        tienda.updateQuality()


main(30)
