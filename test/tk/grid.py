from tkinter import *

root = Tk()

# creating a label widget
myLabel1 = Label(root, text = "Hello world!")
myLabel2 = Label(root, text = "My Name is zex")

# shoving it onto the root
myLabel1.grid(row = 0, column = 0)
myLabel2.grid(row = 1, column = 0)

root.mainloop()