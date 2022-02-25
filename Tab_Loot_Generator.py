import tkinter as tk
from tkinter import ttk
from Frame_Level import *
from Frame_rec import *

class Tab_Loot_Generator:
	
	def __init__(self, tab):
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

		# Global Variables-----------
		#self.varLvl = tk.IntVar()
		self.varRty = tk.StringVar()
		self.vArmorB = tk.BooleanVar()
		self.vArmorM = tk.BooleanVar()
		self.vPotion = tk.BooleanVar()
		self.vRing = tk.BooleanVar()
		self.vRod = tk.BooleanVar()
		self.vScroll = tk.BooleanVar()
		self.vStaff = tk.BooleanVar()
		self.vWand = tk.BooleanVar()
		self.vWeaponB = tk.BooleanVar()
		self.vWeaponM = tk.BooleanVar()
		self.vWonderous = tk.BooleanVar()

		# fGen1-----------------------
		msg = """hello worlds!!"""
		self.conOut = tk.Text(self.fGen1, height = 32, width = 52, state="normal")
		self.conOut.insert("insert", msg)
		self.conOut.insert("end", "hellow")
		self.conOut.config(state="disabled")
		self.conOut.grid(row=0, column=0)

		Frame_rec(self.fGen2, 20)
		Frame_rec(self.fGen3, 9)



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
