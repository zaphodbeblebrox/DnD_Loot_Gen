import tkinter as tk
from tkinter import ttk
from Data_Import import *

import textwrap


class Frame_Gem_Art_Table:
    def __init__(self, color, frame, program_data):
        self.gdata = []
        self.gdata.append(Data_Import.parse_dataset(program_data.tags['GEMS_10'],';'))
        self.gdata.append(Data_Import.parse_dataset(program_data.tags['GEMS_100'],';'))
        self.gdata.append(Data_Import.parse_dataset(program_data.tags['GEMS_1000'],';'))
        self.gdata.append(Data_Import.parse_dataset(program_data.tags['GEMS_50'],';'))
        self.gdata.append(Data_Import.parse_dataset(program_data.tags['GEMS_500'],';'))
        self.gdata.append(Data_Import.parse_dataset(program_data.tags['GEMS_5000'],';'))

        self.adata = []
        self.adata.append(Data_Import.parse_dataset(program_data.tags['ART_25'],';'))
        self.adata.append(Data_Import.parse_dataset(program_data.tags['ART_250'],';'))
        self.adata.append(Data_Import.parse_dataset(program_data.tags['ART_2500'],';'))
        self.adata.append(Data_Import.parse_dataset(program_data.tags['ART_750'],';'))
        self.adata.append(Data_Import.parse_dataset(program_data.tags['ART_7500'],';'))

        self.table_data = None
        self.gatv = ttk.Treeview(frame, height=26)
        self.gatv['columns'] = ("Name", "Value", "Description")

        self.gatv_scrollbar = ttk.Scrollbar(frame)
        self.gatv_scrollbar.grid(row=0, column=1, sticky="nesw")
        self.gatv_scrollbar.config(command=self.gatv.yview)
        self.gatv.configure(yscrollcommand=self.gatv_scrollbar.set)

        self.gatv.column('#0', width=0, stretch="no")
        self.gatv.column('Name', anchor="center", width=40)
        self.gatv.column('Value', anchor="w", width=200)
        self.gatv.column('Description', anchor="w", width=685)
        
        self.gatv.heading('#0', text='', anchor="center")
        self.gatv.heading('Name', text='Name', anchor="center")
        self.gatv.heading('Value', text='Value', anchor="center")
        self.gatv.heading('Description', text='Description', anchor="center")

        self.gatv.grid(row=0, column=0, pady=1)

        self.compile_table_data("all",None, None, None)
    
    def wrap(self, string, length=125):
        return '\n'.join(textwrap.wrap(string, length))

    def build_array(self, data):
        for i in range(len(data)):
            self.add_array_element(data[i])

    def add_array_element(self, data):
        temp = []
        temp.append(data[0])
        temp.append(data[3])
        temp.append(data[4])
        temp.append(data[2])
        temp.append(data[5])
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
            for i in range(len(self.edata)):
                for j in range(len(self.edata[i])):                 
                    if self.edata[i][j][2] == "Yes" and cb_attune[0].get() == True:
                        self.add_array_element(self.edata[i][j])
                    elif self.edata[i][j][2] == "No" and cb_attune[1].get() == True:
                        self.add_array_element(self.edata[i][j])
        elif ftype == "req":
            for i in range(len(self.edata)):
                for j in range(len(self.edata[i])):                 
                    if self.edata[i][j][5] == "ANY":
                        self.add_array_element(self.edata[i][j])
                    elif "ARMOR" in self.edata[i][j][5] and cb_req[0].get() == True:
                        self.add_array_element(self.edata[i][j])
                    elif "SHIELD" in self.edata[i][j][5] and cb_req[1].get() == True:
                        self.add_array_element(self.edata[i][j])
                    elif "WEAPON" in self.edata[i][j][5] and cb_req[2].get() == True:
                        self.add_array_element(self.edata[i][j])
        else:
            self.table_data.append(["error", "error", "error", "error", "error"])
        self.fill_table()
    
    def fill_table(self):
        for item in self.etv.get_children():
            self.etv.delete(item)
        for i in range(len(self.table_data)):
            self.etv.insert(parent='', index='end', iid=i, text='', 
                            values=(self.table_data[i][0],
                                    self.table_data[i][1],
                                    self.wrap(self.table_data[i][2]),
                                    self.table_data[i][3],
                                    self.table_data[i][4]))
        