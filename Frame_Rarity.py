import tkinter as tk
from tkinter import ttk, font

class Frame_Rarity:
    def __init__(self, color, frame):
        self.frame = frame

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
          indicatorcolor=[('selected', color["neon pink"]),
                          ('pressed', color["neon pink"])]
          )

        self.varRty = tk.StringVar()

        ttk.Radiobutton(self.frame, text="Common", variable=self.varRty, value="C", style='TRadiobutton').grid(sticky = "w", row=0, column=0)
        ttk.Radiobutton(self.frame, text="Uncommon", variable=self.varRty, value="U", style='TRadiobutton').grid(sticky = "w", row=1, column=0)
        ttk.Radiobutton(self.frame, text="Rare", variable=self.varRty, value="R", style='TRadiobutton').grid(sticky = "w", row=2, column=0)
        ttk.Radiobutton(self.frame, text="Very Rare", variable=self.varRty, value="V", style='TRadiobutton').grid(sticky = "w", row=3, column=0)
        ttk.Radiobutton(self.frame, text="Legendary", variable=self.varRty, value="L", style='TRadiobutton').grid(sticky = "w", row=4, column=0)
        self.varRty.set("C")

