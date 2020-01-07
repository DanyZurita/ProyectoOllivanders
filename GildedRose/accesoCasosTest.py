def readTestingFile(filePath):
    testFile = open(filePath, 'r')
    testArray = []
    for line in testFile:
        if line.find('day') != -1:
        if line.find('day') and line.find('name') and line.find('sellIn') and line.find('quality') == -1:
            item = line.rsplit(',')
            testArray.append(item)