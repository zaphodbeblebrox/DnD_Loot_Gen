import tkinter as tk

class Frame_Rarity:
    def __init__(self, frame):
        self.frame = frame

        self.varRty = tk.StringVar()

        tk.Radiobutton(self.frame, text="Common", variable=self.varRty, value="C", command=self.selRty).grid(sticky = "w", row=0, column=0)
        tk.Radiobutton(self.frame, text="Uncommon", variable=self.varRty, value="U", command=self.selRty).grid(sticky = "w", row=1, column=0)
        tk.Radiobutton(self.frame, text="Rare", variable=self.varRty, value="R", command=self.selRty).grid(sticky = "w", row=2, column=0)
        tk.Radiobutton(self.frame, text="Very Rare", variable=self.varRty, value="V", command=self.selRty).grid(sticky = "w", row=3, column=0)
        tk.Radiobutton(self.frame, text="Legendary", variable=self.varRty, value="L", command=self.selRty).grid(sticky = "w", row=4, column=0)
        self.rRtyLabel = tk.Label(self.frame)
        self.varRty.set("C")
        self.rRtyLabel.grid(row=5, column=0)


    # Functions-------------------
    def selRty(self):
        selection = "Option " + str(self.varRty.get())
        self.rRtyLabel.config(text = selection)
