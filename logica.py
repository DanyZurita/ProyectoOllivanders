from main import main

def update(passed_days):
    if passed_days == 0:
        return [["name", "sellIn", "quality"],
                    ["+5 Dexterity Vest", 10, 20],
                    ["Aged Brie", 2, 0],
                    ["Elixir of the Mongoose", 5, 7],
                    ["Sulfuras, Hand of Ragnaros", 0, 80],
                    ["Sulfuras, Hand of Ragnaros", -1, 80],
                    ["Backstage passes to a TAFKAL80ETC concert", 15, 20],
                    ["Backstage passes to a TAFKAL80ETC concert", 10, 49],
                    ["Backstage passes to a TAFKAL80ETC concert", 5, 49],
                    ["Conjured Mana Cake", 3, 6]]
    else:
        i = passed_days
        while i != 0:
            lists = []
            lists = lists.append(list(main()))
            i -= 1
        return lists



print(update(3))