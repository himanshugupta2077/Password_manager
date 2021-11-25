#----------------------------------------------------------------------------------------------------------------------------#
from pymongo import MongoClient
from tkinter.ttk import *
from tkinter import *
from PIL import ImageTk, Image
import hashlib
import tkinter.messagebox
import random
import pyperclip
from functools import partial

#----------------------------------------------------------------------------------------------------------------------------#
client = MongoClient()
db = client.password_manager
userdata = db.userdata

def first_window():
	window.geometry("500x245")
	global img
	path = r"/home/user/Documents/STUDIEZ/Projects/04-Password-Manager/Project_files/main/first_window.ppm"
	img = ImageTk.PhotoImage(Image.open(path))
	panel = Label(window, image=img)
	panel.pack(side="top", fill="both")

	window.title("SafePass - Open Database")

	lbl1 = Label(window, text = "Enter Master Password", font=("Arial", 20))
	lbl1.place(x = 110, y = 18)

	lbl2 = Label(window, text = "Master Password: ", font=("Arial", 12))
	lbl2.place(x = 48, y = 110)

	txt = Entry(window, width = 30, show = "●")
	txt.place(x = 190, y = 110)
	txt.focus()

	# canvas=Canvas(window, width=500, height= 400)
	# canvas.place(x = 0, y = 170)
	# canvas.create_line(0, 10, 500, 10, fill="grey", width=1)
	
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

		if "".__eq__(txt.get()):
			tkinter.messagebox.showinfo("Warning!",  "Field cannot be empty!")

		elif key != new_key:
			tkinter.messagebox.showinfo("Warning!",  "Incorrect Password")

		elif key == new_key:
			password_vault()

	button = Button(window, text = "Ok", command = check_password1, width = 8)
	button.place(x = 282, y = 198)

	button = Button(window, text = "Help", command = help, width = 8)
	button.place(x = 17, y = 198)	

	def forget_password():
		pass

	button = Button(window, text = "Forget Password", command = forget_password, width = 15)
	button.place(x = 121, y = 198)

	button = Button(window, text = "Cancel", command = window.quit, width = 8)
	button.place(x = 385, y = 198)

def password_vault():
	window.geometry("530x590")
	
	window.title("Vault")
	for widget in window.winfo_children():
		widget.destroy()
	view_saved_entry()

def add_new_entry():
	#window.geometry("530x590")
	for widget in window.winfo_children():
		widget.destroy()

	global img1
	path = r"/home/user/Documents/STUDIEZ/Projects/04-Password-Manager/Project_files/main/open_pass.ppm"
	img1 = ImageTk.PhotoImage(Image.open(path))
	panel = Label(window, image=img1)
	panel.place(x=0,y=0)

	window.title("SafePass - Add New Entry")

	lbl1 = Label(window, text = "Add New Entry", font=("Arial", 20))
	lbl1.place(x = 100, y = 18)

	button1 = Button(window, text = "Add new entry", command = add_new_entry, width = 14)
	button1.place(x = 13, y = 105)

	button2 = Button(window, text = "View saved entry", command = view_saved_entry, width = 14)
	button2.place(x = 195, y = 105)

	button3 = Button(window, text = "Options", command = options, width = 14)
	button3.place(x = 377, y = 105)

	button = Button(window, text = "Cancel", command = window.quit, width = 10)
	button.place(x = 405, y = 547)

	button = Button(window, text = "Help", command = help, width = 10)
	button.place(x = 13, y = 547)

	lbl = Label(window, text = "Title: ")	
	lbl.place(x = 30, y = 160)
	title_entry = Entry(window, width = 40)
	title_entry.place(x = 130, y = 160)
	title_entry.focus()

	lbl = Label(window, text = "URL: ")
	lbl.place(x = 30, y = 190)
	url_entry = Entry(window, width = 40)
	url_entry.place(x = 130, y = 190)

	lbl = Label(window, text = "Username: ")
	lbl.place(x = 30, y = 220)
	username_entry = Entry(window, width = 40)
	username_entry.place(x = 130, y = 220)

	lbl = Label(window, text = "Password: ")
	lbl.place(x = 30, y = 250)
	password_entry = Entry(window, width = 40)
	password_entry.place(x = 130, y = 250)

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

	button = Button(window, text = "Generate Password", command = generate_password)
	button.place(x = 130, y = 280)
	
	combo = Combobox(window, textvariable = length, width = 4)
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
	combo.place(x = 468, y = 250)
	
	def copy_password():
		password = password_entry.get()
		pyperclip.copy(password)
		
	copy_button = Button(window, text="Copy", command = copy_password)
	copy_button.place(x = 295, y = 280)

	lbl = Label(window, text = "Note: ")
	lbl.place(x = 30, y = 318)
	note_entry = Text(window, width = 40, height = 12)
	note_entry.place(x = 130, y = 318)

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

	button = Button(window, text = "Save", command = save_user_data, width = 10)
	button.place(x = 275, y = 547)

def view_saved_entry():
	window.title("SafePass - View Entry")
	for widget in window.winfo_children():
		widget.destroy()

	global img1
	path = r"/home/user/Documents/STUDIEZ/Projects/04-Password-Manager/Project_files/main/view_pass.ppm"
	img1 = ImageTk.PhotoImage(Image.open(path))
	panel = Label(window, image=img1)
	panel.place(x=0,y=0)

	lbl1 = Label(window, text = "Saved Entries", font=("Arial", 20))
	lbl1.place(x = 100, y = 18)

	button1 = Button(window, text = "Add new entry", command = add_new_entry, width = 14)
	button1.place(x = 13, y = 105)

	button2 = Button(window, text = "View saved entry", command = view_saved_entry, width = 14)
	button2.place(x = 195, y = 105)

	button3 = Button(window, text = "Options", command = options, width = 14)
	button3.place(x = 377, y = 105)

	button = Button(window, text = "Cancel", command = window.quit, width = 10)
	button.place(x = 405, y = 547)

	button = Button(window, text = "Help", command = help, width = 10)
	button.place(x = 13, y = 547)

	saved_title = userdata.find({},{"_id": 0})
	saved_title = list(saved_title)

	def title_viewer(password):
		root = Tk()
		root.geometry("1100x500")
		root.configure(bg='#3D3D3D')
		root.title(title.title())
		my_query = {"password": password }
		saved_title = userdata.find(my_query)

		for x in saved_title:
			user_title = x['title']
			user_url = x['url']
			user_username = x['username']
			user_password = x['password']
			user_note = x['note']

			lbl = Label(root, text = "Title: ")
			lbl.place(x = 20, y = 15)
			lbl = Label(root, text = user_title)
			lbl.place(x = 110, y = 15)

			lbl = Label(root, text = "URL: ")
			lbl.place(x = 20, y = 50)
			lbl = Label(root, text = user_url)
			lbl.place(x = 110, y = 50)
			copy_button = Button(root, text="Copy URL", command =  partial(copy_me ,user_url), width = 15)
			copy_button.place(x = 1200, y = 50)

			lbl = Label(root, text = "Username: ")
			lbl.place(x = 20, y = 85)
			lbl = Label(root, text = user_username)
			lbl.place(x = 110, y = 85)
			copy_button = Button(root, text="Copy Username", command =  partial(copy_me ,user_username),width = 15)
			copy_button.place(x = 1200, y = 85)

			lbl = Label(root, text = "Passowrd: ")
			lbl.place(x = 20, y = 120)
			lbl = Label(root, text = user_password)
			lbl.place(x = 110, y = 120)
			copy_button = Button(root, text="Copy Password", command =  partial(copy_me ,user_password),width = 15)
			copy_button.place(x = 1200, y = 120)

			lbl = Label(root, text = "Note: ")
			lbl.place(x = 20, y = 155)
			lbl = Label(root, text = user_note)
			lbl.place(x = 110, y = 155)
			copy_button = Button(root, text="Copy Note", command =  partial(copy_me ,user_note),width = 15)
			copy_button.place(x = 1200, y = 155)

		root.mainloop()

	x_cor = 18
	y_cor = 155

	x_cor1 = 410
	y_cor1 = 155

	x_cor2 = 290
	y_cor2 = 155		

	for x in saved_title:
		title = x['title']
		password = x['password']

		button1 = Button(window, text = title.title(), command = partial(title_viewer ,password), width = 20)
		button1.place(x = x_cor, y = y_cor )
		y_cor += 43

		button1 = Button(window, text = "Delete", command = partial(delete_me ,password), width = 10)
		button1.place(x = x_cor1, y = y_cor1)
		y_cor1 += 43

		button1 = Button(window, text = "Edit", command = partial(update_me ,password), width = 10)
		button1.place(x = x_cor2, y = y_cor2)
		y_cor2 += 43

def options():
	window.title("SafePass - Options")
	for widget in window.winfo_children():
		widget.destroy()

	global img1
	path = r"/home/user/Documents/STUDIEZ/Projects/04-Password-Manager/Project_files/main/options.ppm"
	img1 = ImageTk.PhotoImage(Image.open(path))
	panel = Label(window, image=img1)
	panel.place(x=0,y=0)	

	lbl1 = Label(window, text = "Options", font=("Arial", 20))
	lbl1.place(x = 100, y = 18)

	button1 = Button(window, text = "Add new entry", command = add_new_entry, width = 14)
	button1.place(x = 13, y = 105)

	button2 = Button(window, text = "View saved entry", command = view_saved_entry, width = 14)
	button2.place(x = 195, y = 105)

	button3 = Button(window, text = "Options", command = options, width = 14)
	button3.place(x = 377, y = 105)

	button = Button(window, text = "Cancel", command = window.quit, width = 10)
	button.place(x = 405, y = 547)

	button = Button(window, text = "Help", command = help, width = 10)
	button.place(x = 13, y = 547)

	def export_data():
		pass

	def import_data():
		pass

	def change_master_password():
		pass

	button1 = Button(window, text = "Export", command = export_data)
	button1.place(x = 18, y = 155)

	button2 = Button(window, text = "Import", command = import_data)
	button2.place(x = 18, y = 195)

	button2 = Button(window, text = "Change master password", command = change_master_password)
	button2.place(x = 18, y = 235)
	
def help():
	root1 = Tk()
	root1.geometry("400x400")
	root1.configure(bg='#3D3D3D')
	root1.title("SafePass - Help")

	def help_button():
		pass

	def about_button():
		pass

	def license_button():
		pass

	button0 = Button(root1, text = "Help", command = help_button, width= 10)
	button0.place(x = 15, y = 15)

	button1 = Button(root1, text = "About", command = about_button, width= 10)
	button1.place(x = 145, y = 15)

	button2 = Button(root1, text = "Licence", command = license_button, width= 10)
	button2.place(x = 275, y = 15)

	root1.mainloop()

def copy_me(data):
	pyperclip.copy(data)

def delete_me(data_id):
	my_query = {"password": data_id}
	userdata.delete_one(my_query)
	view_saved_entry()
	
def update_me(data_id):
	delete_ = {"password": data_id}
	userdata.delete_one(delete_)
	view_saved_entry()

window = Tk()
length = IntVar()
window.configure(bg='#3D3D3D')
#first_window()
#add_new_entry()
password_vault()
#view_saved_entry()
#help()
def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))

#window.bind('<Motion>', motion)
window.mainloop()