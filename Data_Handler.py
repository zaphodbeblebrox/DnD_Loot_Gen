from Core_Window import *
from Data_Import import *

class Data_Handler:
    def __init__(self):
        # self.fileName = fileName
        self.itemTypeList = []
        self.masterList = Data_Import.read_file('.\\File_Master_List.txt')
        self.itemTypeList = Data_Import.read_file(self.masterList[1])
        
        path_individual = Data_Import.read_file(self.masterList[2])
        self.individualTreasure = {
            "0-4":Data_Import.read_file(path_individual[0]),
            "5-10":Data_Import.read_file(path_individual[1]),
            "11-16":Data_Import.read_file(path_individual[2]),
            "17-20":Data_Import.read_file(path_individual[3])
            }
        
        path_horde = Data_Import.read_file(self.masterList[3])
        self.hordeTreasureCoins = {
            "0-4":Data_Import.read_file(path_horde[0]),
            "5-10":Data_Import.read_file(path_horde[1]),
            "11-16":Data_Import.read_file(path_horde[2]),
            "17-20":Data_Import.read_file(path_horde[3])
        }
        self.hordeTreasureItems = {
            "0-4":Data_Import.read_file(path_horde[4]),
            "5-10":Data_Import.read_file(path_horde[5]),
            "11-16":Data_Import.read_file(path_horde[6]),
            "17-20":Data_Import.read_file(path_horde[7])
        }
        self.tags = Data_Import.create_dictionary(self.masterList[4])
        self.mit = Data_Import.create_dictionary(self.masterList[5])
        puase = ""










