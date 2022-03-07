import tkinter as tk

class Frame_Gen_Buttons:
    def __init__(self, frame):
        self.frame = frame

        self.bGen1 = tk.Button(self.frame, text="Individual Treasure", state="normal", padx=15, pady=35, command = self.myClick, bg="green").grid(row=0, column=0, sticky="ew")
        self.bGen2 = tk.Button(self.frame, text="Horde Treasure", state="normal", padx=15, pady=35, command = self.myClick, bg="green").grid(row=1, column=0, sticky="ew")
        self.bGen3 = tk.Button(self.frame, text="Weapon Drop", state="normal", padx=15, pady=35, command = self.myClick, bg="green").grid(row=2, column=0, sticky="ew")
        self.bGen4 = tk.Button(self.frame, text="Magic Item Drop", state="normal", padx=15, pady=35, command = self.myClick, bg="green").grid(row=3, column=0, sticky="ew")
        self.bGen5 = tk.Button(self.frame, text="Roll Specific Item", state="normal", padx=15, pady=35, command = self.myClick, bg="gold").grid(row=4, column=0, sticky="ew")

    # Functions-------------------
    def myClick(self):
        self.myLabel3 = tk.Label(self.frame, text="done")
        self.myLabel3.grid(row=5, column=0)
