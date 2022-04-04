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
        rndRoll = random.randrange(0, rndPartitions[len(rndPartitions)-1])
        for i in range(len(rndPartitions)):
            if rndRoll < rndPartitions[i]:
                outputMsg = data[i][3] + ": " + str(random.randrange(int(data[i][1]), int(data[i][2])))
                if data[i][6] != "none":
                    outputMsg = outputMsg + " ; " + data[i][6] + ": " + str(random.randrange(int(data[i][4]), int(data[i][5])))
                outputMsg = outputMsg + "\n"
                break
        return outputMsg






