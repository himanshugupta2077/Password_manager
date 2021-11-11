#-------------------------------IMPORTS-------------------------------------#
import hashlib, os
import pprint
from tkinter import *

import pymongo
from pymongo import MongoClient

#---------------------------PASSWORD-GENERATOR----------------------------------#



#-------------------------------UI-SETUP & DB-------------------------------------#
client = MongoClient()
db = client.password_manager_test01
userdata = db.userdata

window = Tk()
window.title("Safe Pass")

def first_window():
	lbl = Label(window, text = "Welcome!", pady = 5)
	lbl.config(anchor = CENTER)
	lbl.pack()

	window.geometry("250x150")
	button = Button(window, text = "Login", command = login)
	button.pack(pady = 5)

	button = Button(window, text = "New User", command = create_new_account)
	button.pack(pady = 5)

def login():
	window.geometry("350x250")
	for widget in window.winfo_children():
		widget.destroy()
	
	lbl = Label(window, text = "Enter Username: ", pady = 5)
	lbl.config(anchor = CENTER)
	lbl.pack()
	txt = Entry(window, width = 20)
	txt.pack()
	txt.focus()

	lbl1 = Label(window, text = "Enter Master Password: ", pady = 5)
	lbl1.pack()
	txt1 = Entry(window, width = 20)
	txt1.pack()

	def check_db_and_MP():
		test = "pass"
		collection_names = db.list_collection_names()
			
		if "".__eq__(txt.get()) or "".__eq__(txt1.get()):
			lbl2 = Label(window, text = "Enter all the fields", pady = 5)
			lbl2.pack()

		elif txt.get() not in collection_names:
			lbl2 = Label(window, text = "Incorrect username", pady = 5)
			lbl2.pack()

		elif txt1.get() == test:
			password_vault()

	button = Button(window, text = "Login", command = check_db_and_MP)
	button.pack(pady = 5)

	lbl3 = Label(window)
	lbl3.pack()

def create_new_account():
	window.geometry("350x250")
	for widget in window.winfo_children():
		widget.destroy()
	
	lbl = Label(window, text = "Pick a username: ", pady = 5)
	lbl.config(anchor = CENTER)
	lbl.pack()
	txt = Entry(window, width = 20)
	txt.pack()
	txt.focus()

	lbl1 = Label(window, text = "Create Master Password: ", pady = 5)
	lbl1.pack()
	txt1 = Entry(window, width = 20)
	txt1.pack()

	lbl2 = Label(window, text = "Re-Enter Master Password: ", pady = 5)
	lbl2.pack()
	txt2 = Entry(window, width = 20)
	txt2.pack()
		
	def check_and_create_new_collection():
		collection_names = db.list_collection_names()
		print(collection_names)
		print(txt.get())

		if "".__eq__(txt.get()) or "".__eq__(txt1.get()) or "".__eq__(txt2.get()):
			lbl3 = Label(window, text = "Enter all the fields", pady = 5)
			lbl3.pack()		
		
		elif txt.get() in collection_names:
			lbl3 = Label(window, text = "Username already picked\nPlease pick another username", pady = 5)
			lbl3.pack()
		
		elif txt1.get() != txt2.get():
			lbl3 = Label(window, text = "Passwords do not match", pady = 5)
			lbl3.pack()
		
		else:
			hash_password(txt.get())
			newuserdata = txt.get()
			newuserdata = db.userdata
			newuserdata.insert_one({"test":1})
			for widget in window.winfo_children():
				widget.destroy()
			login()

	button = Button(window, text = "Create New Account", command = check_and_create_new_collection)
	button.pack(pady = 5)

def password_vault():
	for widget in window.winfo_children():
		widget.destroy()
	window.geometry("750x350")

	button1 = Button(window, text = "Add new entry", command = save_new_entry)
	button1.pack(pady = 5)

	button2 = Button(window, text = "View saved entry", command = view_saved_entry)
	button2.pack(pady = 5)

	button3 = Button(window, text = "Delete saved entry", command = delete_saved_entry)
	button3.pack(pady = 5)		

def save_new_entry():
	for widget in window.winfo_children():
		widget.destroy()
	window.geometry("750x350")

	lbl = Label(window, text = "New Entry: ")
	lbl.config(anchor = CENTER)
	lbl.pack()

	lbl = Label(window, text = "Title: ")
	lbl.pack()
	title_entry = Entry(window, width = 20)
	title_entry.pack()
	title_entry.focus()

	lbl = Label(window, text = "URL: ")
	lbl.pack()
	url_entry = Entry(window, width = 20)
	url_entry.pack()

	lbl = Label(window, text = "Username: ")
	lbl.pack()
	username_entry = Entry(window, width = 20)
	username_entry.pack()

	lbl = Label(window, text = "Password: ")
	lbl.pack()
	password_entry = Entry(window, width = 20)
	password_entry.pack()

	lbl = Label(window, text = "Note: ")
	lbl.pack()
	note_entry = Entry(window, width = 20)
	note_entry.pack()

	def save_user_data():
		title = title_entry.get()
		url = url_entry.get()
		username = username_entry.get()
		password = password_entry.get()
		note = note_entry.get()

		entry = {
		"title": title,
		"url": url,
		"username": username,
		"password": password,
		"note": note 
		}

		userdata.insert_one(entry)
		for widget in window.winfo_children():
			widget.destroy()
		password_vault()

	button = Button(window, text = "Save", command = save_user_data)
	button.pack(pady = 5)

def view_saved_entry():
	"""view saved entry"""

def delete_saved_entry():
	"""delete saved entry"""

def hash_password(password):
	salt = os.urandom(64)
	key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

def check_master_password():

	users = [[]]

	username = 'Brent' # The users username
	password = 'mypassword' # The users password

	salt = os.urandom(32) # A new salt for this user
	key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
	users[username] = { # Store the salt and key
		'salt': salt,
    	'key': key
		}


first_window()
window.mainloop()
