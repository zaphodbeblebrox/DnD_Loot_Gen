import tkinter as tk
from tkinter import ttk
from Data_Import import *

class Frame_ItemTypes:
    def __init__(self, color, frame, programData):
        self.frame = frame
        self.varState = []
        tempBoolList = []
        for i in range(len(programData)):
            tempBoolList.append(programData[i][1])
        Boolean_list = list(map(lambda ele: ele == "True", tempBoolList))
		
        for i in range(len(programData)):
            tempVar = tk.BooleanVar(value=Boolean_list[i])
            ttk.Checkbutton(self.frame, text=programData[i][0], variable=tempVar, onvalue=1, offvalue=0).grid(sticky = "w", row=i, column=0, pady=3)
            self.varState.append(tempVar)





