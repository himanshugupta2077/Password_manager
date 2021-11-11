#-------------------------------IMPORTS-------------------------------------#
from tkinter import *
from tkinter import messagebox
import random
import pyperclip

#---------------------------PASSWORD-GENERATOR----------------------------------#
def generate_password():
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	symbols = ['!','#','$','%','&','(',')','*','+']

	nr_letters = random.randint(8,10)
	nr_symbols = random.randint(2,4)
	nr_numbers = random.randint(2,4)

	password_letters = [random.choice(letters) for _ in range(nr_letters)]
	password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
	password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

	password_list = password_letters + password_numbers + password_symbols
	random.shuffle(password_list)

	password = "".join(password_list)
	password_entry.insert(0, password)

	pyperclip.copy(password)

#----------------------------SAVE-PASSWORD-------------------------------------#

def save():
	website = website_entry.get()
	email = email_entry.get()
	password = password_entry.get()

	if len(website) == 0 or len(password) == 0:
		messagebox.showinfo(title = "Error", message = "Please make sure every field is filled correctly!")

	is_ok = messagebox.askokcancel(title = website, message = f"These are details entered: \n{email} \nPassword: {password}")

	if is_ok :
		with open("data.txt", "a") as data_file:
			data_file.write(f"{website} | {email} | {password}\n")
			website_entry.delete(0, END)
			password_entry.delete(0, END)


#-------------------------------UI-SETUP-------------------------------------#
window = Tk()
window.title("Password Manager")
window.config(padx = 40, pady = 50)

canvas = Canvas(height = 200, width = 200)
logo_img = PhotoImage(file = "password.png")
canvas.create_image(138, 100, image = logo_img)
canvas.grid(row = 0, column = 1)

# Labels:
website_label = Label(text = "Website: ")
website_label.grid(row = 1, column = 0)
email_label = Label(text = "Email: ")
email_label.grid(row = 2, column = 0)
password_label = Label(text = "Password: ")
password_label.grid(row = 3, column = 0)

# Enteries:
website_entry = Entry(width = 35)
website_entry.grid(row = 1, column = 1, columnspan = 2)
email_entry = Entry(width = 35)
email_entry.grid(row = 2, column = 1, columnspan = 2)
# email_entry.insert(0, "myemailID")
password_entry = Entry(width = 17)
password_entry.grid(row = 3, column = 1,)

# Buttons:
generate_password = Button(text = "Generate Password", command = generate_password)
generate_password.grid(row = 3, column = 2)
add_button = Button(text = "Add", command = save)
add_button.grid(row = 4, column = 1)

window.mainloop()