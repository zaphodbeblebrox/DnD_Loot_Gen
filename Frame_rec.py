import tkinter as tk

class Frame_rec:
    def __init__(self, frame, numLevels):
        self.frame = frame
        self.numLevels = numLevels

        self.varLvl = tk.IntVar() 
        self.rbLevels = []

        for i in range(self.numLevels):
            self.label = "Level " + str(i+1)
            self.rbLevels.append(tk.Radiobutton(self.frame, text=self.label, variable=self.varLvl, value=(i+1), command=self.sel))
            self.rbLevels[i].grid(sticky = "w", row=(i+1), column=0)
        
        self.varLvl.set(1)
        self.rLvlLabel = tk.Label(self.frame)
        self.rLvlLabel.grid(sticky = "w", row=len(self.rbLevels)+1, column=0)

    # Functions-------------------
    def sel(self):
        selection = "Option " + str(self.varLvl.get())
        self.rLvlLabel.config(text = selection)




