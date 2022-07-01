import tkinter as tk
from tkinter import ttk
from Data_Import import *


class Frame_Enchant_Table:
    def __init__(self, color, frame, program_data):
        self.edata = []
        self.edata.append(Data_Import.parse_dataset(program_data.enchantments['Enchantment_C'],';'))
        self.edata.append(Data_Import.parse_dataset(program_data.enchantments['Enchantment_U'],';'))
        self.edata.append(Data_Import.parse_dataset(program_data.enchantments['Enchantment_R'],';'))
        self.edata.append(Data_Import.parse_dataset(program_data.enchantments['Enchantment_V'],';'))
        self.edata.append(Data_Import.parse_dataset(program_data.enchantments['Enchantment_L'],';'))

        self.table_data = None
        self.etv = ttk.Treeview(frame, height=26)
        self.etv['columns'] = ("Rarity", "Name", "Description", "Attune", "Requirement")

        self.etv.column('#0', width=0, stretch="no")
        self.etv.column('Rarity', anchor="center", width=40)
        self.etv.column('Name', anchor="w", width=200)
        self.etv.column('Description', anchor="w", width=685)
        self.etv.column('Attune', anchor="center", width=42)
        self.etv.column('Requirement', anchor="w", width=200)
        
        self.etv.heading('#0', text='', anchor="center")
        self.etv.heading('Rarity', text='Rarity', anchor="center")
        self.etv.heading('Name', text='Name', anchor="center")
        self.etv.heading('Description', text='Description', anchor="center")
        self.etv.heading('Attune', text='Attune', anchor="center")
        self.etv.heading('Requirement', text='Requirement', anchor="center")
        self.etv.grid(row=0, column=0, pady=1)

        self.compile_table_data("all",None, None, None)
        

    def build_array(self, data):
        for i in range(len(data)):
            temp = []
            temp.append(data[i][0])
            temp.append(data[i][3])
            temp.append(data[i][4])
            temp.append(data[i][2])
            temp.append(data[i][5])
            self.table_data.append(temp)

    def compile_table_data(self, ftype, cb_rarity, cb_attune, cb_req):
        self.table_data = None
        self.table_data = []
        if ftype == "all":
            for i in range(len(self.edata)):
                self.build_array(self.edata[i])
        elif ftype == "rarity":
            for i in range(len(self.edata)):
                if cb_rarity[i].get() == True:
                    self.build_array(self.edata[i])
        elif ftype == "attune":
            if cb_attune[0].get() == True:
                for i in range(len(self.edata)):
                    for j in range(len(self.edata[i])):
                        if self.edata[i][j][2] == "Yes":
                            temp = []
                            temp.append(self.edata[i][j][0])
                            temp.append(self.edata[i][j][3])
                            temp.append(self.edata[i][j][4])
                            temp.append(self.edata[i][j][2])
                            temp.append(self.edata[i][j][5])
                            self.table_data.append(temp)
            if cb_attune[1].get() == True:
                for i in range(len(self.edata)):
                    for j in range(len(self.edata[i])):
                        if self.edata[i][j][2] == "No":
                            temp = []
                            temp.append(self.edata[i][j][0])
                            temp.append(self.edata[i][j][3])
                            temp.append(self.edata[i][j][4])
                            temp.append(self.edata[i][j][2])
                            temp.append(self.edata[i][j][5])
                            self.table_data.append(temp)
        elif ftype == "req":
            self.table_data.append(["tbd", "tbd", "tbd", "tbd", "tbd"])
        else:
            self.table_data.append(["error", "error", "error", "error", "error"])
        self.fill_table()
    
    def fill_table(self):
        for item in self.etv.get_children():
            self.etv.delete(item)
        for i in range(len(self.table_data)):
            self.etv.insert(parent='', index='end', iid=i, text='', values=(self.table_data[i][0],self.table_data[i][1],self.table_data[i][2],self.table_data[i][3],self.table_data[i][4]))
        
