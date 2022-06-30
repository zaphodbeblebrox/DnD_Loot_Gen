import tkinter as tk
from tkinter import ttk


class Frame_Enchant_Table:
    def __init__(self, color, frame, program_data):
        self.edata = program_data.enchantments
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
        self.fill_table()


        

    def compile_table_data(self, ftype, cb_rarity, cb_attune, cb_req):
        pass
    
    def fill_table(self):
        self.etv.insert(parent='', index=0, iid=0, text='', values=('1','Vineet','Alpha','Yes'))
        self.etv.insert(parent='', index=1, iid=1, text='', values=('2','Anil','Bravo','No'))
        self.etv.insert(parent='', index=2, iid=2, text='', values=('3','Vinod','Charlie','Yes'))
        self.etv.insert(parent='', index=3, iid=3, text='', values=('4','Vimal','Delta','Yes'))
        self.etv.insert(parent='', index=4, iid=4, text='', values=('5','Manjeet','Echo','Yes'))
