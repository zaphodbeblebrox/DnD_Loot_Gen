import tkinter as tk
from tkinter import ttk, font
from Tab_Enchantments import *
from Tab_Loot_Generator import *
# from Tab_Gem_Art import *

# this is fine, but for legibility I would recommend
# breaking every block you have in this class into its own function.
# generally you want to aspire for the Single Responsibility Principle,
# which says that a class or function should only be concerned with one thing.
#
# here the Core Window is concerned with the implementation of every sub-piece
# of window setup - instead create a new method for every code block you defined
# and have Core Window execute each one:
#
# def __init__(self, program_data):
#       self.color = get_color()
#       create_notebook_style()
#       create_label_style()
#       [...]
#
# this way Core Window init reads like a table of contents
# and each function it calls compartmentalizes and abstracts
# the implementation of that code
class Core_Window:
    def __init__(self, program_data):

        self.color = {
            "notebookbg":"#1a1a1a",
            "notebookfg":"#000000",
            "background":"#232323",
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
            "scrollbar":"#4d4d4d",
        }
        
        self.root = tk.Tk() #Makes the window
        self.root.title("Random Loot Generator")
        self.root.iconbitmap("dnd.ico")
        # self.root.geometry('1500x700')
        self.root.config(background = self.color['background'])

        # Create Notebook Style
        f = ('Segoe UI','10','bold')
        t = ('Segoe UI','10','normal')
        flabel = ('Segoe UI','16','underline')
        style = ttk.Style()
        style.theme_use('default')

        style.configure('TNotebook.Tab', background = self.color['untab'], foreground = self.color['notebookfg'], font=f, padding=(19,1))
        style.configure('TNotebook', borderwidth=0, background = self.color['notebookbg'])
        style.map('TNotebook.Tab', background = [('selected', self.color['background'])], foreground = [('selected', self.color['label text'])])
        
         # Label Style
        style.configure('TLabel', font = flabel, padx=0, pady=0, background=self.color['background'], foreground=self.color['selected'], 
                        height=4, width=5, focuscolor=self.color['button'], justify ="center")

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

        #  Scrollbar Style 
        style.configure('Vertical.TScrollbar', arrowcolor=self.color["selected"], background=self.color["scrollbar"], 
                        bordercolor=self.color['disabled'], troughcolor=self.color["background"], borderwidth=0)
        style.map('Vertical.TScrollbar',
            foreground = [('disabled', self.color["disabled"]),
                      ('pressed', self.color["scrollbar"]),
                      ('active', self.color["highlight"])],
            background = [('disabled', self.color["background"]),
                      ('pressed', '!focus', self.color["background"]),
                      ('active', self.color["background"])],
            indicatorcolor=[('selected', self.color["scrollbar"]),
                          ('pressed', self.color["scrollbar"])]
          )

        #  Treeview Style
        style.configure('Treeview', foreground=self.color["txt fg"], background=self.color["txt bg"], 
                        indicatorcolor=self.color["not selected"], focuscolor=self.color["background"], font=t,
                        fieldbackground=self.color["txt bg"])
        style.map('Treeview',
            foreground = [('disabled', self.color["disabled"]),
                        ('pressed', self.color["pressed"]),
                        ('active', self.color["highlight"])],
            background = [('disabled', self.color["background"]),
                        ('pressed', '!focus', self.color["background"]),
                        ('active', self.color["background"])],
            indicatorcolor=[('selected', self.color["selected"]),
                        ('pressed', self.color["selected"])]
          )
        style.configure('Treeview.Heading', foreground=self.color["txt fg"], background=self.color["txt bg"], 
                        indicatorcolor=self.color["not selected"], focuscolor=self.color["background"], font=t)
        style.map('Treeview.Heading',
            foreground = [('disabled', self.color["disabled"]),
                        ('pressed', self.color["pressed"]),
                        ('active', self.color["highlight"])],
            background = [('disabled', self.color["background"]),
                        ('pressed', '!focus', self.color["background"]),
                        ('active', self.color["background"])],
            indicatorcolor=[('selected', self.color["selected"]),
                        ('pressed', self.color["selected"])]
          )

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
        self.notebook.add(self.tabGems, text="Gem & Art Table")
        self.notebook.add(self.tabMagic, text="Magic Reference")
        self.notebook.add(self.tabStatusEffects, text="Status Effects")
        self.notebook.add(self.tag_definitions, text="Tag Definitions")
        self.notebook.grid(row=0, column=0)

        Tab_Loot_Generator(self.color, self.tabGen, program_data)
        Tab_Enchantments(self.color, self.tabEnchantment, program_data)
        # Tab_Gem_Art(self.color, self.tabEnchantment, program_data)

    def start(self):
        self.root.mainloop() #start monitoring and updating the GUI