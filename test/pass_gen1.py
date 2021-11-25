import random
import pyperclip
from tkinter import *
from tkinter.ttk import *
from array import *

def pass_gen():
    root = Tk()
    var1 = IntVar()

    root.title("Password Generator")

    lbl0 = Label(root, text = "Password")
    lbl0.grid(row = 0)
    ent0 = Entry(root)
    ent0.grid(row = 0, column = 1)

    lbl1 = Label(root, text = "Length")
    lbl1.grid(row = 1)

    def generate_password():
        password = calc_password()
        print(password)
        ent0.insert(10, password)

    def calc_password():
        ent0.delete(0, END)    
        
        MAX_LEN = var1.get()

        # declare arrays of the character that we need in out password
        # Represented as chars to enable easy string concatenation
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
        
        # combines all the character arrays above to form one array
        COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
        
        # randomly select at least one character from each character set above
        rand_digit = random.choice(DIGITS)
        rand_upper = random.choice(UPCASE_CHARACTERS)
        rand_lower = random.choice(LOCASE_CHARACTERS)
        rand_symbol = random.choice(SYMBOLS)
        
        # combine the character randomly selected above
        # at this stage, the password contains only 4 characters but 
        # we want a 12-character password
        temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

        # now that we are sure we have at least one character from each
        # set of characters, we fill the rest of
        # the password length by selecting randomly from the combined 
        # list of character above.
        temp_pass_list = []
        for x in range(MAX_LEN - 4):
            temp_pass = temp_pass + random.choice(COMBINED_LIST)
        
            # convert temporary password into array and shuffle to 
            # prevent it from having a consistent pattern
            # where the beginning of the password is predictable
            temp_pass_list = list(temp_pass)
            random.shuffle(temp_pass_list)
        
        # traverse the temporary password array and append the chars
        # to form the password
        password = ""
        for x in temp_pass_list:
                password = password + x

        return password

    generate_button = Button(root, text="Generate", command = generate_password)
    generate_button.grid(row = 0, column = 2)

    def copy_password():
        password = ent0.get()
        pyperclip.copy(password)

    copy_button = Button(root, text="Copy", command = copy_password)
    copy_button.grid(row = 1, column = 2)

    combo = Combobox(root, textvariable=var1)
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
    combo.grid(column=1, row=1)

    root.mainloop()

pass_gen()