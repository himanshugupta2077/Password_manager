#-------------------------------IMPORTS-------------------------------------#
from tkinter import *
import hashlib


#---------------------------PASSWORD-GENERATOR----------------------------------#



#----------------------------SAVE-PASSWORDS (DataBase)-------------------------------------#



#-------------------------------UI-SETUP-------------------------------------#
window = Tk()

window.title("Safe Pass")

def first_screen():
	window.geometry("250x150")

	lbl = Label(window, text = "Create Master Password")
	lbl.config(anchor = CENTER)
	lbl.pack()

	txt = Entry(window, width = 20)
	txt.pack()
	txt.focus()
	txt.focus()

	lbl1 = Label(window, text = "Re-Enter Password: ")
	lbl1.pack()

	txt1 = Entry(window, width = 20)
	txt1.pack()

	lbl2 = Label(window)
	lbl2.pack()

	def save_master_password():
		if txt.get() == txt1.get():
			pass
		else:
			lbl2.config(text = "Passwords do not match")

	button = Button(window, text = "Save", command = save_master_password)
	button.pack(pady = 5)

def login_screen():
	window.geometry("350x150")

	lbl = Label(window, text = "Enter Master Password")
	lbl.config(anchor = CENTER)
	lbl.pack()

	txt = Entry(window, width = 20)
	txt.pack()
	txt.focus()

	lbl1 = Label(window)
	lbl1.pack()

	def check_password():
		password = "test"

		if password == txt.get():
			password_vault()
		else:
			txt.delete(0, 'end')
			lbl1.config(text = "Wrong passoword")


	button = Button(window, text = "Submit", command = check_password)
	button.pack(pady = 5)

def password_vault():
	for widget in window.winfo_children():
		widget.destroy()
	window.geometry("750x350")

	lbl = Label(window, text = "Password Vault")
	lbl.config(anchor = CENTER)
	lbl.pack()

login_screen()
window.mainloop()