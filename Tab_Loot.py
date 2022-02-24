import tkinter as tk
from tkinter import ttk
from Frame_Level import *

class Tab_Loot:
	
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

		Frame_Level(self.fGen2)

		# fGen2-----------------------
		# self.rLvl1 = tk.Radiobutton(self.fGen2, text="Level 1", variable=self.varLvl, value=1, command=self.sel)
		# self.rLvl2 = tk.Radiobutton(self.fGen2, text="Level 2", variable=self.varLvl, value=2, command=self.sel)
		# self.rLvl3 = tk.Radiobutton(self.fGen2, text="Level 3", variable=self.varLvl, value=3, command=self.sel)
		# self.rLvl4 = tk.Radiobutton(self.fGen2, text="Level 4", variable=self.varLvl, value=4, command=self.sel)
		# self.rLvl5 = tk.Radiobutton(self.fGen2, text="Level 5", variable=self.varLvl, value=5, command=self.sel)
		# self.rLvl6 = tk.Radiobutton(self.fGen2, text="Level 6", variable=self.varLvl, value=6, command=self.sel)
		# self.rLvl7 = tk.Radiobutton(self.fGen2, text="Level 7", variable=self.varLvl, value=7, command=self.sel)
		# self.rLvl8 = tk.Radiobutton(self.fGen2, text="Level 8", variable=self.varLvl, value=8, command=self.sel)
		# self.rLvl9 = tk.Radiobutton(self.fGen2, text="Level 9", variable=self.varLvl, value=9, command=self.sel)
		# self.rLvl10 = tk.Radiobutton(self.fGen2, text="Level 10", variable=self.varLvl, value=10, command=self.sel)
		# self.rLvl11 = tk.Radiobutton(self.fGen2, text="Level 11", variable=self.varLvl, value=11, command=self.sel)
		# self.rLvl12 = tk.Radiobutton(self.fGen2, text="Level 12", variable=self.varLvl, value=12, command=self.sel)
		# self.rLvl13 = tk.Radiobutton(self.fGen2, text="Level 13", variable=self.varLvl, value=13, command=self.sel)
		# self.rLvl14 = tk.Radiobutton(self.fGen2, text="Level 14", variable=self.varLvl, value=14, command=self.sel)
		# self.rLvl15 = tk.Radiobutton(self.fGen2, text="Level 15", variable=self.varLvl, value=15, command=self.sel)
		# self.rLvl16 = tk.Radiobutton(self.fGen2, text="Level 16", variable=self.varLvl, value=16, command=self.sel)
		# self.rLvl17 = tk.Radiobutton(self.fGen2, text="Level 17", variable=self.varLvl, value=17, command=self.sel)
		# self.rLvl18 = tk.Radiobutton(self.fGen2, text="Level 18", variable=self.varLvl, value=18, command=self.sel)
		# self.rLvl19 = tk.Radiobutton(self.fGen2, text="Level 19", variable=self.varLvl, value=19, command=self.sel)
		# self.rLvl20 = tk.Radiobutton(self.fGen2, text="Level 20", variable=self.varLvl, value=20, command=self.sel)
		# self.rLvlLabel = tk.Label(self.fGen2)

		# self.varLvl.set(1)

		# self.rLvl1.grid(sticky = "w", row=0, column=0)
		# self.rLvl2.grid(sticky = "w", row=1, column=0)
		# self.rLvl3.grid(sticky = "w", row=2, column=0)
		# self.rLvl4.grid(sticky = "w", row=3, column=0)
		# self.rLvl5.grid(sticky = "w", row=4, column=0)
		# self.rLvl6.grid(sticky = "w", row=5, column=0)
		# self.rLvl7.grid(sticky = "w", row=6, column=0)
		# self.rLvl8.grid(sticky = "w", row=7, column=0)
		# self.rLvl9.grid(sticky = "w", row=8, column=0)
		# self.rLvl10.grid(sticky = "w", row=9, column=0)
		# self.rLvl11.grid(sticky = "w", row=10, column=0)
		# self.rLvl12.grid(sticky = "w", row=11, column=0)
		# self.rLvl13.grid(sticky = "w", row=12, column=0)
		# self.rLvl14.grid(sticky = "w", row=13, column=0)
		# self.rLvl15.grid(sticky = "w", row=14, column=0)
		# self.rLvl16.grid(sticky = "w", row=15, column=0)
		# self.rLvl17.grid(sticky = "w", row=16, column=0)
		# self.rLvl18.grid(sticky = "w", row=17, column=0)
		# self.rLvl19.grid(sticky = "w", row=18, column=0)
		# self.rLvl20.grid(sticky = "w", row=19, column=0)
		# self.rLvlLabel.grid(sticky = "w", row=20, column=0)

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
