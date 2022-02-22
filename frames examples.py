from tkinter import *
from tkinter import ttk

# App Definitions
root = Tk()
root.geometry('1500x700')
root.title("Random Loot Generator")


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
varLvl = IntVar()
varRty = IntVar()
vArmorB = IntVar()
vArmorM = IntVar()
vPotion = IntVar()
vRing = IntVar()
vRod = IntVar()
vScroll = IntVar()
vStaff = IntVar()
vWand = IntVar()
vWeaponB = IntVar()
vWeaponM = IntVar()
vWonderous = IntVar()

# Generator Frame Definitions----------

frameGen = LabelFrame(tabGen, text="Loot Generator Frame", padx=5, pady=5)
frameGen.grid(row=0, column=0)

fGen1 = LabelFrame(frameGen, text="Generator Output", padx=5, pady=5)
fGen2 = LabelFrame(frameGen, text="Loot Level", padx=5, pady=5)
fGen3 = LabelFrame(frameGen, text="Type of Generation", padx=5, pady=5)
fGen4 = LabelFrame(frameGen, text="Item Rarity", padx=5, pady=5)
fGen5 = LabelFrame(frameGen, text="Item Types", padx=5, pady=5)

fGen1.grid(row=0, column=0)
fGen2.grid(row=0, column=1)
fGen3.grid(row=0, column=2)
fGen4.grid(row=0, column=3)
fGen5.grid(row=0, column=4)

# Functions-------------------
def sel():
   selection = "You selected the option " + str(varLvl.get())
   rLvlLabel.config(text = selection)

def selRty():
   selection = "You selected the option " + str(varRty.get())
   rRtyLabel.config(text = selection)

def myClick():
    myLabel3 = Label(fGen3, text="done")
    myLabel3.grid(row=10, column=0)

# fGen1-----------------------
msg = """hello worlds!!"""
conOut = Text(fGen1, height = 20, width = 52, state=NORMAL)
conOut.insert(INSERT, msg)
conOut.insert(END, "hellow")
conOut.config(state=DISABLED)
conOut.grid(row=0, column=0)

# fGen2-----------------------
rLvl1 = Radiobutton(fGen2, text="Level 1", variable=varLvl, value=1, command=sel)
rLvl2 = Radiobutton(fGen2, text="Level 2", variable=varLvl, value=2, command=sel)
rLvl3 = Radiobutton(fGen2, text="Level 3", variable=varLvl, value=3, command=sel)
rLvl4 = Radiobutton(fGen2, text="Level 4", variable=varLvl, value=4, command=sel)
rLvl5 = Radiobutton(fGen2, text="Level 5", variable=varLvl, value=5, command=sel)
rLvl6 = Radiobutton(fGen2, text="Level 6", variable=varLvl, value=6, command=sel)
rLvl7 = Radiobutton(fGen2, text="Level 7", variable=varLvl, value=7, command=sel)
rLvl8 = Radiobutton(fGen2, text="Level 8", variable=varLvl, value=8, command=sel)
rLvl9 = Radiobutton(fGen2, text="Level 9", variable=varLvl, value=9, command=sel)
rLvl10 = Radiobutton(fGen2, text="Level 10", variable=varLvl, value=10, command=sel)
rLvl11 = Radiobutton(fGen2, text="Level 11", variable=varLvl, value=11, command=sel)
rLvl12 = Radiobutton(fGen2, text="Level 12", variable=varLvl, value=12, command=sel)
rLvl13 = Radiobutton(fGen2, text="Level 13", variable=varLvl, value=13, command=sel)
rLvl14 = Radiobutton(fGen2, text="Level 14", variable=varLvl, value=14, command=sel)
rLvl15 = Radiobutton(fGen2, text="Level 15", variable=varLvl, value=15, command=sel)
rLvl16 = Radiobutton(fGen2, text="Level 16", variable=varLvl, value=16, command=sel)
rLvl17 = Radiobutton(fGen2, text="Level 17", variable=varLvl, value=17, command=sel)
rLvl18 = Radiobutton(fGen2, text="Level 18", variable=varLvl, value=18, command=sel)
rLvl19 = Radiobutton(fGen2, text="Level 19", variable=varLvl, value=19, command=sel)
rLvl20 = Radiobutton(fGen2, text="Level 20", variable=varLvl, value=20, command=sel)
rLvlLabel = Label(fGen2)

varLvl.set(1)

rLvl1.grid(row=0, column=0)
rLvl2.grid(row=1, column=0)
rLvl3.grid(row=2, column=0)
rLvl4.grid(row=3, column=0)
rLvl5.grid(row=4, column=0)
rLvl6.grid(row=5, column=0)
rLvl7.grid(row=6, column=0)
rLvl8.grid(row=7, column=0)
rLvl9.grid(row=8, column=0)
rLvl10.grid(row=9, column=0)
rLvl11.grid(row=10, column=0)
rLvl12.grid(row=11, column=0)
rLvl13.grid(row=12, column=0)
rLvl14.grid(row=13, column=0)
rLvl15.grid(row=14, column=0)
rLvl16.grid(row=15, column=0)
rLvl17.grid(row=16, column=0)
rLvl18.grid(row=17, column=0)
rLvl19.grid(row=18, column=0)
rLvl20.grid(row=19, column=0)
rLvlLabel.grid(row=20, column=0)

# fGen3-----------------------
bGen1 = Button(fGen3, text="Individual Treasure", state=NORMAL, padx=15, pady=15, command = myClick, bg="green")
bGen2 = Button(fGen3, text="Horde Treasure", state=NORMAL, padx=15, pady=15, command = myClick, bg="green")
bGen3 = Button(fGen3, text="Weapon Drop", state=NORMAL, padx=15, pady=15, command = myClick, bg="green")
bGen4 = Button(fGen3, text="Magic Item Drop", state=NORMAL, padx=15, pady=15, command = myClick, bg="green")

bGen1.grid(row=0, column=0)
bGen2.grid(row=1, column=0)
bGen3.grid(row=2, column=0)
bGen4.grid(row=3, column=0)

# fGen4-----------------------
rRty1 = Radiobutton(fGen4, text="Common", variable=varRty, value="C", command=selRty)
rRty2 = Radiobutton(fGen4, text="Uncommon", variable=varRty, value="U", command=selRty)
rRty3 = Radiobutton(fGen4, text="Rare", variable=varRty, value="R", command=selRty)
rRty4 = Radiobutton(fGen4, text="Very Rare", variable=varRty, value="V", command=selRty)
rRty5 = Radiobutton(fGen4, text="Legendary", variable=varRty, value="L", command=selRty)
bRty1 = Button(fGen4, text="Roll Item", state=NORMAL, padx=15, pady=15, command = myClick, bg="green")
rRtyLabel = Label(fGen4)

varRty.set("C")

rRty1.grid(row=0, column=0)
rRty2.grid(row=1, column=0)
rRty3.grid(row=2, column=0)
rRty4.grid(row=3, column=0)
rRty5.grid(row=4, column=0)
bRty1.grid(row=5, column=0)
rRtyLabel.grid(row=6, column=0)

# fGen5-----------------------
cbItemType1 = Checkbutton(fGen5, text="Armor - Basic", variable=vArmorB, onvalue=1, offvalue=0)
cbItemType2 = Checkbutton(fGen5, text="Armor - Magic", variable=vArmorM, onvalue=1, offvalue=0)
cbItemType3 = Checkbutton(fGen5, text="Potion", variable=vPotion, onvalue=1, offvalue=0)
cbItemType4 = Checkbutton(fGen5, text="Ring", variable=vRing, onvalue=1, offvalue=0)
cbItemType5 = Checkbutton(fGen5, text="Rod", variable=vRod, onvalue=1, offvalue=0)
cbItemType6 = Checkbutton(fGen5, text="Scroll", variable=vScroll, onvalue=1, offvalue=0)
cbItemType7 = Checkbutton(fGen5, text="Staff", variable=vStaff, onvalue=1, offvalue=0)
cbItemType8 = Checkbutton(fGen5, text="Wand", variable=vWand, onvalue=1, offvalue=0)
cbItemType9 = Checkbutton(fGen5, text="Weapon - Basic", variable=vWeaponB, onvalue=1, offvalue=0)
cbItemType10 = Checkbutton(fGen5, text="Weapon - Magic", variable=vWeaponM, onvalue=1, offvalue=0)
cbItemType11 = Checkbutton(fGen5, text="Wonderous", variable=vWonderous, onvalue=1, offvalue=0)

cbItemType1.grid(row=0, column=0)
cbItemType2.grid(row=1, column=0)
cbItemType3.grid(row=2, column=0)
cbItemType4.grid(row=3, column=0)
cbItemType5.grid(row=4, column=0)
cbItemType6.grid(row=5, column=0)
cbItemType7.grid(row=6, column=0)
cbItemType8.grid(row=7, column=0)
cbItemType9.grid(row=8, column=0)
cbItemType10.grid(row=9, column=0)
cbItemType11.grid(row=10, column=0)

#Creatiing a Label Widget
#myLabel1 = Label(frameGen, text="Hello World")
#myLabel2 = Label(root, text="Death to all humans")

root.mainloop()






