import tkinter as tk
from tkinter import ttk

from Tab_Loot_Generator import *
# from MyRightPanel import *

class Core_Window:
	def __init__(self):

		self.root = tk.Tk() #Makes the window
		self.root.title("Random Loot Generator") #Makes the title that will appear in the top left
		# self.root.geometry('1500x700')
		#self.root.config(background = "#FFFFFF")

		# Tab Definitions
		self.notebook = ttk.Notebook(self.root)

		self.tabGen = ttk.Frame(self.notebook)
		self.tabEnchantment = ttk.Frame(self.notebook)
		self.tabGems = ttk.Frame(self.notebook)
		self.tabMagic = ttk.Frame(self.notebook)
		self.tabStatusEffects = ttk.Frame(self.notebook)

		self.notebook.add(self.tabGen, text="Loot Generator")
		self.notebook.add(self.tabEnchantment, text="Enchantments")
		self.notebook.add(self.tabGems, text="Gem Table")
		self.notebook.add(self.tabMagic, text="Magic Reference")
		self.notebook.add(self.tabStatusEffects, text="Status Effects")
		self.notebook.grid(row=0, column=0)

		Tab_Loot_Generator(self.tabGen)
		Tab_Loot_Generator(self.tabEnchantment)

	def start(self):
		self.root.mainloop() #start monitoring and updating the GUI