import tkinter as tk
from tkinter import ttk


class Frame_Output:
    def __init__(self, color, frame):
        self.frame = frame
        self.output_scrollbar = ttk.Scrollbar(self.frame)
        self.output_scrollbar.grid(row=0, column=1, sticky="nesw")
        msg = "Welcome to the Loot Generator!\n"
        self.output = tk.Text(self.frame, height = 32, width = 100, state="normal", background=color["txt bg"], fg=color["txt fg"], bd=0, yscrollcommand=self.output_scrollbar.set)
        self.output.insert("insert", msg)
        self.output.config(state="disabled")
        self.output.grid(row=0, column=0)
        self.output_scrollbar.config(command=self.output.yview)

    def newOutput(self, msg):
        msg = msg + "----------\n"
        self.output.config(state="normal")
        self.output.insert('1.0', msg)    #'row.col' position
        self.output.config(state="disabled")
        self.output.see('1.0')