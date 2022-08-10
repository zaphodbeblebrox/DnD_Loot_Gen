from logging import root
import tkinter as tk
from tkinter import font, ttk
from Frame_Gem_Art_Table import *
from Frame_GA_Filter import *

class Tab_Gem_Art:
    
    def __init__(self, color, tab, program_data):
        self.tab = tab
        self.color = color

        f = font.Font(weight = "bold", size= 10)

        # Generator Frame Definitions----------

        self.f_main = tk.LabelFrame(self.tab, bd=0, padx=5, pady=5, bg=self.color['background'])
        self.f_main.grid(row=0, column=0)

        self.f_table = tk.LabelFrame(self.f_main, text="Gem & Art Table", padx=5, pady=5, bg=self.color['background'], fg=self.color['header'], font=f)
        self.f_filter = tk.LabelFrame(self.f_main, text="Filter", padx=5, pady=5, bg=self.color['background'], fg=self.color['header'], font=f)

        self.f_table.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.f_filter.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        self.et = Frame_Gem_Art_Table(color, self.f_table, program_data)
        self.fs = Frame_GA_Filter(color, self.f_filter,self.et)
        # self.textbox = Frame_Output(self.color,self.fGen1)
        # self.levelCtrl = Frame_Level(self.color, self.fGen2, 20)
        # self.rarityCtrl = Frame_Rarity(self.color, self.fGen4)

        # self.itCtrl = Frame_ItemTypes(self.color, self.fGen5, program_data.itemTypeList)
        # self.buttons = Frame_Gen_Buttons(self.color, self.fGen3, program_data,  self.textbox, self.levelCtrl, self.rarityCtrl, self.itCtrl)

