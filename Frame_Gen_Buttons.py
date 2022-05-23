from calendar import c
import tkinter as tk
from Randomizer_Handler import *
import random

class Frame_Gen_Buttons:
    def __init__(self, frame, programData, textFrame, levelFrame, rarityFrame, itemTypeFrame):
        self.frame = frame
        self.programData = programData
        self.textFrame = textFrame
        self.levelFrame = levelFrame
        self.rarityFrame = rarityFrame
        self.itemTypeFrame = itemTypeFrame
        self.rhFunList = [method for method in dir(Randomizer_Handler) if method.startswith('__') is False]

        self.bGen1 = tk.Button(self.frame, text="Individual Treasure", state="normal", padx=15, pady=35, command = self.individualTreasureB, bg="green").grid(row=0, column=0, sticky="ew")
        self.bGen2 = tk.Button(self.frame, text="Horde Treasure", state="normal", padx=15, pady=35, command = self.hordeTreasureB, bg="green").grid(row=1, column=0, sticky="ew")
        self.bGen3 = tk.Button(self.frame, text="Weapon Drop", state="normal", padx=15, pady=35, command = self.weaponDropB, bg="green").grid(row=2, column=0, sticky="ew")
        self.bGen4 = tk.Button(self.frame, text="Gem/Art", state="normal", padx=15, pady=35, command = self.artgemB, bg="green").grid(row=3, column=0, sticky="ew")
        tk.Button(self.frame, text="Enchanted Rune\nDrop", state="normal", padx=15, pady=35, command = self.runeB, bg="green").grid(row=4, column=0, sticky="ew")
        self.bGen5 = tk.Button(self.frame, text="Roll Specific Item", state="normal", padx=15, pady=35, command = self.rollItemB, bg="gold").grid(row=5, column=0, sticky="ew")

    # Functions-------------------
    def individualTreasureB(self):
        rh = Randomizer_Handler(self.programData)
        currentLvl = self.levelFrame.varLvl.get()
        outputText = ""
        if currentLvl <=4:
            outputText = rh.indivTreasure(self.programData.individualTreasure.get("0-4"))
            self.textFrame.newOutput(outputText)
        elif currentLvl <= 10:
            outputText = rh.indivTreasure(self.programData.individualTreasure.get("5-10"))
            self.textFrame.newOutput(outputText)
        elif currentLvl <= 16:
            outputText = rh.indivTreasure(self.programData.individualTreasure.get("11-16"))
            self.textFrame.newOutput(outputText)
        elif currentLvl <= 20:
            outputText = rh.indivTreasure(self.programData.individualTreasure.get("17-20"))
            self.textFrame.newOutput(outputText)
        else:
            outputText = "Error!"
            self.textFrame.newOutput(outputText)
    
    def hordeTreasureB(self):
        rh = Randomizer_Handler(self.programData)
        currentLvl = self.levelFrame.varLvl.get()
        outputText = ""
        if currentLvl <=4:
            outputText = rh.hordeTreasure(self.programData.hordeTreasureCoins.get("0-4"), self.programData.hordeTreasureItems.get("0-4"), self.programData)
            self.textFrame.newOutput(outputText)
        elif currentLvl <= 10:
            outputText = rh.hordeTreasure(self.programData.hordeTreasureCoins.get("5-10"), self.programData.hordeTreasureItems.get("5-10"), self.programData)
            self.textFrame.newOutput(outputText)
        elif currentLvl <= 16:
            outputText = rh.hordeTreasure(self.programData.hordeTreasureCoins.get("11-16"), self.programData.hordeTreasureItems.get("11-16"), self.programData)
            self.textFrame.newOutput(outputText)
        elif currentLvl <= 20:
            outputText = rh.hordeTreasure(self.programData.hordeTreasureCoins.get("17-20"), self.programData.hordeTreasureItems.get("17-20"), self.programData)
            self.textFrame.newOutput(outputText)
        else:
            outputText = "Error!"
            self.textFrame.newOutput(outputText)
    
    def weaponDropB(self):
        rh = Randomizer_Handler(self.programData)
        currentLvl = self.levelFrame.varLvl.get()
        outputText = ""
        if currentLvl <=4:
            outputText = rh.aswDrop("0-4")
            self.textFrame.newOutput(outputText)
        elif currentLvl <= 10:
            outputText = rh.aswDrop("5-10")
            self.textFrame.newOutput(outputText)
        elif currentLvl <= 16:
            outputText = rh.aswDrop("11-16")
            self.textFrame.newOutput(outputText)
        elif currentLvl <= 20:
            outputText = rh.aswDrop("17-20")
            self.textFrame.newOutput(outputText)
        else:
            outputText = "Error!"
            self.textFrame.newOutput(outputText)

    def runeB(self):
        rh = Randomizer_Handler(self.programData)
        currentLvl = self.levelFrame.varLvl.get()
        outputText = ""
        if currentLvl <=4:
            outputText = rh.aswDrop("0-4")
            self.textFrame.newOutput(outputText)
        elif currentLvl <= 10:
            outputText = rh.aswDrop("5-10")
            self.textFrame.newOutput(outputText)
        elif currentLvl <= 16:
            outputText = rh.aswDrop("11-16")
            self.textFrame.newOutput(outputText)
        elif currentLvl <= 20:
            outputText = rh.aswDrop("17-20")
            self.textFrame.newOutput(outputText)
        else:
            outputText = "Error!"
            self.textFrame.newOutput(outputText)


    def artgemB(self):
        pass

    def rollItemB(self):
        rh = Randomizer_Handler(self.programData)
        sel = []
        outputText = ""
        for i in range(len(self.itemTypeFrame.varState)):
            if self.itemTypeFrame.varState[i].get():
                sel.append(self.programData.itemTypeList[i])
            # selection = str(self.itemTypeFrame.templist[i]) + " ~ State Bool:\t" + str(self.itemTypeFrame.varState[i].get()) + '\n'
            # self.textFrame.newOutput(selection)
        r = random.choice(sel)
        choice = r[2] + "_" + self.rarityFrame.varRty.get()

        if self.programData.asw.get(choice) != None:
            self.textFrame.newOutput(rh.getasw(self.programData.asw.get(choice)) + "\n") 
        elif self.programData.rrsww.get(choice) != None:
            self.textFrame.newOutput(rh.getrrsww(self.programData.rrsww.get(choice)) + "\n")  
        elif self.programData.potion.get(choice) != None:
            self.textFrame.newOutput(rh.getPotion(self.programData.potion.get(choice)) + "\n")  
        elif self.programData.enchantments.get(choice) != None:
            self.textFrame.newOutput(rh.gete(self.programData.enchantments.get(choice)) + "\n") 
        elif "Scroll" in choice != None:
            temp = "Spell_"
            sl = 0
            if choice[-1] == "C":
                sl = random.choice((0,1))
            elif choice[-1] == "U":
                sl = random.choice((2,3))
            elif choice[-1] == "R":
                sl = random.choice((4,5))
            elif choice[-1] == "V":
                sl = random.choice((6,7,8))
            elif choice[-1] == "L":
                sl = 9  
            choice = "SPELL_" + str(sl)
            self.textFrame.newOutput(rh.getScroll(self.programData.spell.get(choice)) + "\n")                      
            


        
        


