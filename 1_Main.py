# this is a good entry point into the program
# short simple and decoupled from the classes it executes

from Core_Window import *
from Data_Handler import *

programData = Data_Handler()
myWindow = Core_Window(programData)
myWindow.start()
