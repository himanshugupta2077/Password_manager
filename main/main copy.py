#-------------------------------IMPORTS-------------------------------------#
import pprint
import hashlib, os

from pymongo import MongoClient
from tkinter import *
from tkinter import simpledialog
from functools import partial

#-------------------------------UI-SETUP & DB-------------------------------------#
client = MongoClient()
db = client.password_manager
userdata = db.userdata

window = Tk()
window.title("Safe Pass")

def first_window():
	lbl1 = Label(window, text = "Welcome!", pady = 5)
	lbl1.config(anchor = CENTER)
	lbl1.pack()

	lbl2 = Label(window, text = "Enter Master Password: ", pady = 10)
	lbl2.pack()

	txt = Entry(window, width = 20, show = "*")
	txt.pack()
	txt.focus()
	
	def check_password1():
		password = txt.get()
		hash_data = {
		'user': 'rahul',
		'salt': b'\x8d\xee\xf9\xbf\x0f\xaa\xfc2\xc9\xe73\x9c\x05)\xeb\xcb\xc8\xb1k\x12[\x93W\xd8qq\xe1\x89\xff\xe6\xc2S',
		'key': 'c6d752e80118cae0b45472e7c6208f0950826c76fee4c996c762c9220c6526a1'
		}

		password = password + hash_data['user']
		salt = hash_data['salt']
		key = hash_data['key']

		new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 1000000)
		new_key = new_key.hex()

		lbl2 = Label(window, text = "", pady = 5)
		lbl2.pack()		

		if "".__eq__(txt.get()):
			lbl2.destroy()
			lbl2 = Label(window, text = "Field cannot be empty.", pady = 5)
			lbl2.pack()

		elif key != new_key:
			lbl2.destroy()
			lbl2 = Label(window, text = "Incorrect password.", pady = 5)
			lbl2.pack()

		elif key == new_key:
			password_vault()

	window.geometry("350x250")
	button = Button(window, text = "Open vault", command = check_password1)
	button.pack(pady = 10)

	button = Button(window, text = "Quit", command = window.quit)
	button.pack(pady = 10)	

def password_vault():
	window.title("Safe Pass - Vault")
	for widget in window.winfo_children():
		widget.destroy()
	window.geometry("750x350")

	button1 = Button(window, text = "Add new entry", command = save_new_entry)
	button1.pack(pady = 5)

	button2 = Button(window, text = "View saved entry", command = view_saved_entry)
	button2.pack(pady = 5)

	button3 = Button(window, text = "Delete saved entry", command = delete_saved_entry)
	button3.pack(pady = 5)

	button = Button(window, text = "Quit", command = window.quit)
	button.pack(pady = 10)	

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

	button = Button(window, text = "Quit", command = window.quit)
	button.pack(pady = 10)	

def view_saved_entry():
	"""view saved entry"""

def delete_saved_entry():
	"""delete saved entry"""	

first_window()
window.mainloop()