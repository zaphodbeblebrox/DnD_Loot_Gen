from logging import root
import tkinter as tk
from tkinter import ttk
from Frame_Level import *
from Frame_Rarity import *
from Frame_ItemTypes import *
from Frame_Gen_Buttons import *
from Frame_Output import *
from Data_Import import *

class Tab_Loot_Generator:
	
	def __init__(self, tab, programData):
		self.tab = tab

		# Generator Frame Definitions----------

		self.frameGen = tk.LabelFrame(self.tab, text="Loot Generator Frame", padx=5, pady=5)
		#frameGen.config(bg="#3b3b3b")
		self.frameGen.grid(row=0, column=0)

		self.fGen1 = tk.LabelFrame(self.frameGen, text="Generator Output", padx=5, pady=5)
		self.fGen2 = tk.LabelFrame(self.frameGen, text="Loot Level", padx=5, pady=5)
		self.fGen3 = tk.LabelFrame(self.frameGen, text="Type of Generation", padx=5, pady=5)
		self.fGen4 = tk.LabelFrame(self.frameGen, text="Item Rarity", padx=5, pady=5)
		self.fGen5 = tk.LabelFrame(self.frameGen, text="Item Types", padx=5, pady=5)

		self.fGen1.grid(row=0, column=0, sticky="nsew")
		self.fGen2.grid(row=0, column=1, sticky="nsew")
		self.fGen3.grid(row=0, column=2, sticky="nsew")
		self.fGen4.grid(row=0, column=3, sticky="nsew")
		self.fGen5.grid(row=0, column=4, sticky="nsew")

		self.textbox = Frame_Output(self.fGen1)
		self.levelCtrl = Frame_Level(self.fGen2, 20)
		self.rarityCtrl = Frame_Rarity(self.fGen4)

		self.itCtrl = Frame_ItemTypes(self.fGen5, programData.itemTypeList)
		self.buttons = Frame_Gen_Buttons(self.fGen3, programData,  self.textbox, self.levelCtrl, self.rarityCtrl, self.itCtrl)


		



	# Functions-------------------
	def sel(self):
		selection = "Option " + str(self.varLvl.get())
		self.rLvlLabel.config(text = selection)

	# def selRty(self):
	# 	selection = "Option " + str(self.varRty.get())
	# 	self.rRtyLabel.config(text = selection)

	# def myClick(self):
	# 	self.myLabel3 = tk.Label(fGen3, text="done")
	# 	self.myLabel3.grid(row=10, column=0)
