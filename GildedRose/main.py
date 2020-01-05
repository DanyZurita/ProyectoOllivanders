from AgedBrie import AgedBrie
from Sulfuras import Sulfuras
from Dexterity import Dexterity
from Elixir import Elixir
from GildedRose import GildedRose
from Conjured import Conjured
from BackstagePass import BackstagePass


def main(passedDays):

    agedBrie = AgedBrie("Aged Brie", 2, 0)
    sulfuras = Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80)
    sulfuras1 = Sulfuras("Sulfuras, Hand of Ragnaros", -1, 80)
    dexterity = Dexterity("+5 Dexterity Vest", 10, 20)
    elixirMongoose = Elixir("Elixir of Mongoose", 5, 7)
    conjuredManaCake = Conjured("Conjured Mana Cake", 3, 6)
    backstagePass = BackstagePass("Backstage Passes to TAFKAL80ETC concert", 15, 20)
    backstagePass1 = BackstagePass("Backstage Passes to TAFKAL80ETC concert", 10, 49)
    backstagePass2 = BackstagePass("Backstage Passes to TAFKAL80ETC concert", 5, 49)

    listaInventario = [agedBrie, sulfuras, sulfuras1, dexterity, elixirMongoose, conjuredManaCake, backstagePass, backstagePass1, backstagePass2]
    tienda = GildedRose(listaInventario)

    print('\n' + '---------- DAY 0 ----------')
    tienda.show()
    tienda.__repr__()
    if passedDays != 0:
        for day in range(1, passedDays+1):
            print('\n' + '---------- DAY ' + str(day) + ' ----------')
            tienda.updateQuality()
            tienda.show()
            

if __name__ == "__main__":
    main(3)