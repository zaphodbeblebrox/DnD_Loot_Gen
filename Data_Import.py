from Core_Window import *

class Data_Import:
    def __init__(self):
        # self.fileName = fileName
        self.itemTypeList = []
        self.itpath = '.\\Items\\Item_Types.txt'
        # self.ReadFile(self.itpath)

    def ReadFile(fileName):
        content_array = []
        with open(fileName) as f:
                #Content_list is the list that contains the read lines.     
                for line in f:
                        content_array.append(line.replace('\n',''))
        return content_array

    def parse_file(array, deliminator):
        leftColData = [0 for x in range(len(array))]
        rightColData = [0 for x in range(len(array))]
        temp = []
        for i in range(len(array)):
            tempArray = array[i].split(deliminator)
            temp.append(tempArray)
            leftColData[i] = tempArray[0]
            rightColData[i] = tempArray[1]
        return (leftColData, rightColData)
        

    def parse_dataset(array, deliminator):
        leftColData = [0 for x in range(len(array))]
        rightColData = [0 for x in range(len(array))]
        temp = []
        for i in range(len(array)):
            tempArray = array[i].split(deliminator)
            temp.append(tempArray)
            leftColData[i] = tempArray[0]
            rightColData[i] = tempArray[1]
        # return (leftColData, rightColData)
        return temp


