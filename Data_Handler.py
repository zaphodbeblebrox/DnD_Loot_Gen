from Core_Window import *
from Data_Import import *

class Data_Handler:
    def __init__(self):
        # self.fileName = fileName
        self.itemTypeList = []
        self.masterList = Data_Import.ReadFile('.\\File_Master_List.txt')
        self.itemTypeList = Data_Import.ReadFile(self.masterList[1])
        
        path_individual = Data_Import.ReadFile(self.masterList[2])
        self.individual_0_4 = Data_Import.ReadFile(path_individual[0])
        self.individual_5_10 = Data_Import.ReadFile(path_individual[1])
        self.individual_11_16 = Data_Import.ReadFile(path_individual[2])
        self.individual_17_20 = Data_Import.ReadFile(path_individual[3])






