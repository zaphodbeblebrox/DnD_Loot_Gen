from Core_Window import *
from Data_Import import *

class Data_Handler:
    def __init__(self):
        # self.fileName = fileName
        self.itemTypeList = []
        self.masterList = Data_Import.ReadFile('.\\File_Master_List.txt')
        self.itemTypeList = Data_Import.ReadFile(self.masterList[1])
        
        path_individual = Data_Import.ReadFile(self.masterList[2])
        self.individualTreasure = {
            "0-4":Data_Import.ReadFile(path_individual[0]),
            "5-10":Data_Import.ReadFile(path_individual[1]),
            "11-16":Data_Import.ReadFile(path_individual[2]),
            "17-20":Data_Import.ReadFile(path_individual[3])
            }







