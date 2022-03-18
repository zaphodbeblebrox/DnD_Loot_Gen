import tkinter as tk

class Frame_Gen_Buttons:
    def __init__(self, frame, textFrame, levelFrame, rarityFrame, itemTypeFrame):
        self.frame = frame
        self.textFrame = textFrame
        self.levelFrame = levelFrame
        self.rarityFrame = rarityFrame
        self.itemTypeFrame = itemTypeFrame

        self.bGen1 = tk.Button(self.frame, text="Individual Treasure", state="normal", padx=15, pady=35, command = self.individualTreasureB, bg="green").grid(row=0, column=0, sticky="ew")
        self.bGen2 = tk.Button(self.frame, text="Horde Treasure", state="normal", padx=15, pady=35, command = self.hordeTreasureB, bg="green").grid(row=1, column=0, sticky="ew")
        self.bGen3 = tk.Button(self.frame, text="Weapon Drop", state="normal", padx=15, pady=35, command = self.weaponDropB, bg="green").grid(row=2, column=0, sticky="ew")
        self.bGen4 = tk.Button(self.frame, text="Magic Item Drop", state="disabled", padx=15, pady=35, command = self.magicItemB, bg="green").grid(row=3, column=0, sticky="ew")
        self.bGen5 = tk.Button(self.frame, text="Roll Specific Item", state="normal", padx=15, pady=35, command = self.rollItemB, bg="gold").grid(row=4, column=0, sticky="ew")

    # Functions-------------------
    def individualTreasureB(self):
        selection = "Option:\t" + str(self.levelFrame.varLvl.get()) + '\n'
        self.textFrame.newOutput(selection)
        # self.myLabel3 = tk.Label(self.frame, text=selection)
        # self.myLabel3.grid(row=5, column=0)
    
    def hordeTreasureB(self):
        selection = "Option " + str(self.levelFrame.varLvl.get())
        self.myLabel3 = tk.Label(self.frame, text=selection)
        self.myLabel3.grid(row=5, column=0)
    
    def weaponDropB(self):
        selection = "Option " + str(self.levelFrame.varLvl.get())
        self.myLabel3 = tk.Label(self.frame, text=selection)
        self.myLabel3.grid(row=5, column=0)

    def magicItemB(self):
        selection = "Option " + str(self.levelFrame.varLvl.get())
        self.myLabel3 = tk.Label(self.frame, text=selection)
        self.myLabel3.grid(row=5, column=0)

    def rollItemB(self):
        for i in range(len(self.itemTypeFrame.varState)):
            selection = str(self.itemTypeFrame.templist[i]) + "State Bool:\t" + str(self.itemTypeFrame.varState[i].get()) + '\n'
            self.textFrame.newOutput(selection)


