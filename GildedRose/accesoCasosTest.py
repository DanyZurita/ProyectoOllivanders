def readTestingFile(filePath):
    testFile = open(filePath, 'r')
    testArray = []
    acumulador = []
    for line in testFile:
        if line.find('day') != -1:
            testArray.append(acumulador)
            acumulador = []
        if line.find('day') and line.find('name') and line.find('sellIn') and line.find('quality') == -1:
            item = line.rsplit(',')
            acumulador.append(item)

    testFile.close()
    return testArray

print(readTestingFile('stdout.gr'))