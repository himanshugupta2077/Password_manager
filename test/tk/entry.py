from tkinter import *

root = Tk()

e = Entry(root, width = 50)
e.pack()
e.insert(0, "Himanshu Gupta")

def myClick():
	myLabel = Label(root, text = f"Hi!, {e.get()}")
	myLabel.pack()

myButton = Button(root, text = "Enter yout name: ", command = myClick)
myButton.pack()


root.mainloop()