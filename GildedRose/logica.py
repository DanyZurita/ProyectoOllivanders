from main import main
from createObjects import createItems


def update(passed_days):
    listaInventario = createItems()

    registerDict = {}
    registerList = []

    if passed_days == 0:
        for item in listaInventario:
            registerList.append([item.name, item.sellIn, item.quality])
        registerDict["DAY 0"] = registerList
        return registerDict
    else:
        for day in range(0, passed_days):
            registerDict = {}
            registerList = []
            for item in listaInventario:
                item.updateQuality()
                registerList.append([item.name, item.sellIn, item.quality])
            registerDict["DAY " + str(day + 1)] = registerList
        return registerDict


if __name__ == "__main__":

    print(update(30)) 
