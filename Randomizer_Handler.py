from Core_Window import *
from Data_Import import *
import random

class Randomizer_Handler:
    def __init__(self):
        self.trigger = 0

    # def randomNumberGenerator(self, max)
  
    def indivTreasure(dataLootTable):
        data = Data_Import.parse_dataset(dataLootTable, ':')
        rndPartitions = []
        outputMsg = ""
        startCount = 0
        for i in range(len(dataLootTable)):
            startCount = startCount + int(data[i][0])
            rndPartitions.append(startCount)
        rndRoll = random.randrange(0, rndPartitions[-1])
        for i in range(len(rndPartitions)):
            if rndRoll < rndPartitions[i]:
                outputMsg = data[i][3] + ": " + str(random.randrange(int(data[i][1]), int(data[i][2])))
                if data[i][6] != "none":
                    outputMsg = outputMsg + " ; " + data[i][6] + ": " + str(random.randrange(int(data[i][4]), int(data[i][5])))
                outputMsg = outputMsg + "\n"
                break
        return outputMsg

    def hordeTreasure(dataCoinTable, dataItemTable):
        dataCoin = Data_Import.parse_dataset(dataCoinTable, ':')
        outputMsg = ""
        for i in range(len(dataCoin)):
            if int(dataCoin[i][2]) != 0:
                outputMsg = outputMsg + dataCoin[i][0] + ": " + str(random.randrange(int(dataCoin[i][1]), int(dataCoin[i][2]))) + "\n"
        
        dataItem = Data_Import.parse_dataset(dataItemTable, ':')
        rndPartitions = []
        startCount = 0
        for i in range(len(dataItem)):
            startCount = startCount + int(dataItem[i][0])
            rndPartitions.append(startCount)
        rndRoll = random.randrange(0, rndPartitions[-1])
        for i in range(len(rndPartitions)):
            if rndRoll < rndPartitions[i]:
                # Grab tag and process
                outputMsg = dataItem[i][3] + ": " + str(random.randrange(int(dataItem[i][1]), int(dataItem[i][2])))
                if dataItem[i][6] != "none":
                    outputMsg = outputMsg + " ; " + dataItem[i][6] + ": " + str(random.randrange(int(dataItem[i][4]), int(dataItem[i][5])))
                outputMsg = outputMsg + "\n"
                break
        
        
        
        return outputMsg
        rndRoll = random.randrange(0, rndPartitions[len(rndPartitions)-1])
        for i in range(len(rndPartitions)):
            if rndRoll < rndPartitions[i]:
                outputMsg = data[i][3] + ": " + str(random.randrange(int(data[i][1]), int(data[i][2])))
                if data[i][6] != "none":
                    outputMsg = outputMsg + " ; " + data[i][6] + ": " + str(random.randrange(int(data[i][4]), int(data[i][5])))
                outputMsg = outputMsg + "\n"
                break
        return outputMsg






