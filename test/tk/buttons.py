from tkinter import *

root = Tk()

def myClick():
	myLabel = Label(root, text = "I clicked a button!")
	myLabel.pack()

myButton = Button(root, text = "Click me!", command = myClick)
myButton.pack()


root.mainloop()