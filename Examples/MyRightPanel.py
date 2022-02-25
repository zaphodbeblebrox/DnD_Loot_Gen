from tkinter import *

class ColorButton:
	def __init__(self, frame, color, callback):
		self.frame = frame
		self.color = color   # the button's color is retained and accessible
		self.callback = callback

		self.button = Button(self.frame, text=self.color.capitalize(), command= lambda: self.callback(self.color) ).pack(side="left")

		#using pack eliminates the need to count grid spaces


class MyRightPanel:
	def __init__(self, root, frame):
		self.root = root
		self.frame = frame

		#Right Frame and its contents

		self.circleCanvas = Canvas(self.frame, width=100, height=100, bg='white')
		self.circleCanvas.grid(row=0, column=0, padx=10, pady=2)

		self.btnFrame = Frame(self.frame, width=200, height=10, borderwidth=1)
		self.btnFrame.grid(row=1, column=0, padx=10, pady=2)

                # significantly simplified button creation
		self.redBtn = ColorButton(self.btnFrame, "red", self.makeCircle)
		self.yellowBtn = ColorButton(self.btnFrame, "yellow", self.makeCircle)
		self.greenBtn = ColorButton(self.btnFrame, "green", self.makeCircle)

		self.colorLog = Text(self.frame, width = 30, height = 10, takefocus=0)
		self.colorLog.grid(row=3, column=0, padx=10, pady=2)

	def makeCircle(self, color):
		self.circleCanvas.create_oval(20, 20, 80, 80, width=0, fill=color)
		self.colorLog.insert(0.0, color.capitalize() + "\n")