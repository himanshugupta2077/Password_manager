from tkinter import *
import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.password_manager_test01

window = Tk()
window.title("Safe Pass")

txt1 = Entry(window, width = 20)
txt1.pack()

def ppp(): 
    newuserdata = db.txt1.get
    newuserdata.insert_one({"test":1})

button = Button(window, text = "Create New Account", command = ppp)
button.pack(pady = 5)

#newuserdata = "qwerty"


window.mainloop()