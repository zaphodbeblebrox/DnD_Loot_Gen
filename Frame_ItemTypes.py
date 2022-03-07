import tkinter as tk

class Frame_ItemTypes:
    def __init__(self, frame, data):
        self.frame = frame
        self.data = data

        for i in range(len(self.data)):
           tk.Checkbutton(self.frame, text=self.data[i][0], variable=self.data[i][1].set(self.data[i][2]), onvalue=1, offvalue=0).grid(sticky = "w", row=i, column=0)




