import tkinter as tk
from tkinter import ttk, font

from Tab_Loot_Generator import *
# from MyRightPanel import *

class Core_Window:
    def __init__(self, data):

        self.color = {
            "background":"#232323",
            "notebookbg":"#1a1a1a",
            "button":"#333333",
            "untab":"#BB86FC",
            "selected":"#FFDD03",
            "not selected":"#333333",
            "header":"#FFDD00",
            "label text":"#BB86FC",
            "pressed":"#D3D3D3",
            "txt bg":"#232323",
            "txt fg":"#ffffff",
            "highlight":"#D3D3D3",
            "disabled":"#FF9494",



            "dark gray":"#232323",
            "teal":"#03DAC5",
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
        self.root.title("Random Loot Generator")
        self.root.iconbitmap("dnd.ico")
        # self.root.geometry('1500x700')
        self.root.config(background = self.color['background'])

        # Create Notebook Style
        f = font.Font(weight = "bold", size= 10)
        style = ttk.Style()
        style.theme_use('default')
        style.configure('TNotebook.Tab', background = self.color['untab'], foreground = self.color['black'], font=('Segoe UI','10','bold'), padding=(19,1))
        style.configure('TNotebook', borderwidth=0, background = self.color['notebookbg'])
        style.map('TNotebook.Tab', background = [('selected', self.color['background'])], foreground = [('selected', self.color['label text'])])
        
        # Button Style
        style.configure('TButton', font = f, padx=0, pady=0, background=self.color['button'], foreground=self.color['label text'], 
                        height=4, width=18, focuscolor=self.color['button'], justify ="center")
        style.map('TButton', 
            foreground = [('disabled', self.color["disabled"]),
                        ('pressed', self.color["label text"]),
                        ('selected', self.color['label text'])], 
            background = [('disabled', self.color["button"]),
                        ('pressed', self.color["button"]),
                        ('active', self.color["button"])])
        
        # Radio Button Style
        style.configure('TRadiobutton', foreground=self.color["label text"], background=self.color["background"], 
                        indicatorcolor=self.color["not selected"], focuscolor=self.color["background"], font=f)
        style.map('TRadiobutton',
            foreground = [('disabled', self.color["disabled"]),
                        ('pressed', self.color["pressed"]),
                        ('active', self.color["highlight"])],
            background = [('disabled', self.color["background"]),
                        ('pressed', '!focus', self.color["background"]),
                        ('active', self.color["background"])],
            indicatorcolor=[('selected', self.color["selected"]),
                        ('pressed', self.color["selected"])]
          )
        
        #  Check Box Style 
        style.configure('TCheckbutton', foreground=self.color["label text"], background=self.color["background"], 
                        indicatorcolor=self.color["not selected"], font=f, focuscolor=self.color['background'])
        style.map('TCheckbutton',
            foreground = [('disabled', self.color["disabled"]),
                      ('pressed', self.color["pressed"]),
                      ('active', self.color["highlight"])],
            background = [('disabled', self.color["background"]),
                      ('pressed', '!focus', self.color["background"]),
                      ('active', self.color["background"])],
            indicatorcolor=[('selected', self.color["selected"]),
                          ('pressed', self.color["selected"])]
          )

        #Create Frame Style
        # style.configure('TFrame', background = self.color['background'], foreground = self.color['white'], font=('Segoe UI','19','bold'))
        # style.map('TFrame', background = [('selected', self.color['black'])], foreground = [('selected', self.color['pink'])])

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