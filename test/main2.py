import webbrowser
from pymongo import MongoClient
from tkinter.ttk import *
from tkinter import *
from PIL import ImageTk, Image
import hashlib
import tkinter.messagebox
import random
import pyperclip
from functools import partial

#-------------------------------------------------------------------------------------------------------------------------------#

client = MongoClient()
db = client.password_manager
userdata = db.userdata

#--------------------------------------------------------------------------------------------------------------------------------#

def first_window():
    window.title("SafePass")

#---------------------------------------------------------------------------------------------------------------------------------#

window = Tk()
window.configure(bg='#282A30')

first_window()

window.mainloop()