import tkinter as tk
from tkinter import ttk

class Tab_Loot:
	def __init__(self, tab):
		self.tab = tab

		#self.tabGen = ttk.Frame(self.tab)
		self.tabGen = ttk.Frame(self.tab)
		



		#Left Frame and its contents

		tk.Label(self.tabGen, text="Instructions:").grid(row=0, column=0, padx=10, pady=2)


		# self.instruct = tk.Label(self.tabGen, text="1\n2\n2\n3\n4\n5\n6\n7\n8\n9\n")
		# self.instruct.grid(row=1, column=0, padx=10, pady=2)

		# tk.Label(self.tabGen, text="hello").grid(row=2, column=0, padx=10, pady=2)
