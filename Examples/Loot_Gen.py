from tkinter import *

root = Tk()
var = IntVar()
root.geometry('1500x700')
root.title("Random Loot Generator")
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()

def myClick():
    myLabel3 = Label(root, text="done")
    myLabel3.grid(row=5, column=1)

def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)

#Creatiing a Label Widget
myLabel1 = Label(root, text="Hello World")
myLabel2 = Label(root, text="Death to all humans")
myButton1 = Button(root, text="Individual Treasure", state=NORMAL, padx=15, pady=15, command = myClick, bg="green")
myButton2 = Button(root, text="Horde Treasure", state=DISABLED, fg="red")
radio1 = Radiobutton(root, text="Level 1", variable=var, value=1, command=sel)
#radio1.pack(anchor = W)
radio2 = Radiobutton(root, text="Level 2", variable=var, value=2, command=sel)
#radio2.pack(anchor = W)
radio3 = Radiobutton(root, text="Level 3", variable=var, value=3, command=sel)
#radio3.pack(anchor = W)
label = Label(root)

ckbox1 = Checkbutton(root, text="Armor", variable=var1, onvalue=1, offvalue=0)
ckbox2 = Checkbutton(root, text="Weapon", variable=var2, onvalue=1, offvalue=0)
ckbox3 = Checkbutton(root, text="Staff", variable=var3, onvalue=1, offvalue=0)

msg = """hello worlds!!"""
T = Text(root, height = 20, width = 52, state=NORMAL)
T.insert(INSERT, "1......")
T.insert(END, "hellow")
T.config(state=DISABLED)

#shoving it onto the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=2)
myButton1.grid(row=0, column=3)
myButton2.grid(row=3, column=1)
radio1.grid(row=0, column=6)
radio2.grid(row=1, column=6)
radio3.grid(row=2, column=6)
label.grid(row=3, column=6)
ckbox1.grid(row=0, column=7)
ckbox2.grid(row=1, column=7)
ckbox3.grid(row=2, column=7)

T.grid(row=0, column=8)

root.mainloop()






