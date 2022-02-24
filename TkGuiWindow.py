import tkinter as tk
from tkinter import ttk

from Tab_Loot import *
# from MyRightPanel import *

class TkGuiWindow:
	def __init__(self):

		self.root = tk.Tk() #Makes the window
		self.root.title("Window Title") #Makes the title that will appear in the top left
		self.root.config(background = "#FFFFFF")

		# Tab Definitions
		self.notebook = ttk.Notebook(self.root)
		self.tabGen = Tab_Loot(self.notebook)
		
		self.notebook.add(self.tabGen, text="Loot Generator")
		self.notebook.add(self.tabGen, text="hello")
		self.notebook.grid(row=0, column=0)

		#self.leftPanel = MyLeftPanel(self.root, self.leftFrame)
		#self.rightPanel = MyRightPanel(self.root, self.rightFrame)

	def start(self):
		self.root.mainloop() #start monitoring and updating the GUI