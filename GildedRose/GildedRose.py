from NormalItem import NormalItem


class GildedRose:

    def __init__(self,  items):
        self.items = items

    def updateQuality(self):
        for itemClass in self.items:
            itemClass.updateQuality()
            itemClass.show()

    def showInventori(self):
        for itemClass in self.items:
            itemClass.show()

    def __repr__(self, passed_days):
        registerDict = {}
        registerList = []
        if passed_days == 0:
            for itemClass in self.items:
                registerList.append([itemClass.__repr__()])
            registerDict["DAY 0"] = registerList
            return registerList
        else:
            for day in range(0, (passed_days)):
                registerDict = {}
                registerList = []
                for itemClass in self.items:
                    itemClass.updateQuality()
                    registerList.append([itemClass.__repr__()])
                registerDict["DAY " + str(day + 1)] = registerList
            return registerDict
