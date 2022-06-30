import tkinter as tk
from tkinter import ttk


class Frame_Filter:
    def __init__(self, color, frame):
        self.frame = frame
        # ttk.Label(self.frame, text="Filter").grid(row=0, column=0)

        self.var_filter_type = tk.StringVar()

        ttk.Radiobutton(self.frame, text="View All", variable=self.var_filter_type, value="all", style='TRadiobutton').grid(sticky = "w", row=0, column=0, pady=3)
        ttk.Radiobutton(self.frame, text="Rarity", variable=self.var_filter_type, value="rarity", style='TRadiobutton').grid(sticky = "w", row=1, column=0, pady=3)
        ttk.Radiobutton(self.frame, text="Attunement", variable=self.var_filter_type, value="attune", style='TRadiobutton').grid(sticky = "w", row=7, column=0, pady=3)
        ttk.Radiobutton(self.frame, text="Requirements", variable=self.var_filter_type, value="req", style='TRadiobutton').grid(sticky = "w", row=10, column=0, pady=3)
        self.var_filter_type.set(value="all")

        self.var_rarity_state = [tk.BooleanVar(value=True), tk.BooleanVar(value=True), tk.BooleanVar(value=True), tk.BooleanVar(value=True), tk.BooleanVar(value=True)]
        ttk.Checkbutton(self.frame, text="Common", variable=self.var_rarity_state[0], onvalue=1, offvalue=0).grid(sticky = "w", row=2, column=0, padx=(20,5), pady=3)
        ttk.Checkbutton(self.frame, text="Uncommon", variable=self.var_rarity_state[1], onvalue=1, offvalue=0).grid(sticky = "w", row=3, column=0, padx=(20,5), pady=3)
        ttk.Checkbutton(self.frame, text="Rare", variable=self.var_rarity_state[2], onvalue=1, offvalue=0).grid(sticky = "w", row=4, column=0, padx=(20,5), pady=3)
        ttk.Checkbutton(self.frame, text="Very Rare", variable=self.var_rarity_state[3], onvalue=1, offvalue=0).grid(sticky = "w", row=5, column=0, padx=(20,5), pady=3)
        ttk.Checkbutton(self.frame, text="Legendary", variable=self.var_rarity_state[4], onvalue=1, offvalue=0).grid(sticky = "w", row=6, column=0, padx=(20,5), pady=3)

        self.var_attune_state = [tk.BooleanVar(value=True), tk.BooleanVar(value=True)]
        ttk.Checkbutton(self.frame, text="Yes", variable=self.var_attune_state[0], onvalue=1, offvalue=0).grid(sticky = "w", row=8, column=0, padx=(20,5),pady=3)
        ttk.Checkbutton(self.frame, text="No", variable=self.var_attune_state[1], onvalue=1, offvalue=0).grid(sticky = "w", row=9, column=0, padx=(20,5),pady=3)

        self.var_req_state = [tk.BooleanVar(value=True), tk.BooleanVar(value=True), tk.BooleanVar(value=True)]
        ttk.Checkbutton(self.frame, text="Armors", variable=self.var_req_state[0], onvalue=1, offvalue=0).grid(sticky = "w", row=11, column=0, padx=(20,5),pady=3)
        ttk.Checkbutton(self.frame, text="Shields", variable=self.var_req_state[1], onvalue=1, offvalue=0).grid(sticky = "w", row=12, column=0, padx=(20,5),pady=3)
        ttk.Checkbutton(self.frame, text="Weapons", variable=self.var_req_state[2], onvalue=1, offvalue=0).grid(sticky = "w", row=13, column=0, padx=(20,5),pady=3)

        boarder1 = tk.Frame(self.frame, highlightcolor=color["label text"], highlightbackground=color["label text"], highlightthickness=2, bd=0, height=5, width=18)
        ttk.Button(boarder1, text="Apply Filter", state="normal", command = self.apply_filter).grid(row=0, column=0, sticky="nesw",ipady=15)
        boarder1.grid(row=14, column=0, sticky="nsew", padx=5, pady=15)


    def apply_filter(self):
        msg = msg + "----------\n"
        self.output.config(state="normal")
        self.output.insert('1.0', msg)    #'row.col' position
        self.output.config(state="disabled")
        self.output.see('1.0')