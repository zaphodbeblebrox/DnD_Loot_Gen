from Core_Window import *

class Data_Import:
    def __init__(self):
        # self.fileName = fileName
        self.itemTypeList = []
        self.itpath = '.\\Items\\Item_Types.txt'
        self.ReadFile(self.itpath)

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


