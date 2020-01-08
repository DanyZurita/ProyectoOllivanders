from GildedRose import GildedRose
from createObjects import createItems


def main(passedDays):
    listaInventario = createItems()
    tiendaGildedRose = GildedRose(listaInventario)
    updatedItemsArray = tiendaGildedRose.items
    if passedDays > 0:
        for day in range(0, passedDays):
            tiendaGildedRose.updateQuality()
        updatedItemsArray = tiendaGildedRose.items
    return updatedItemsArray

print(main(5))

