import tkinter as tk

class Frame_ItemTypes:
    def __init__(self, frame):
        self.frame = frame

        self.vArmorB = tk.BooleanVar(value=True)
        self.vArmorM = tk.BooleanVar()
        self.vPotion = tk.BooleanVar()
        self.vRing = tk.BooleanVar()
        self.vRod = tk.BooleanVar()
        self.vScroll = tk.BooleanVar()
        self.vStaff = tk.BooleanVar()
        self.vWand = tk.BooleanVar()
        self.vWeaponB = tk.BooleanVar()
        self.vWeaponM = tk.BooleanVar()
        self.vWonderous = tk.BooleanVar()

        self.var1 = tk.Checkbutton(self.frame, text="Armor - Basic", variable=self.vArmorB.set(True), onvalue=1, offvalue=0)
        self.var2 = tk.Checkbutton(self.frame, text="Armor - Magic", variable=self.vArmorM.set(False), onvalue=1, offvalue=0).grid(sticky = "w", row=1, column=0)
        self.var3 = tk.Checkbutton(self.frame, text="Potion", variable=self.vPotion.set(True), onvalue=1, offvalue=0).grid(sticky = "w", row=2, column=0)
        self.var4 = tk.Checkbutton(self.frame, text="Ring", variable=self.vRing.set(False), onvalue=1, offvalue=0).grid(sticky = "w", row=3, column=0)
        self.var5 = tk.Checkbutton(self.frame, text="Rod", variable=self.vRod.set(False), onvalue=1, offvalue=0).grid(sticky = "w", row=4, column=0)
        self.var6 = tk.Checkbutton(self.frame, text="Scroll", variable=self.vScroll.set(False), onvalue=1, offvalue=0).grid(sticky = "w", row=5, column=0)
        tk.Checkbutton(self.frame, text="Staff", variable=self.vStaff.set(False), onvalue=1, offvalue=0).grid(sticky = "w", row=6, column=0)
        tk.Checkbutton(self.frame, text="Wand", variable=self.vWand.set(False), onvalue=1, offvalue=0).grid(sticky = "w", row=7, column=0)
        tk.Checkbutton(self.frame, text="Weapon - Basic", variable=self.vWeaponB.set(True), onvalue=1, offvalue=0).grid(sticky = "w", row=8, column=0)
        tk.Checkbutton(self.frame, text="Weapon - Magic", variable=self.vWeaponM.set(False), onvalue=1, offvalue=0).grid(sticky = "w", row=9, column=0)
        tk.Checkbutton(self.frame, text="Wonderous", variable=self.vWonderous.set(False), onvalue=1, offvalue=0).grid(sticky = "w", row=10, column=0)
        self.var1.grid(sticky = "w", row=0, column=0)




