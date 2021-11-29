#----------------------------------------------------------------------------------------------------------------------------#
import webbrowser
from pymongo import MongoClient
from tkinter.ttk import *
from tkinter import *
import hashlib
import tkinter.messagebox
import random
import pyperclip
from functools import partial
import smtplib, ssl
import math
import keyring
import os
#----------------------------------------------------------------------------------------------------------------------------#
client = MongoClient()
db = client.password_manager
userdata = db.userdata
user_metadata = db.user_metadata

def password_vault():
	window.geometry("530x590")
	
	window.title("Vault")
	for widget in window.winfo_children():
		widget.destroy()
	view_saved_entry()

def add_new_entry():
	for widget in window.winfo_children():
		widget.destroy()

	window.title("SafePass - Add New Entry")

	lbl1 = Label(window, text = "Add New Entry", font=("Manjari Thin", 30), bg = "#23262B", fg="white")
	lbl1.place(x = 140, y = 22)

	button1 = Button(window, text = "Add new entry", command = add_new_entry, width = 14, bg = "#4658E0", fg="white", highlightthickness=0, borderwidth=0)
	button1.place(x = 13, y = 90)

	button2 = Button(window, text = "View saved entry", command = view_saved_entry, width = 14, bg = "#4658E0", fg="white", highlightthickness=0, borderwidth=0)
	button2.place(x = 195, y = 90)

	button3 = Button(window, text = "Options", command = options, width = 14, bg = "#4658E0", fg="white", highlightthickness=0, borderwidth=0)
	button3.place(x = 377, y = 90)

	button = Button(window, text = "Cancel", command = window.quit, width = 10, bg = "#4658E0", fg="white", highlightthickness=0, borderwidth=0)
	button.place(x = 405, y = 547)

	button = Button(window, text = "Help", command = help, width = 10, bg = "#4658E0", fg="white", highlightthickness=0, borderwidth=0)
	button.place(x = 13, y = 547)

	lbl = Label(window, text = "Title: ", font=("Great Vibes", 13), bg = "#23262B", fg="white")	
	lbl.place(x = 30, y = 140)
	title_entry = Entry(window, width = 40, bg="#1D1B19", fg="white", highlightthickness=0, borderwidth=0)
	title_entry.place(x = 130, y = 140)
	title_entry.focus()

	lbl = Label(window, text = "URL: ",font=("Great Vibes", 13), bg = "#23262B", fg="white")
	lbl.place(x = 30, y = 170)
	url_entry = Entry(window, width = 40, bg="#1D1B19", fg="white", highlightthickness=0, borderwidth=0)
	url_entry.place(x = 130, y = 170)

	lbl = Label(window, text = "Username: ", font=("Great Vibes", 13), bg = "#23262B", fg="white")
	lbl.place(x = 30, y = 200)
	username_entry = Entry(window, width = 40, bg="#1D1B19", fg="white" , highlightthickness=0, borderwidth=0)
	username_entry.place(x = 130, y = 200)

	lbl = Label(window, text = "Password: ", font=("Great Vibes", 13), bg = "#23262B", fg="white")
	lbl.place(x = 30, y = 230)
	password_entry = Entry(window, width = 40, bg="#1D1B19", fg="white", highlightthickness=0, borderwidth=0)
	password_entry.place(x = 130, y = 230)

	def generate_password():
		password = calc_password()
		password_entry.insert(10, password)

	def calc_password():
		password_entry.delete(0, END)    
		
		MAX_LEN = length.get()

		DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  
		LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
							'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
							'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
							'z']
		
		UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
							'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
							'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
							'Z']
		
		SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', 
				'*', '(', ')', '<']
		
		COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
		
		rand_digit = random.choice(DIGITS)
		rand_upper = random.choice(UPCASE_CHARACTERS)
		rand_lower = random.choice(LOCASE_CHARACTERS)
		rand_symbol = random.choice(SYMBOLS)

		temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

		temp_pass_list = []
		for x in range(MAX_LEN - 4):
			temp_pass = temp_pass + random.choice(COMBINED_LIST)

			temp_pass_list = list(temp_pass)
			random.shuffle(temp_pass_list)
		
		password = ""
		for x in temp_pass_list:
				password = password + x

		return password

	button = Button(window, text = "Generate Password", command = generate_password, bg = "#4658E0", fg="white", highlightthickness=0, borderwidth=0)
	button.place(x = 130, y = 260)
	
	combo = Combobox(window, textvariable = length, width = 4, background="#1D1B19", foreground="black")
	combo['values'] = ( 8, 9, 10, 11, 12, 13, 14, 15, 16,
                        17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 
                        27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 
                        37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 
                        47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 
                        57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 
                        67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 
                        77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 
                        87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 
                        97, 98, 99, 100, 101, 102, 103, 104, 105, 
                        106, 107, 108, 109, 110, 111, 112, 113, 
                        114, 115, 116, 117, 118, 119, 120)
	combo.current(0)
	combo.bind('<<ComboboxSelected>>')
	combo.place(x = 468, y = 230)
	
	def copy_password():
		password = password_entry.get()
		pyperclip.copy(password)
		
	copy_button = Button(window, text="Copy", command = copy_password, bg = "#4658E0", fg="white", highlightthickness=0, borderwidth=0)
	copy_button.place(x = 295, y = 260)

	lbl = Label(window, text = "Note: ",font=("Great Vibes", 13), bg = "#23262B", fg="white")
	lbl.place(x = 30, y = 298)
	note_entry = Text(window, width = 40, height = 12, bg="#1D1B19", fg="white", highlightthickness=0, borderwidth=0)
	note_entry.place(x = 130, y = 298)

	def save_user_data():
		title = title_entry.get()
		url = url_entry.get()
		username = username_entry.get()
		password = password_entry.get()
		note = note_entry.get('1.0', 'end')

		entry = {
		"title": title,
		"url": url,
		"username": username,
		"password": password,
		"note": note 
		}

		userdata.insert_one(entry)
		# for widget in window.winfo_children():
		# 	widget.destroy()
		title_entry.delete(0, END)
		url_entry.delete(0, END)
		username_entry.delete(0, END)
		password_entry.delete(0, END)
		note_entry.delete(1.0, END)
		title_entry.focus()

	button = Button(window, text = "Save", command = save_user_data, width = 10, bg = "#4658E0", fg="white", highlightthickness=0, borderwidth=0)
	button.place(x = 275, y = 547)

def view_saved_entry():
	window.title("SafePass - View Entry")
	for widget in window.winfo_children():
		widget.destroy()

	lbl1 = Label(window, text = "Saved Entries", font=("Manjari Thin", 30), bg = "#23262B", fg="white")
	lbl1.place(x = 150, y = 22)

	button1 = Button(window, text = "Add new entry", command = add_new_entry, width = 14, bg = "#4658E0", fg="white", highlightthickness=0, borderwidth=0)
	button1.place(x = 13, y = 90)

	button2 = Button(window, text = "View saved entry", command = view_saved_entry, width = 14, bg = "#4658E0", fg="white", highlightthickness=0, borderwidth=0)
	button2.place(x = 195, y = 90)

	button3 = Button(window, text = "Options", command = options, width = 14, bg = "#4658E0", fg="white", highlightthickness=0, borderwidth=0)
	button3.place(x = 377, y = 90)

	button = Button(window, text = "Cancel", command = window.quit, width = 10, bg = "#4658E0", fg="white", highlightthickness=0, borderwidth=0)
	button.place(x = 405, y = 547)

	button = Button(window, text = "Help", command = help, width = 10, bg = "#4658E0", fg="white", highlightthickness=0, borderwidth=0)
	button.place(x = 13, y = 547)

	document_list = userdata.find({},{"_id": 0})
	document_list = list(document_list)

	def title_viewer(password):
		root = Tk()
		root.geometry("1400x500")
		root.configure(bg='#23262B')
		root.title("SafePass - Details")
		my_query = {"password": password }
		saved_title = userdata.find(my_query)

		for x in saved_title:
			user_title = x['title']
			user_url = x['url']
			user_username = x['username']
			user_password = x['password']
			user_note = x['note']

			lbl = Label(root, text = "Title: ", font=("Great Vibes", 13), bg = "#23262B", fg="white")
			lbl.place(x = 20, y = 15)
			lbl = Label(root, text = user_title, bg = "#23262B", fg="white")
			lbl.place(x = 130, y = 15)

			lbl = Label(root, text = "URL: ", font=("Great Vibes", 13), bg = "#23262B", fg="white")
			lbl.place(x = 20, y = 50)
			lbl = Label(root, text = user_url,  bg = "#23262B", fg="white")
			lbl.place(x = 130, y = 50)
			copy_button = Button(root, text="Copy URL", command =  partial(copy_me ,user_url), width = 15, bg = "#4658E0", fg="white", highlightthickness=0, borderwidth=0)
			copy_button.place(x = 1200, y = 50)
			open_me = Button(root, text = "Open URL", command =  partial(callback ,user_url),  width = 15, bg = "#4658E0", fg="white", highlightthickness=0, borderwidth=0)
			open_me.place(x = 1040, y= 50)

			lbl = Label(root, text = "Username: ", font=("Great Vibes", 13), bg = "#23262B", fg="white")
			lbl.place(x = 20, y = 85)
			lbl = Label(root, text = user_username, bg = "#23262B", fg="white")
			lbl.place(x = 130, y = 85)
			copy_button = Button(root, text="Copy Username", command =  partial(copy_me ,user_username),width = 15, bg = "#4658E0", fg="white", highlightthickness=0, borderwidth=0)
			copy_button.place(x = 1200, y = 85)

			lbl = Label(root, text = "Passowrd: ", font=("Great Vibes", 13), bg = "#23262B", fg="white")
			lbl.place(x = 20, y = 120)
			lbl = Label(root, text = user_password, bg = "#23262B", fg="white")
			lbl.place(x = 130, y = 120)
			copy_button = Button(root, text="Copy Password", command =  partial(copy_me ,user_password),width = 15, bg = "#4658E0", fg="white", highlightthickness=0, borderwidth=0)
			copy_button.place(x = 1200, y = 120)

			lbl = Label(root, text = "Note: ", font=("Great Vibes", 13), bg = "#23262B", fg="white")
			lbl.place(x = 20, y = 155)
			lbl = Label(root, text = user_note, bg = "#23262B", fg="white")
			lbl.place(x = 130, y = 155)
			copy_button = Button(root, text="Copy Note", command =  partial(copy_me ,user_note),width = 15, bg = "#4658E0", fg="white", highlightthickness=0, borderwidth=0)
			copy_button.place(x = 1200, y = 155)

		root.mainloop()	

	# ent = Entry(window, width = 47, bg="#1D1B19", fg="white", highlightthickness=0, borderwidth=0)
	# ent.place(x = 18, y = 147)
	# pop = "Search here"
	# ent.insert(10, pop)

	# def search_me(query):
	# 	print(query)
	# 	for x in userdata.find({"title": query}):
	# 		print(x)

	# btn = Button(window, text = "Search", width = 10, command = partial(search_me , ent.get), bg = "#4658E0", fg="white", highlightthickness=0, borderwidth=0)
	# btn.place(x = 410, y = 144, )

	x_cor = 18
	y_cor = 198

	x_cor1 = 410
	y_cor1 = 198

	x_cor2 = 290
	y_cor2 = 198		

	for x in document_list:
		title = x['title']
		password = x['password']

		button1 = Button(window, text = title.title(), command = partial(title_viewer ,password), width = 20, bg = "#4658E0", fg="white", highlightthickness=0, borderwidth=0)
		button1.place(x = x_cor, y = y_cor)
		y_cor += 43

		button1 = Button(window, text = "Delete", command = partial(delete_me ,password), width = 10, bg = "#4658E0", fg="white", highlightthickness=0, borderwidth=0)
		button1.place(x = x_cor1, y = y_cor1)
		y_cor1 += 43

		button1 = Button(window, text = "Edit", command = partial(update_me ,password), width = 10, bg = "#4658E0", fg="white", highlightthickness=0, borderwidth=0)
		button1.place(x = x_cor2, y = y_cor2)
		y_cor2 += 43

def options():
	window.title("SafePass - Options")
	for widget in window.winfo_children():
		widget.destroy()

	lbl1 = Label(window, text = "Options", font=("Manjari Thin", 30), bg = "#23262B", fg="white")
	lbl1.place(x = 190, y = 22)

	button1 = Button(window, text = "Add new entry", command = add_new_entry, width = 14, bg = "#4658E0", fg="white", highlightthickness=0, borderwidth=0)
	button1.place(x = 13, y = 90)

	button2 = Button(window, text = "View saved entry", command = view_saved_entry, width = 14, bg = "#4658E0", fg="white", highlightthickness=0, borderwidth=0)
	button2.place(x = 195, y = 90)

	button3 = Button(window, text = "Options", command = options, width = 14, bg = "#4658E0", fg="white", highlightthickness=0, borderwidth=0)
	button3.place(x = 377, y = 90)

	button = Button(window, text = "Cancel", command = window.quit, width = 10, bg = "#4658E0", fg="white", highlightthickness=0, borderwidth=0)
	button.place(x = 405, y = 547)

	button = Button(window, text = "Help", command = help, width = 10, bg = "#4658E0", fg="white", highlightthickness=0, borderwidth=0)
	button.place(x = 13, y = 547)

	def export_data():
		pass

	def import_data():
		pass

	button1 = Button(window, text = "Export", command = export_data, bg = "#4658E0", fg="white", highlightthickness=0, borderwidth=0)
	button1.place(x = 18, y = 155)

	button2 = Button(window, text = "Import", command = import_data, bg = "#4658E0", fg="white", highlightthickness=0, borderwidth=0)
	button2.place(x = 18, y = 195)

	button2 = Button(window, text = "Change master password", command = change_master_password, bg = "#4658E0", fg="white", highlightthickness=0, borderwidth=0)
	button2.place(x = 18, y = 235)
	
def help():
	root1 = Toplevel()
	root1.geometry("395x299")
	root1.configure(bg='#23262B')
	root1.title("SafePass - About")

	lbl= Label(root1, text = "SafePass", font=("Great Vibes", 13), bg = "#23262B", fg="white")
	lbl.place(x = 165, y = 170)
	lbl= Label(root1, text = "1.0", font=("Great Vibes", 13), bg = "#23262B", fg="white")
	lbl.place(x = 185, y = 200)
	lbl= Label(root1, text = "SafePass keeps all your Passoword in a Digital Vault", font=("Great Vibes", 13), bg = "#23262B", fg="white")
	lbl.place(x = 25, y = 230)
	link = Label(root1, text="Homepage - Help", font=("Great Vibes", 13), fg="blue", cursor="hand2", bg = "#23262B")
	link.place(x = 140, y = 260)
	link.bind("<Button-1>", lambda e:
	callback("https://zexceed012.github.io/"))
	
	global imgq
	imgq=PhotoImage(file='/home/user/Documents/STUDIEZ/Projects/04-Password-Manager/Project_files/main/images/locked.ppm')
	Label(root1,image=imgq).place(x = 125, y = 10)
	root1.mainloop()

def copy_me(data):
	pyperclip.copy(data)

def delete_me(data_id):
	my_query = {"password": data_id}
	userdata.delete_one(my_query)
	view_saved_entry()
	
def update_me(password):

	my_query = {"password": password }
	saved_title = userdata.find(my_query)

	for x in saved_title:
		title1 = x["title"]
		url1= x["url"]
		username1 = x["username"]
		password1 = x["password"]
		note1 = x["note"]

	to_be_update = {"title" : title1, "url" : url1, "username" : username1, "password" : password1, "note" : note1}

	root2 = Toplevel()
	root2.geometry("530x455")
	root2.title("SafePass - Edit")
	root2.configure(bg='#23262B')
	
	lbl = Label(root2, text = "Title: ", font=("Great Vibes", 13), bg = "#23262B", fg="white")	
	lbl.place(x = 30, y = 30)
	title_entry = Entry(root2, width = 40, bg="#1D1B19", fg="white", highlightthickness=0, borderwidth=0)
	title_entry.place(x = 130, y = 30)
	title_entry.insert(10, title1)
	title_entry.focus()

	lbl = Label(root2, text = "URL: ", font=("Great Vibes", 13), bg = "#23262B", fg="white")
	lbl.place(x = 30, y = 60)
	url_entry = Entry(root2, width = 40, bg="#1D1B19", fg="white", highlightthickness=0, borderwidth=0)
	url_entry.insert(10, url1)
	url_entry.place(x = 130, y = 60)

	lbl = Label(root2, text = "Username: ", font=("Great Vibes", 13), bg = "#23262B", fg="white")
	lbl.place(x = 30, y = 90)
	username_entry = Entry(root2, width = 40, bg="#1D1B19", fg="white", highlightthickness=0, borderwidth=0)
	username_entry.insert(10, username1)
	username_entry.place(x = 130, y = 90)

	lbl = Label(root2, text = "Password: ", font=("Great Vibes", 13), bg = "#23262B", fg="white")
	lbl.place(x = 30, y = 120)
	password_entry = Entry(root2, width = 40, bg="#1D1B19", fg="white", highlightthickness=0, borderwidth=0)
	password_entry.insert(10, password1)
	password_entry.place(x = 130, y = 120)

	def generate_password():
		password = calc_password()
		password_entry.insert(10, password)

	def calc_password():
		password_entry.delete(0, END)    
		
		MAX_LEN = length.get()

		DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  
		LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
							'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
							'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
							'z']
		
		UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
							'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
							'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
							'Z']
		
		SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', 
				'*', '(', ')', '<']
		
		COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
		
		rand_digit = random.choice(DIGITS)
		rand_upper = random.choice(UPCASE_CHARACTERS)
		rand_lower = random.choice(LOCASE_CHARACTERS)
		rand_symbol = random.choice(SYMBOLS)

		temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

		temp_pass_list = []
		for x in range(MAX_LEN - 4):
			temp_pass = temp_pass + random.choice(COMBINED_LIST)

			temp_pass_list = list(temp_pass)
			random.shuffle(temp_pass_list)
		
		password = ""
		for x in temp_pass_list:
				password = password + x

		return password

	button = Button(root2, text = "Generate Password", command = generate_password, bg = "#4658E0", fg="white", highlightthickness=0, borderwidth=0)
	button.place(x = 130, y = 150)
	
	combo = Combobox(root2, textvariable = length, width = 4)
	combo['values'] = ( 8, 9, 10, 11, 12, 13, 14, 15, 16,
                        17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 
                        27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 
                        37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 
                        47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 
                        57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 
                        67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 
                        77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 
                        87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 
                        97, 98, 99, 100, 101, 102, 103, 104, 105, 
                        106, 107, 108, 109, 110, 111, 112, 113, 
                        114, 115, 116, 117, 118, 119, 120)
	combo.current(0)
	combo.bind('<<ComboboxSelected>>')
	combo.place(x = 468, y = 120)
	
	def copy_password():
		password = password_entry.get()
		pyperclip.copy(password)
		
	copy_button = Button(root2, text="Copy", command = copy_password, bg = "#4658E0", fg="white", highlightthickness=0, borderwidth=0)
	copy_button.place(x = 295, y = 150)

	lbl = Label(root2, text = "Note: ", font=("Great Vibes", 13), bg = "#23262B", fg="white")
	lbl.place(x = 30, y = 188)
	note_entry = Text(root2, width = 40, height = 12, bg="#242424", fg="white")
	note_entry.insert(INSERT, note1)
	note_entry.place(x = 130, y = 188)

	def update_button():
		title = title_entry.get()
		url = url_entry.get()
		username = username_entry.get()
		password = password_entry.get()
		note = note_entry.get('1.0', 'end')
		
		entry = {"$set":{
				"title": title,
				"url": url,
				"username": username,
				"password": password,
				"note": note 
				}}

		userdata.update_one(to_be_update, entry)
		root2.quit()

	button = Button(root2, text = "Save", command = update_button, width = 10, bg = "#4658E0", fg="white", highlightthickness=0, borderwidth=0)
	button.place(x = 270, y = 410)

	button = Button(root2, text = "Cancel", command = root2.quit, width = 10, bg = "#4658E0", fg="white", highlightthickness=0, borderwidth=0)
	button.place(x = 400, y = 410)

	root2.mainloop()
	view_saved_entry()

def callback(url):
	webbrowser.open_new_tab(url)

def first_window():
	window.geometry("500x244")
	window.title("SafePass - Open Vault")

	lbl1 = Label(window, text = "Enter Credentials", font=("Manjari Thin", 30), bg = "#23262B", fg="white")
	lbl1.place(x = 32, y = 22)

	lbl2 = Label(window, text = "Enter first name: ", font=("Great Vibes", 13), bg = "#23262B", fg="white")
	lbl2.place(x = 32, y = 80)
	
	txt1 = Entry(window, width = 33, bg="#1D1B19", fg="white", highlightthickness=0, borderwidth=0)
	txt1.place(x = 190, y = 83)
	txt1.focus()

	lbl2 = Label(window, text = "Enter last name: ", font=("Great Vibes", 13), bg = "#23262B", fg="white")
	lbl2.place(x = 32, y = 115)

	txt2 = Entry(window, width = 33, bg="#1D1B19", fg="white", highlightthickness=0, borderwidth=0)
	txt2.place(x = 190, y = 118)

	lbl2 = Label(window, text = "Enter password: ", font=("Great Vibes", 13), bg = "#23262B", fg="white")
	lbl2.place(x = 32, y = 150)

	txt3 = Entry(window, width = 33, bg="#1D1B19", fg="white", highlightthickness=0, borderwidth=0)
	txt3.place(x = 190, y = 153)

	def check_credentials():
		if "".__eq__(txt1.get()) or "".__eq__(txt2.get()) or "".__eq__(txt3.get()):
			tkinter.messagebox.showinfo("Warning!", "Enter all the fields")
		else:
			check_password1()
	
	def check_password1():
		user1 = txt1.get()
		user2 = txt2.get()
		password = txt3.get()
		salt = keyring.get_password("safepass", user1)
		key = keyring.get_password("safepass", user2)
		new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode('utf-8'), 1000000)
		new_key = str(new_key)

		if key != new_key: 
			tkinter.messagebox.showinfo("Warning!", "Incorrect Password\nTry again")
		else: 
			password_vault()

	button = Button(window, text = "Ok", command = check_credentials, width = 8 , bg = "#4658E0", fg="white", highlightthickness=0, borderwidth=0)
	button.place(x = 284, y = 200)

	button = Button(window, text = "Help", command = help, width = 8 , bg = "#4658E0", fg="white", highlightthickness=0, borderwidth=0)
	button.place(x = 17, y = 200)	

	def reset_password():
		for widget in window.winfo_children():
			widget.destroy()
		window.geometry("500x180")
		window.title("SafePass - Forgot Password")

		lbl1 = Label(window, text = "Reset Password", font=("Manjari Thin", 30), bg = "#23262B", fg="white")
		lbl1.place(x = 35, y = 28)

		lbl2 = Label(window, text = "Enter Email-ID: ", font=("Alef", 12), bg = "#23262B", fg="white")
		lbl2.place(x = 32, y = 85)
		
		txt1 = Entry(window, width = 33, bg="#1D1B19", fg="white", highlightthickness=0, borderwidth=0)
		txt1.place(x = 170, y = 87)
		txt1.focus()

		def send_me_otp():
			entered_email = txt1.get()

			for x in user_metadata.find({},{ "_id": 0 }):
  				email = x["email"]

			if entered_email == email:
						def generateOTP() :
						
							digits = "0123456789"
							OTP = ""

							for i in range(4) :
								OTP += digits[math.floor(random.random() * 10)]
						
							return OTP

						def send_otp():

							for x in user_metadata.find({},{ "_id": 0 }):
								email = x["email"]

							port = 465
							smtp_server = "smtp.gmail.com"
							sender_email = "albertsosmarteinstein@gmail.com"  
							receiver_email = email
							password = "WTGoVzMhGnh%R^^@budk7^2aDc9b#3Nv$XGkAPbsoLH"
							
							message = f"""\
							Subject: Hi there

							This message is sent from SafePass.

							Your OTP is {otp}, don't share it with anyone. 
							"""

							context = ssl.create_default_context()
							with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
								server.login(sender_email, password)
								server.sendmail(sender_email, receiver_email, message)
						
						otp = generateOTP()
						send_otp()

						for widget in window.winfo_children():
							widget.destroy()

						lbl1 = Label(window, text = "Reset Password", font=("Manjari Thin", 30), bg = "#23262B", fg="white")
						lbl1.place(x = 40, y = 28)
						
						lbl2 = Label(window, text = "Enter OTP: ", font=("Alef", 12), bg = "#23262B", fg="white")
						lbl2.place(x = 32, y = 85)
						
						txt = Entry(window, width = 33, bg="#1D1B19", fg="white", highlightthickness=0, borderwidth=0)
						txt.place(x = 170, y = 87)
						txt.focus()

						def check_otp():
							if otp == txt.get(): change_master_password()
							else: print("Wrong OTP")
						
						button = Button(window, text = "Ok", command = check_otp ,width = 8 , bg = "#4658E0", fg="white", highlightthickness=0, borderwidth=0)
						button.place(x = 282, y = 135)
						
						button = Button(window, text = "Help", command = help, width = 8 , bg = "#4658E0", fg="white", highlightthickness=0, borderwidth=0)
						button.place(x = 17, y = 135)
						
						button = Button(window, text = "Cancel", command = window.quit, width = 8 , bg = "#4658E0" , fg="white", highlightthickness=0, borderwidth=0)
						button.place(x = 385, y = 135)

		button = Button(window, text = "Send OTP", command = send_me_otp ,width = 8 , bg = "#4658E0", fg="white", highlightthickness=0, borderwidth=0)
		button.place(x = 282, y = 135)

		button = Button(window, text = "Help", command = help, width = 8 , bg = "#4658E0", fg="white", highlightthickness=0, borderwidth=0)
		button.place(x = 17, y = 135)

		button = Button(window, text = "Cancel", command = window.quit, width = 8 , bg = "#4658E0" , fg="white", highlightthickness=0, borderwidth=0)
		button.place(x = 385, y = 135)	

	button = Button(window, text = "Forget Password", command = reset_password, width = 15 , bg = "#4658E0", fg="white", highlightthickness=0, borderwidth=0)
	button.place(x = 121, y = 200)

	button = Button(window, text = "Cancel", command = window.quit, width = 8 , bg = "#4658E0" , fg="white", highlightthickness=0, borderwidth=0)
	button.place(x = 390, y = 200)

def new_password():
	window.geometry("500x307")
	window.title("SafePass - New Vault")

	lbl1 = Label(window, text = "Create New Vault", font=("Manjari Thin", 30), bg = "#23262B", fg="white")
	lbl1.place(x = 35, y = 22)

	lbl2 = Label(window, text = "Enter first name: ", font=("Alef", 12), bg = "#23262B", fg="white")
	lbl2.place(x = 35, y = 80)
	
	txt1 = Entry(window, width = 33, bg="#1D1B19", fg="white", highlightthickness=0, borderwidth=0)
	txt1.place(x = 190, y = 84)
	txt1.focus()

	lbl2 = Label(window, text = "Enter last name: ", font=("Alef", 12), bg = "#23262B", fg="white")
	lbl2.place(x = 35, y = 115)

	txt2 = Entry(window, width = 33, bg="#1D1B19", fg="white", highlightthickness=0, borderwidth=0)
	txt2.place(x = 190, y = 119)

	lbl2 = Label(window, text = "Enter your E-mail: ", font=("Alef", 12), bg = "#23262B", fg="white")
	lbl2.place(x = 35, y = 150)

	txt3 = Entry(window, width = 33, bg="#1D1B19", fg="white", highlightthickness=0, borderwidth=0)
	txt3.place(x = 190, y = 154)

	lbl2 = Label(window, text = "Enter a password: ", font=("Alef", 12), bg = "#23262B", fg="white")
	lbl2.place(x = 35, y = 185)

	txt4 = Entry(window, width = 33, bg="#1D1B19", fg="white", highlightthickness=0, borderwidth=0)
	txt4.place(x = 190, y = 189)

	lbl2 = Label(window, text = "Re-enter Password: ", font=("Alef", 12), bg = "#23262B", fg="white")
	lbl2.place(x = 35, y = 220)

	txt5 = Entry(window, width = 33, bg="#1D1B19", fg="white", highlightthickness=0, borderwidth=0)
	txt5.place(x = 190, y = 224)

		# tkinter.messagebox.showinfo("Warning!",  "Incorrect Password")
		# elif key == new_key:
		# 	password_vault()

	def check_new_credentials():
		if "".__eq__(txt1.get()) or "".__eq__(txt2.get()) or "".__eq__(txt3.get()) or "".__eq__(txt4.get()) or "".__eq__(txt5.get()):
			tkinter.messagebox.showinfo("Warning!", "Enter all the fields")

		elif txt4.get() != txt5.get():
			tkinter.messagebox.showinfo("Warning!", "Passwords do not match\nEnter again")

		else:
			save_new_credentials()

	def save_new_credentials():
		fname = txt1.get()
		lname = txt2.get()
		email = txt3.get()
		#password1 = txt4.get()
		password2 = txt5.get()

		user_credentials = {
			"fname" : fname,
			"lname" : lname,
			"email" : email
		}

		user_metadata.insert_one(user_credentials)

		salt = os.urandom(32)
		salt = str(salt)
		key = hashlib.pbkdf2_hmac('sha256', password2.encode('utf-8'), salt.encode('utf-8'), 1000000)
		key = str(key)

		keyring.set_password("safepass", fname, salt)
		keyring.set_password("safepass", lname, key)
		
		for widget in window.winfo_children():
			widget.destroy()
		
		first_window()

	button = Button(window, text = "Ok",command = check_new_credentials ,width = 8 , bg = "#4658E0", fg="white", highlightthickness=0, borderwidth=0)
	button.place(x = 285, y = 265)

	button = Button(window, text = "Help", command = help, width = 8 , bg = "#4658E0", fg="white", highlightthickness=0, borderwidth=0)
	button.place(x = 17, y = 265)	

	button = Button(window, text = "Cancel", command = window.quit, width = 8 , bg = "#4658E0" , fg="white", highlightthickness=0, borderwidth=0)
	button.place(x = 395, y = 265)

def check_collection():
	check_me = "userdata"
	if check_me in db.list_collection_names():
		first_window()
	else:
		new_password()

def change_master_password():
	for widget in window.winfo_children():
		widget.destroy()

	window.geometry("500x207")
	window.title("SafePass - Reset Password")
	lbl1 = Label(window, text = "Resetting Password", font=("Manjari Thin", 30), bg = "#23262B", fg="white")
	lbl1.place(x = 35, y = 22)

	lbl2 = Label(window, text = "Enter New Password: ", font=("Alef", 12), bg = "#23262B", fg="white")
	lbl2.place(x = 35, y = 80)
	
	txt1 = Entry(window, width = 30, bg="#1D1B19", fg="white", highlightthickness=0, borderwidth=0)
	txt1.place(x = 220, y = 84)
	txt1.focus()

	lbl2 = Label(window, text = "Re-enter Password: ", font=("Alef", 12), bg = "#23262B", fg="white")
	lbl2.place(x = 35, y = 115)

	txt2 = Entry(window, width = 30, bg="#1D1B19", fg="white", highlightthickness=0, borderwidth=0)
	txt2.place(x = 220, y = 119)

	def set_new_password():
		salt = os.urandom(32)
		salt = str(salt)
		key = hashlib.pbkdf2_hmac('sha256', txt1.get().encode('utf-8'), salt.encode('utf-8'), 1000000)
		key = str(key)

		for x in user_metadata.find({},{ "_id": 0 }):
			fname = x["fname"]
			lname = x["lname"]

		keyring.set_password("safepass", fname, salt)
		keyring.set_password("safepass", lname, key)

		for widget in window.winfo_children():
			widget.destroy()
		
		first_window()
		#tkinter.messagebox.showinfo("Success!", "Passwords reset successful\nRestart the application & login")

	button = Button(window, text = "Ok",command = set_new_password ,width = 8 , bg = "#4658E0", fg="white", highlightthickness=0, borderwidth=0)
	button.place(x = 285, y = 165)

	button = Button(window, text = "Help", command = help, width = 8 , bg = "#4658E0", fg="white", highlightthickness=0, borderwidth=0)
	button.place(x = 17, y = 165)

	button = Button(window, text = "Cancel", command = window.quit, width = 8 , bg = "#4658E0" , fg="white", highlightthickness=0, borderwidth=0)
	button.place(x = 395, y = 165)

#-----------------------------------------------------------------------------------------------------------------------------#

window = Tk()
length = IntVar()
window.configure(bg='#23262B')

#first_window()
password_vault()
#check_collection()
#change_master_password()

def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))
#window.bind('<Motion>', motion)

window.mainloop()