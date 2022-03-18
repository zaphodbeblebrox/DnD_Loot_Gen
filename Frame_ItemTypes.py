import tkinter as tk
from Data_Import import *

class Frame_ItemTypes:
    def __init__(self, frame, dataFile):
        self.frame = frame
        self.varState = []
        
        self.templist, tempBoolList = Data_Import.parse_file(dataFile)
        for i in range(len(tempBoolList)):
            tempBoolList[i] = tempBoolList[i].replace("\n","")
        Boolean_list = list(map(lambda ele: ele == "True", tempBoolList))
		
        for i in range(len(self.templist)):
            tempVar = tk.BooleanVar()
            tk.Checkbutton(self.frame, text=self.templist[i], variable=tempVar.set(Boolean_list[i]), onvalue=1, offvalue=0).grid(sticky = "w", row=i, column=0)
            self.varState.append(tempVar)





