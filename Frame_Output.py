import tkinter as tk

class Frame_Output:
    def __init__(self, frame):
        self.frame = frame
        msg = "Item\t\tStat\n"
        self.output = tk.Text(self.frame, height = 32, width = 52, state="normal")
        self.output.insert("insert", msg)
        self.output.config(state="disabled")
        self.output.grid(row=0, column=0)

    def newOutput(self, msg):
        self.output.config(state="normal")
        self.output.insert('2.0', msg)    #'row.col' position
        self.output.config(state="disabled")