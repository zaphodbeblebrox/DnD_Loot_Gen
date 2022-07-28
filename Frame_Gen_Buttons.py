from calendar import c
import tkinter as tk
from Randomizer_Handler import *
from tkinter import ttk, font
import random

class Frame_Gen_Buttons:
    def __init__(self, color, frame, programData, textFrame, levelFrame, rarityFrame, itemTypeFrame):
        self.frame = frame
        self.programData = programData
        self.textFrame = textFrame
        self.levelFrame = levelFrame
        self.rarityFrame = rarityFrame
        self.itemTypeFrame = itemTypeFrame
        self.rhFunList = [method for method in dir(Randomizer_Handler) if method.startswith('__') is False]
        
        boarder1 = tk.Frame(self.frame, highlightcolor=color["label text"], highlightbackground=color["label text"], highlightthickness=2, bd=0, height=5, width=18)
        ttk.Button(boarder1, text="Individual\nTreasure", state="normal", command = self.individualTreasureB).grid(row=0, column=0, sticky="nesw",ipady=15)
        boarder1.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        boarder2 = tk.Frame(self.frame, highlightcolor=color["label text"], highlightbackground=color["label text"], highlightthickness=2, bd=0, height=5, width=18)
        ttk.Button(boarder2, text="Horde\nTreasure", state="normal", command = self.hordeTreasureB).grid(row=0, column=0, sticky="nesw",ipady=15)
        boarder2.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        boarder3 = tk.Frame(self.frame, highlightcolor=color["label text"], highlightbackground=color["label text"], highlightthickness=2, bd=0, height=5, width=18)
        ttk.Button(boarder3, text="Weapon Drop", state="normal", command = self.weaponDropB).grid(row=0, column=0, sticky="nesw",ipady=23)
        boarder3.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)

        boarder4 = tk.Frame(self.frame, highlightcolor=color["label text"], highlightbackground=color["label text"], highlightthickness=2, bd=0, height=5, width=18)
        ttk.Button(boarder4, text="Art & Gems", state="normal", command = self.artgemB).grid(row=0, column=0, sticky="nesw",ipady=23)
        boarder4.grid(row=3, column=0, sticky="nsew", padx=5, pady=5)

        boarder5 = tk.Frame(self.frame, highlightcolor=color["label text"], highlightbackground=color["label text"], highlightthickness=2, bd=0, height=5, width=18)
        ttk.Button(boarder5, text="Enchanted Rune", state="normal", command = self.runeB).grid(row=0, column=0, sticky="nesw",ipady=23)
        boarder5.grid(row=4, column=0, sticky="nsew", padx=5, pady=5)

        boarder6 = tk.Frame(self.frame, highlightcolor=color["label text"], highlightbackground=color["label text"], highlightthickness=2, bd=0, height=5, width=18)
        ttk.Button(boarder6, text="Roll Specific Item", state="normal", command = self.rollItemB).grid(row=0, column=0, sticky="nesw",ipady=23)
        boarder6.grid(row=5, column=0, sticky="nsew", padx=5, pady=5)
        
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
            outputText = rh.rollEnchant("0-4")
            self.textFrame.newOutput(outputText)
        elif currentLvl <= 10:
            outputText = rh.rollEnchant("5-10")
            self.textFrame.newOutput(outputText)
        elif currentLvl <= 16:
            outputText = rh.rollEnchant("11-16")
            self.textFrame.newOutput(outputText)
        elif currentLvl <= 20:
            outputText = rh.rollEnchant("17-20")
            self.textFrame.newOutput(outputText)
        else:
            outputText = "Error!"
            self.textFrame.newOutput(outputText)


    def artgemB(self):
        rh = Randomizer_Handler(self.programData)
        currentLvl = self.levelFrame.varLvl.get()
        if currentLvl <=4:
            self.textFrame.newOutput(rh.rollartgem(self.programData.aglt.get("0-4")))
        elif currentLvl <= 10:
            self.textFrame.newOutput(rh.rollartgem(self.programData.aglt.get("5-10")))
        elif currentLvl <= 16:
            self.textFrame.newOutput(rh.rollartgem(self.programData.aglt.get("11-16")))
        elif currentLvl <= 20:
            self.textFrame.newOutput(rh.rollartgem(self.programData.aglt.get("17-20")))
        else:
            self.textFrame.newOutput("Error!")

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
            


        
        


