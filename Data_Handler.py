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
        
        path_horde = Data_Import.ReadFile(self.masterList[3])
        self.hordeTreasureCoins = {
            "0-4":Data_Import.ReadFile(path_horde[0]),
            "5-10":Data_Import.ReadFile(path_horde[1]),
            "11-16":Data_Import.ReadFile(path_horde[2]),
            "17-20":Data_Import.ReadFile(path_horde[3])
        }
        self.hordeTreasureItems = {
            "0-4":Data_Import.ReadFile(path_horde[4]),
            "5-10":Data_Import.ReadFile(path_horde[5]),
            "11-16":Data_Import.ReadFile(path_horde[6]),
            "17-20":Data_Import.ReadFile(path_horde[7])
        }







