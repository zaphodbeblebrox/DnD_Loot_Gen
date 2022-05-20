from secrets import choice
from Core_Window import *
from Data_Import import *
import random

class Randomizer_Handler:
    def __init__(self, programData):
        self.nonestr = "none"
        self.programData = programData
        pass

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
                if data[i][6] != self.nonestr:
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
                                if mit_array[i][1] == self.nonestr:
                                    outputMsg = outputMsg + "x1 " + mit_array[i][2] + "\n"
                                elif programData.tags.get(mit_array[i][1]) != None:
                                    outputMsg = outputMsg + "x1 " + mit_array[i][2] + " " + random.choice(programData.tags.get(mit_array[i][1])) + "\n"
                                elif programData.asw.get(mit_array[i][1]) != None:
                                    outputMsg = outputMsg + "x1 " + self.getasw(programData.asw.get(mit_array[i][1])) + "\n"
                                elif programData.rrsww.get(mit_array[i][1]) != None:
                                    outputMsg = outputMsg + "x1 " + self.getrrsww(programData.rrsww.get(mit_array[i][1])) + "\n"
                                elif programData.potion.get(mit_array[i][1]) != None:
                                    outputMsg = outputMsg + "x1 " + self.getSpell(programData.potion.get(mit_array[i][1])) + "\n"
                                elif programData.spell.get(mit_array[i][1]) != None:
                                    outputMsg = outputMsg + "x1 " + self.getScroll(programData.spell.get(mit_array[i][1])) + "\n"
                                break
                    pause = ""
                break
        return outputMsg

    def aswDrop(self, currentlvl):
        outputmsg = "x1 "
        asw_table = Data_Import.parse_dataset(self.programData.asw_loot_table.get(currentlvl), ':')
        asw_partitions = self.build_rnd_table(asw_table)
        rndRoll = random.randrange(0, asw_partitions[-1])
        asw_selected = None
        for i in range(0,len(asw_partitions)):
            if rndRoll < asw_partitions[i]:
                asw_selected = self.programData.asw.get(asw_table[i][1])
                if asw_selected == None:
                    return "No Item\n"
                else:
                    break
        
        asw_selected = Data_Import.parse_dataset(asw_selected, ";")
        asw_selected = random.choice(asw_selected)
        # asw_selected = Data_Import.parse_dataset(asw_selected, ";")
        if asw_selected[3] != "-":
            outputmsg = outputmsg + asw_selected[3] + " - "
        item = self.getrnditem(asw_selected[1])
        outputmsg = outputmsg + item

        if asw_selected[4] == '0':
            return outputmsg + " ~ Book: " + asw_selected[6] + "\n"       
        elif asw_selected[4] == '-':
            return outputmsg + " - Attune: " + asw_selected[2] + " ~ Book: " + asw_selected[6] + "\n"

        # roll enchantments....
        for i in range(int(asw_selected[4])):
            outputmsg = outputmsg + "\n    Enchant Slot " + str(i+1) + ": "
            sel = self.getEnchant(currentlvl, item)
            pass 
            
            

        
       
        return outputmsg + "\n"    
    
    def tag_compare(self, item, dicCheck):
        pass
    
    def getEnchant(self, currentlvl, item):
        et = self.programData.elt.get(currentlvl)
        et_partitions = self.build_rnd_table(et)
        et = Data_Import.parse_dataset(et, ':')
        rndRoll = random.randrange(0, et_partitions[-1])
        sel = None
        for i in range(0,len(et_partitions)):
            if rndRoll < et_partitions[i]:
                t = self.programData.enchantments.get(et[i][1])
                if t == None:
                    return "Empty"
                temp = Data_Import.parse_dataset(t, ';')
                rndchoice = ""
                while True:
                    rndchoice = random.choice(temp)
                    if rndchoice[4] == "ANY":
                        break
                    elif self.tag_compare(item, self.programData.tags.get(rndchoice[4])):
                        break

                return rndchoice[3] + " ~ Attune: " + rndchoice[2] + " ~ Req: " + rndchoice[4] + " ~ Book(pg): " + rndchoice[5]
    
    def getrnditem(self, itag):
        sel = self.programData.tags.get(itag)
        if sel == None:
            return itag
        else:
            return random.choice(sel)

    def getasw(self, array):                            #breakdown next
        temp = Data_Import.parse_dataset(array, ';')
        rndchoice = random.choice(temp)
        return rndchoice[3] + " ~ Attune: " + rndchoice[2] + " ~ Req: " + rndchoice[4] + " ~ Book(pg): " + rndchoice[5]

    def getrrsww(self, array):
        temp = Data_Import.parse_dataset(array, ';')
        rndchoice = random.choice(temp)
        return rndchoice[3] + " ~ Attune: " + rndchoice[2] + " ~ Req: " + rndchoice[4] + " ~ Book(pg): " + rndchoice[5]

    def getSpell(self, array):
        temp = Data_Import.parse_dataset(array, ';')
        rndchoice = random.choice(temp)
        return rndchoice[2]

    def getScroll(self, array):
        temp = Data_Import.parse_dataset(array, ';')
        rndchoice = random.choice(temp)
        return "Level " + rndchoice[0] + " Scroll of " + rndchoice[2]

    def getPotion(self, array):
        temp = Data_Import.parse_dataset(array, ';')
        rndchoice = random.choice(temp)
        return rndchoice[2] + " ~ Book(pg): " + rndchoice[3]
        
    def build_rnd_table(self, data):
        startCount = 0
        rndPartitions = []
        for i in range(len(data)):
            startCount = startCount + int(data[i][0])
            rndPartitions.append(startCount)
        return rndPartitions

        
    






