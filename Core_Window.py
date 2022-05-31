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
            "pink":"#e22b65",
            "cyan":"#00c7b0", 
            "neon pink":"#FF10F0"
        }
        
        self.root = tk.Tk() #Makes the window
        self.root.title("Random Loot Generator") #Makes the title that will appear in the top left
        # photo = tk.PhotoImage(file = "dnd.ico")
        self.root.iconbitmap("dnd.ico")
        # self.root.geometry('1500x700')
        self.root.config(background = self.color['dark gray'])

        # Create Notebook Style
        f = font.Font(weight = "bold", size= 10)
        style = ttk.Style()
        style.theme_use('default')
        style.configure('TNotebook.Tab', background = self.color['purple'], foreground = self.color['white'], font=('Segoe UI','10','bold'))
        style.configure('TNotebook', borderwidth=0)
        style.map('TNotebook.Tab', background = [('selected', self.color['dark gray'])], foreground = [('selected', self.color['pink'])])
        
        # Button Style
        style.configure('W.TButton', font = f, padx=0, pady=0, background=self.color['purple'], foreground=self.color['white'], height=5, width=18, focuscolor=self.color['purple'], justify ="center")
        style.map('W.TButton', background = [('selected', self.color['black'])], foreground = [('selected', self.color['pink'])])
        
        # Radio Button Style
        style.configure('TRadiobutton', foreground=self.color["cyan"], background=self.color["dark gray"], indicatorcolor=self.color["white"], font=f)
        style.map('TRadiobutton',
            foreground = [('disabled', self.color["pink"]),
                      ('pressed', self.color["pink"]),
                      ('active', self.color["light gray"])],
            background = [('disabled', self.color["dark gray"]),
                      ('pressed', '!focus', self.color["dark gray"]),
                      ('active', self.color["dark gray"])],
            indicatorcolor=[('selected', self.color["pink"]),
                          ('pressed', self.color["pink"])]
          )
        
        #  Check Box Style 
        style.configure('TCheckbutton', foreground=self.color["cyan"], background=self.color["dark gray"], indicatorcolor=self.color["white"], font=f, focuscolor=self.color['dark gray'])
        style.map('TCheckbutton',
            foreground = [('disabled', self.color["pink"]),
                      ('pressed', self.color["pink"]),
                      ('active', self.color["light gray"])],
            background = [('disabled', self.color["dark gray"]),
                      ('pressed', '!focus', self.color["dark gray"]),
                      ('active', self.color["dark gray"])],
            indicatorcolor=[('selected', self.color["pink"]),
                          ('pressed', self.color["pink"])]
          )

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