from Core_Window import *
from Data_Import import *

class Data_Handler:
    def __init__(self):
        # self.fileName = fileName
        self.itemTypeList = []
        self.masterList = Data_Import.ReadFile('.\\File_Master_List.txt')
        self.itemTypeList = Data_Import.ReadFile(self.masterList[1])
        print(self.itemTypeList)
        print("\n-----------")
        print(self.itemTypeList[0])




