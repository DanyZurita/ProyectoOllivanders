from AgedBrie import AgedBrie


def passDays(item, days):
    registerList = []
    for day in range(1, days):
        item.updateQuality()
        registerList.append([day, item.sellIn, item.quality])
    return registerList


def test_agedBrieTwoDaysZeroQuality():
    agedBrie = AgedBrie("Aged Brie", 2, 0)
    assert passDays(agedBrie, 5) == [[1, 1, 1], [2, 0, 2], [3, -1, 4], [4, -2, 6]]
