def readTestingFile(filePath):
    testFile = open(filePath, 'r')
    testArray = []
    acumulador = []
    for line in testFile:
        if line.find('- day') != -1:
            acumulador = []
        if line == '\n':
            testArray.append(acumulador)
        if lineaEsItem(line):
            # Eliminar saltos de linea y hacer splir de 2 (empieza de la derecha siempre)
            line = line.strip()
            item = line.rsplit(',', 2)
            acumulador.append(item)

    testFile.close()
    return testArray


def lineaEsItem(line):
    if line.find('day') == -1 and line.find('sellIn') == -1 and line != '\n' and line != '':
        return True
    return False


print(readTestingFile('GildedRose\stdout.gr'))
