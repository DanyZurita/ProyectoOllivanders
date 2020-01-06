from AgedBrie import AgedBrie
from Sulfuras import Sulfuras
from Dexterity import Dexterity
from Elixir import Elixir
from GildedRose import GildedRose
from Conjured import Conjured
from BackstagePass import BackstagePass
from NormalItem import NormalItem
from createObjects import createItems

def main(passedDays):
    listaInventario = createItems()
    tiendaGildedRose = GildedRose(listaInventario)

    print('\n' + '---------- DAY 0 ----------')
    tiendaGildedRose.showInventori()
    tiendaGildedRose.__repr__()
    if passedDays != 0:
        for day in range(0, passedDays):
            print('\n' + '---------- DAY ' + str(day + 1) + ' ----------')
            tiendaGildedRose.updateQuality()


if __name__ == "__main__":

    print(main(1))
