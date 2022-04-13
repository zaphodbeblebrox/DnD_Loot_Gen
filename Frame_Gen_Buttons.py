from calendar import c
import tkinter as tk
from Randomizer_Handler import *

class Frame_Gen_Buttons:
    def __init__(self, frame, programData, textFrame, levelFrame, rarityFrame, itemTypeFrame):
        self.frame = frame
        self.programData = programData
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
        currentLvl = self.levelFrame.varLvl.get()
        outputText = ""
        if currentLvl <=4:
            outputText = Randomizer_Handler.indivTreasure(self.programData.individualTreasure.get("0-4"))
            self.textFrame.newOutput(outputText)
        elif currentLvl <= 10:
            outputText = Randomizer_Handler.indivTreasure(self.programData.individualTreasure.get("5-10"))
            self.textFrame.newOutput(outputText)
        elif currentLvl <= 16:
            outputText = Randomizer_Handler.indivTreasure(self.programData.individualTreasure.get("11-16"))
            self.textFrame.newOutput(outputText)
        elif currentLvl <= 20:
            outputText = Randomizer_Handler.indivTreasure(self.programData.individualTreasure.get("17-20"))
            self.textFrame.newOutput(outputText)
        else:
            outputText = "Error!"
            self.textFrame.newOutput(outputText)
    
    def hordeTreasureB(self):
        currentLvl = self.levelFrame.varLvl.get()
        outputText = ""
        if currentLvl <=4:
            outputText = Randomizer_Handler.hordeTreasure(self.programData.hordeTreasureCoins.get("0-4"), self.programData.hordeTreasureItems.get("0-4"), self.programData)
            self.textFrame.newOutput(outputText)
        elif currentLvl <= 10:
            outputText = Randomizer_Handler.hordeTreasure(self.programData.hordeTreasureCoins.get("5-10"), self.programData.hordeTreasureItems.get("5-10"), self.programData)
            self.textFrame.newOutput(outputText)
        elif currentLvl <= 16:
            outputText = Randomizer_Handler.hordeTreasure(self.programData.hordeTreasureCoins.get("11-16"), self.programData.hordeTreasureItems.get("11-16"), self.programData)
            self.textFrame.newOutput(outputText)
        elif currentLvl <= 20:
            outputText = Randomizer_Handler.hordeTreasure(self.programData.hordeTreasureCoins.get("17-20"), self.programData.hordeTreasureItems.get("17-20"), self.programData)
            self.textFrame.newOutput(outputText)
        else:
            outputText = "Error!"
            self.textFrame.newOutput(outputText)
    
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
            selection = str(self.itemTypeFrame.templist[i]) + " ~ State Bool:\t" + str(self.itemTypeFrame.varState[i].get()) + '\n'
            self.textFrame.newOutput(selection)


