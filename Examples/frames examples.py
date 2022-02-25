import tkinter as tk
from tkinter import ttk

# Example for breaking up into multiple files
# https://robotic-controls.com/learn/python-guis/python-gui-broken-multiple-files

# App Definitions
root = tk.Tk()
#root.geometry('1500x700')
root.title("Random Loot Generator")
#root.config(bg="#3b3b3b")


# Tab Definitions
tabRoot = ttk.Notebook(root)

tabGen = ttk.Frame(tabRoot)
tabEnchantment = ttk.Frame(tabRoot)
tabGems = ttk.Frame(tabRoot)
tabMagic = ttk.Frame(tabRoot)
tabStatusEffects = ttk.Frame(tabRoot)

tabRoot.add(tabGen, text="Loot Generator")
tabRoot.add(tabEnchantment, text="Enchantments")
tabRoot.add(tabGems, text="Gem Table")
tabRoot.add(tabMagic, text="Magic Reference")
tabRoot.add(tabStatusEffects, text="Status Effects")

tabRoot.grid(row=0, column=0)

# Global Variables-----------
varLvl = tk.IntVar()
varRty = tk.StringVar()
vArmorB = tk.BooleanVar()
vArmorM = tk.BooleanVar()
vPotion = tk.BooleanVar()
vRing = tk.BooleanVar()
vRod = tk.BooleanVar()
vScroll = tk.BooleanVar()
vStaff = tk.BooleanVar()
vWand = tk.BooleanVar()
vWeaponB = tk.BooleanVar()
vWeaponM = tk.BooleanVar()
vWonderous = tk.BooleanVar()

# Generator Frame Definitions----------

frameGen = tk.LabelFrame(tabGen, text="Loot Generator Frame", padx=5, pady=5)
#frameGen.config(bg="#3b3b3b")
frameGen.grid(row=0, column=0)

fGen1 = tk.LabelFrame(frameGen, text="Generator Output", padx=5, pady=5)
fGen2 = tk.LabelFrame(frameGen, text="Loot Level", padx=5, pady=5)
fGen3 = tk.LabelFrame(frameGen, text="Type of Generation", padx=5, pady=5)
fGen4 = tk.LabelFrame(frameGen, text="Item Rarity", padx=5, pady=5)
fGen5 = tk.LabelFrame(frameGen, text="Item Types", padx=5, pady=5)

fGen1.grid(row=0, column=0, sticky="nsew")
fGen2.grid(row=0, column=1, sticky="nsew")
fGen3.grid(row=0, column=2, sticky="nsew")
fGen4.grid(row=0, column=3, sticky="nsew")
fGen5.grid(row=0, column=4, sticky="nsew")

# Functions-------------------
def sel():
   selection = "Option " + str(varLvl.get())
   rLvlLabel.config(text = selection)

def selRty():
   selection = "Option " + str(varRty.get())
   rRtyLabel.config(text = selection)

def myClick():
    myLabel3 = tk.Label(fGen3, text="done")
    myLabel3.grid(row=10, column=0)

# fGen1-----------------------
msg = """hello worlds!!"""
conOut = tk.Text(fGen1, height = 32, width = 52, state="normal")
conOut.insert("insert", msg)
conOut.insert("end", "hellow")
conOut.config(state="disabled")
conOut.grid(row=0, column=0)

# fGen2-----------------------
rLvl1 = tk.Radiobutton(fGen2, text="Level 1", variable=varLvl, value=1, command=sel)
rLvl2 = tk.Radiobutton(fGen2, text="Level 2", variable=varLvl, value=2, command=sel)
rLvl3 = tk.Radiobutton(fGen2, text="Level 3", variable=varLvl, value=3, command=sel)
rLvl4 = tk.Radiobutton(fGen2, text="Level 4", variable=varLvl, value=4, command=sel)
rLvl5 = tk.Radiobutton(fGen2, text="Level 5", variable=varLvl, value=5, command=sel)
rLvl6 = tk.Radiobutton(fGen2, text="Level 6", variable=varLvl, value=6, command=sel)
rLvl7 = tk.Radiobutton(fGen2, text="Level 7", variable=varLvl, value=7, command=sel)
rLvl8 = tk.Radiobutton(fGen2, text="Level 8", variable=varLvl, value=8, command=sel)
rLvl9 = tk.Radiobutton(fGen2, text="Level 9", variable=varLvl, value=9, command=sel)
rLvl10 = tk.Radiobutton(fGen2, text="Level 10", variable=varLvl, value=10, command=sel)
rLvl11 = tk.Radiobutton(fGen2, text="Level 11", variable=varLvl, value=11, command=sel)
rLvl12 = tk.Radiobutton(fGen2, text="Level 12", variable=varLvl, value=12, command=sel)
rLvl13 = tk.Radiobutton(fGen2, text="Level 13", variable=varLvl, value=13, command=sel)
rLvl14 = tk.Radiobutton(fGen2, text="Level 14", variable=varLvl, value=14, command=sel)
rLvl15 = tk.Radiobutton(fGen2, text="Level 15", variable=varLvl, value=15, command=sel)
rLvl16 = tk.Radiobutton(fGen2, text="Level 16", variable=varLvl, value=16, command=sel)
rLvl17 = tk.Radiobutton(fGen2, text="Level 17", variable=varLvl, value=17, command=sel)
rLvl18 = tk.Radiobutton(fGen2, text="Level 18", variable=varLvl, value=18, command=sel)
rLvl19 = tk.Radiobutton(fGen2, text="Level 19", variable=varLvl, value=19, command=sel)
rLvl20 = tk.Radiobutton(fGen2, text="Level 20", variable=varLvl, value=20, command=sel)
rLvlLabel = tk.Label(fGen2)

varLvl.set(1)

rLvl1.grid(sticky = "w", row=0, column=0)
rLvl2.grid(sticky = "w", row=1, column=0)
rLvl3.grid(sticky = "w", row=2, column=0)
rLvl4.grid(sticky = "w", row=3, column=0)
rLvl5.grid(sticky = "w", row=4, column=0)
rLvl6.grid(sticky = "w", row=5, column=0)
rLvl7.grid(sticky = "w", row=6, column=0)
rLvl8.grid(sticky = "w", row=7, column=0)
rLvl9.grid(sticky = "w", row=8, column=0)
rLvl10.grid(sticky = "w", row=9, column=0)
rLvl11.grid(sticky = "w", row=10, column=0)
rLvl12.grid(sticky = "w", row=11, column=0)
rLvl13.grid(sticky = "w", row=12, column=0)
rLvl14.grid(sticky = "w", row=13, column=0)
rLvl15.grid(sticky = "w", row=14, column=0)
rLvl16.grid(sticky = "w", row=15, column=0)
rLvl17.grid(sticky = "w", row=16, column=0)
rLvl18.grid(sticky = "w", row=17, column=0)
rLvl19.grid(sticky = "w", row=18, column=0)
rLvl20.grid(sticky = "w", row=19, column=0)
rLvlLabel.grid(sticky = "w", row=20, column=0)

# fGen3-----------------------
bGen1 = tk.Button(fGen3, text="Individual Treasure", state="normal", padx=15, pady=35, command = myClick, bg="green")
bGen2 = tk.Button(fGen3, text="Horde Treasure", state="normal", padx=15, pady=35, command = myClick, bg="green")
bGen3 = tk.Button(fGen3, text="Weapon Drop", state="normal", padx=15, pady=35, command = myClick, bg="green")
bGen4 = tk.Button(fGen3, text="Magic Item Drop", state="normal", padx=15, pady=35, command = myClick, bg="green")

bGen1.grid(row=0, column=0, sticky="ew")
bGen2.grid(row=1, column=0, sticky="ew")
bGen3.grid(row=2, column=0, sticky="ew")
bGen4.grid(row=3, column=0, sticky="ew")

# fGen4-----------------------
subFGen4 = tk.LabelFrame(fGen4, padx=5, pady=5)
subFGen4.grid(row=0, column=0, sticky="nsew")

rRty1 = tk.Radiobutton(subFGen4, text="Common", variable=varRty, value="C", command=selRty)
rRty2 = tk.Radiobutton(subFGen4, text="Uncommon", variable=varRty, value="U", command=selRty)
rRty3 = tk.Radiobutton(subFGen4, text="Rare", variable=varRty, value="R", command=selRty)
rRty4 = tk.Radiobutton(subFGen4, text="Very Rare", variable=varRty, value="V", command=selRty)
rRty5 = tk.Radiobutton(subFGen4, text="Legendary", variable=varRty, value="L", command=selRty)
bRty1 = tk.Button(fGen4, text="Roll Item", state="normal", padx=15, pady=35, command = myClick, bg="gold")
rRtyLabel = tk.Label(subFGen4)

varRty.set("C")

rRty1.grid(sticky = "w", row=0, column=0)
rRty2.grid(sticky = "w", row=1, column=0)
rRty3.grid(sticky = "w", row=2, column=0)
rRty4.grid(sticky = "w", row=3, column=0)
rRty5.grid(sticky = "w", row=4, column=0)
bRty1.grid(row=1, column=0, sticky = "nesw")
rRtyLabel.grid(row=6, column=0)

# fGen5-----------------------
cbItemType1 = tk.Checkbutton(fGen5, text="Armor - Basic", variable=vArmorB, onvalue=1, offvalue=0)
cbItemType2 = tk.Checkbutton(fGen5, text="Armor - Magic", variable=vArmorM, onvalue=1, offvalue=0)
cbItemType3 = tk.Checkbutton(fGen5, text="Potion", variable=vPotion, onvalue=1, offvalue=0)
cbItemType4 = tk.Checkbutton(fGen5, text="Ring", variable=vRing, onvalue=1, offvalue=0)
cbItemType5 = tk.Checkbutton(fGen5, text="Rod", variable=vRod, onvalue=1, offvalue=0)
cbItemType6 = tk.Checkbutton(fGen5, text="Scroll", variable=vScroll, onvalue=1, offvalue=0)
cbItemType7 = tk.Checkbutton(fGen5, text="Staff", variable=vStaff, onvalue=1, offvalue=0)
cbItemType8 = tk.Checkbutton(fGen5, text="Wand", variable=vWand, onvalue=1, offvalue=0)
cbItemType9 = tk.Checkbutton(fGen5, text="Weapon - Basic", variable=vWeaponB, onvalue=1, offvalue=0)
cbItemType10 = tk.Checkbutton(fGen5, text="Weapon - Magic", variable=vWeaponM, onvalue=1, offvalue=0)
cbItemType11 = tk.Checkbutton(fGen5, text="Wonderous", variable=vWonderous, onvalue=1, offvalue=0)

vArmorB.set(True)
vArmorM.set(False)
vPotion.set(True)
vRing.set(False)
vRod.set(False)
vScroll.set(False)
vStaff.set(False)
vWand.set(False)
vWeaponB.set(True)
vWeaponM.set(False)
vWonderous.set(False)

cbItemType1.grid(sticky = "w", row=0, column=0)
cbItemType2.grid(sticky = "w", row=1, column=0)
cbItemType3.grid(sticky = "w", row=2, column=0)
cbItemType4.grid(sticky = "w", row=3, column=0)
cbItemType5.grid(sticky = "w", row=4, column=0)
cbItemType6.grid(sticky = "w", row=5, column=0)
cbItemType7.grid(sticky = "w", row=6, column=0)
cbItemType8.grid(sticky = "w", row=7, column=0)
cbItemType9.grid(sticky = "w", row=8, column=0)
cbItemType10.grid(sticky = "w", row=9, column=0)
cbItemType11.grid(sticky = "w", row=10, column=0)

#Creatiing a Label Widget
#myLabel1 = Label(frameGen, text="Hello World")
#myLabel2 = Label(root, text="Death to all humans")

root.mainloop()






