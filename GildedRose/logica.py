from main import main
from AgedBrie import AgedBrie
from Sulfuras import Sulfuras
from Dexterity import Dexterity
from Elixir import Elixir
from GildedRose import GildedRose
from Conjured import Conjured
from BackstagePass import BackstagePass


def update(passed_days):
    agedBrie = AgedBrie("Aged Brie", 2, 0)
    sulfuras = Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80)
    sulfuras1 = Sulfuras("Sulfuras, Hand of Ragnaros", -1, 80)
    dexterity = Dexterity("+5 Dexterity Vest", 10, 20)
    elixirMongoose = Elixir("Elixir of the Mongoose", 5, 7)
    conjuredManaCake = Conjured("Conjured Mana Cake", 3, 6)
    backstagePass = BackstagePass("Backstage passes to a TAFKAL80ETC concert", 15, 20)
    backstagePass1 = BackstagePass("Backstage passes to a TAFKAL80ETC concert", 10, 49)
    backstagePass2 = BackstagePass("Backstage passes to a TAFKAL80ETC concert", 5, 49)
    listaInventario = [dexterity, agedBrie, elixirMongoose, sulfuras,
                       sulfuras1, backstagePass, backstagePass1,
                       backstagePass2, conjuredManaCake]

    if passed_days == 0:
        dicItems = {}
        registerList = []
        for item in listaInventario:
            registerList.append([item.name, item.sellIn, item.quality])
            dicItems["DAY 0"] = registerList
        return dicItems
    else:
        for day in range(1, (passed_days + 1)):
            dicItems = {}
            registerList = []
            for item in listaInventario:
                item.updateQuality()               
                registerList.append([item.name, item.sellIn, item.quality])
                dicItems = {}
                dicItems["DAY " + str(day)] = registerList
        return dicItems


if __name__ == "__main__":

    print(update(3))