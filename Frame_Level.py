import tkinter as tk
from tkinter import font, ttk

class Frame_Level:
    def __init__(self, color, frame, numLevels):
        self.frame = frame
        self.numLevels = numLevels

        f = font.Font(weight = "bold", size= 10)
        style = ttk.Style()
        style.configure('TRadiobutton', foreground=color["red"], background=color["dark gray"], indicatorcolor=color["white"], font=f)

        style.map('TRadiobutton',
          foreground = [('disabled', color["red"]),
                      ('pressed', color["red"]),
                      ('active', color["light gray"])],
          background = [('disabled', color["dark gray"]),
                      ('pressed', '!focus', color["dark gray"]),
                      ('active', color["dark gray"])],
          indicatorcolor=[('selected', color["cyan"]),
                          ('pressed', color["cyan"])]
          )

        self.varLvl = tk.IntVar() 
        self.rbLevels = []

        for i in range(self.numLevels):
            self.label = "Level " + str(i+1)
            self.rbLevels.append(ttk.Radiobutton(self.frame, text=self.label, variable=self.varLvl, value=(i+1), style='TRadiobutton'))
            # self.rbLevels.append(tk.Radiobutton(self.frame, text=self.label, variable=self.varLvl, value=(i+1), command=self.sel, 
            #                         bg=color["dark gray"], fg=color["red"], selectcolor=color["purple"], font=f, activebackground=color["dark gray"],
            #                         activeforeground=color["red"]))
            self.rbLevels[i].grid(sticky = "w", row=(i+1), column=0, pady=3)
        
        self.varLvl.set(1)



