from Core_Window import *
from Data_Import import *
import random

class Randomizer_Handler:
    def __init__(self):
        pass

    # def randomNumberGenerator(self, max)
  
    def build_rnd_table(self, data):
        startCount = 0
        rndPartitions = []
        for i in range(len(data)):
            startCount = startCount + int(data[i][0])
            rndPartitions.append(startCount)
        return rndPartitions


    def indivTreasure(self, dataLootTable):
        data = Data_Import.parse_dataset(dataLootTable, ':')
        # rndPartitions = self.build_rnd_table(data)
        rndPartitions = []
        outputMsg = ""
        rndPartitions = self.build_rnd_table(data)
        rndRoll = random.randrange(0, rndPartitions[-1])
        for i in range(len(rndPartitions)):
            if rndRoll < rndPartitions[i]:
                outputMsg = data[i][3] + ": " + str(random.randrange(int(data[i][1]), int(data[i][2])))
                if data[i][6] != "none":
                    outputMsg = outputMsg + " ; " + data[i][6] + ": " + str(random.randrange(int(data[i][4]), int(data[i][5])))
                outputMsg = outputMsg + "\n"
                break
        return outputMsg

    def hordeTreasure(self, dataCoinTable, dataItemTable, programData):
        # Coins
        dataCoin = Data_Import.parse_dataset(dataCoinTable, ':')
        outputMsg = ""
        for i in range(len(dataCoin)):
            if int(dataCoin[i][2]) != 0:
                outputMsg = outputMsg + dataCoin[i][0] + ": " + str(random.randrange(int(dataCoin[i][1]), int(dataCoin[i][2]))) + "\n"
        
        # Gems and Art
        dataItem = Data_Import.parse_dataset(dataItemTable, ':')
        rndPartitions = self.build_rnd_table(dataItem)
        rndRoll = random.randrange(0, rndPartitions[-1])
        for i in range(0,len(rndPartitions)):
            if rndRoll < rndPartitions[i]:
                if int(dataItem[i][2]) == 0:
                    break
                num_items = random.randrange(int(dataItem[i][1]), int(dataItem[i][2]))
                item_list = Data_Import.parse_dataset(programData.tags.get(dataItem[i][3]), ";")
                item_dic = {}
                for y in range(0,num_items):
                    roll = random.randrange(0, len(item_list)-1)
                    if item_dic.get(item_list[roll][1]) == None:
                        item_dic[item_list[roll][1]] = [1, item_list[roll][0], item_list[roll][1], item_list[roll][2]]
                    else:
                        item_dic[item_list[roll][1]][0] = item_dic[item_list[roll][1]][0] + 1

                for key in item_dic:
                    if item_dic[key][3] != "":
                        outputMsg = outputMsg + str(item_dic[key][0]) + "x " + item_dic[key][1] + "gp "+ item_dic[key][2] + " ~ " + item_dic[key][3] + "\n"
                    else:
                        outputMsg = outputMsg + str(item_dic[key][0]) + "x " + item_dic[key][1] + "gp "+ item_dic[key][2] + "\n"
                outputMsg = outputMsg + "\n"
                
                # Magic Item Table
                t = programData.mit
                if int(dataItem[i][4]) > 0:
                    if int(dataItem[i][4]) == 1: 
                        num_items = 1
                    else:
                        num_items = random.randrange(1, int(dataItem[i][4]))
                    mit_array = Data_Import.parse_dataset(programData.mit.get(dataItem[i][5]), ':')
                    mitPartitions = self.build_rnd_table(mit_array)                   
                    for r in range(0, num_items):
                        table_roll = random.randrange(0, mitPartitions[-1])
                        for i in range(0, len(mitPartitions)-1):
                            if table_roll<mitPartitions[i]:
                                outputMsg = outputMsg + "x1 " + mit_array[i][2] + "\n"
                                break



                    pause = ""
                    pass


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






