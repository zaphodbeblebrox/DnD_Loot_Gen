from cgitb import enable
from distutils import command
from tkinter import *

root = Tk()

def myClick():
    myLabel3 = Label(root, text="done")
    myLabel3.grid(row=5, column=1)

#Creatiing a Label Widget
myLabel1 = Label(root, text="Hello World")
myLabel2 = Label(root, text="Death to all humans")
myButton1 = Button(root, text="Individual Treasure", state=NORMAL, padx=15, pady=15, command = myClick, bg="green")
myButton2 = Button(root, text="Horde Treasure", state=DISABLED, fg="red")
#shoving it onto the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=2)
myButton1.grid(row=0, column=3)
myButton2.grid(row=3, column=1)

root.mainloop()






