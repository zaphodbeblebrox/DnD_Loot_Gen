from Core_Window import *
from Data_Import import *

class Data_Handler:
    def __init__(self):
        # self.fileName = fileName
        self.itemTypeList = []
        self.masterList = Data_Import.ReadFile('.\\File_Master_List.txt')
        self.itemTypeList = Data_Import.ReadFile(self.masterList[1])

    def ReadFile(self, fileName):
        content_array = []
        with open(fileName) as f:
                #Content_list is the list that contains the read lines.     
                for line in f:
                        content_array.append(line)
        return content_array

    def parse_file(self, array):
        leftColData = [0 for x in range(len(array))]
        rightColData = [0 for x in range(len(array))]
        for i in range(len(array)):
            tempArray = array[i].split(';')
            leftColData[i] = tempArray[0]
            rightColData[i] = tempArray[1]
        return (leftColData, rightColData)


