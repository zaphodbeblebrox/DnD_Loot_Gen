import tkinter as tk
from tkinter import ttk

from Tab_Loot_Generator import *
# from MyRightPanel import *

class Core_Window:
    def __init__(self, data):

        self.color = {
            "dark gray":"#232323",
            "light gray":"#D3D3D3",
            "purple":"#8336a8",
            "red":"#eb111e",
            "white":"#ffffff", 
            "black":"#000000",
            "near black":"#111011",
            "pink":"#cc83b8",
            "cyan":"#00c7b0", 
            "neon pink":"#FF10F0"
        }
        
        self.root = tk.Tk() #Makes the window
        self.root.title("Random Loot Generator") #Makes the title that will appear in the top left
        # self.root.geometry('1500x700')
        self.root.config(background = self.color['dark gray'])

        # Create Notebook Style
        style = ttk.Style()
        style.theme_use('default')
        style.configure('TNotebook.Tab', background = self.color['purple'], foreground = self.color['white'])
        style.configure('TNotebook', borderwidth=0)
        style.map('TNotebook.Tab', background = [('selected', self.color['dark gray'])], foreground = [('selected', self.color['red'])])

        #Create Frame Style
        style.configure('TFrame', background = self.color['dark gray'])

        # Tab Definitions
        self.notebook = ttk.Notebook(self.root)

        self.tabGen = ttk.Frame(self.notebook)
        self.tabEnchantment = ttk.Frame(self.notebook)
        self.tabGems = ttk.Frame(self.notebook)
        self.tabMagic = ttk.Frame(self.notebook)
        self.tabStatusEffects = ttk.Frame(self.notebook)
        self.tag_definitions = ttk.Frame(self.notebook)

        self.notebook.add(self.tabGen, text="Loot Generator")
        self.notebook.add(self.tabEnchantment, text="Enchantments")
        self.notebook.add(self.tabGems, text="Gem Table")
        self.notebook.add(self.tabMagic, text="Magic Reference")
        self.notebook.add(self.tabStatusEffects, text="Status Effects")
        self.notebook.add(self.tag_definitions, text="Tag Definitions")
        self.notebook.grid(row=0, column=0)

        Tab_Loot_Generator(self.color, self.tabGen, data)
        Tab_Loot_Generator(self.color, self.tabEnchantment, data)

    def start(self):
        self.root.mainloop() #start monitoring and updating the GUI