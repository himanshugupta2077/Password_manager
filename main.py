# ----------------------------------------------------------------------------------------------------------------------------#
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
from tkinter import ttk
import re

# --------------------------------------------------------------------------------------------------------------------------#
client = MongoClient()
db = client.password_manager
userdata = db.userdata
user_metadata = db.user_metadata


def password_vault():
    window.geometry("530x560")

    window.title("Vault")
    for widget in window.winfo_children():
        widget.destroy()
    add_new_entry()


def add_new_entry():
    for widget in window.winfo_children():
        widget.destroy()

    window.title("SafePass - Add New Entry")

    lbl1 = Label(
        window,
        text="Add New Entry",
        font=("Manjari Thin", 30),
        bg="#23262B",
        fg="white",
    )
    lbl1.place(x=30, y=22)

    button1 = Button(
        window,
        text="Add new entry",
        command=add_new_entry,
        width=14,
        bg="#4658E0",
        fg="white",
        highlightthickness=0,
        borderwidth=0,
    )
    button1.place(x=15, y=80)

    button2 = Button(
        window,
        text="View saved entry",
        command=view_saved_entry,
        width=14,
        bg="#4658E0",
        fg="white",
        highlightthickness=0,
        borderwidth=0,
    )
    button2.place(x=195, y=80)

    button3 = Button(
        window,
        text="Options",
        command=options,
        width=14,
        bg="#4658E0",
        fg="white",
        highlightthickness=0,
        borderwidth=0,
    )
    button3.place(x=377, y=80)

    button = Button(
        window,
        text="Cancel",
        command=window.quit,
        width=10,
        bg="#4658E0",
        fg="white",
        highlightthickness=0,
        borderwidth=0,
    )
    button.place(x=405, y=520)

    button = Button(
        window,
        text="Help",
        command=help,
        width=10,
        bg="#4658E0",
        fg="white",
        highlightthickness=0,
        borderwidth=0,
    )
    button.place(x=13, y=520)

    lbl = Label(
        window, text="Title: ", font=("Great Vibes", 13), bg="#23262B", fg="white"
    )
    lbl.place(x=30, y=130)
    title_entry = Entry(
        window, width=40, bg="#1D1B19", fg="white", highlightthickness=0, borderwidth=0
    )
    title_entry.place(x=135, y=135)
    title_entry.focus()

    lbl = Label(
        window, text="URL: ", font=("Great Vibes", 13), bg="#23262B", fg="white"
    )
    lbl.place(x=30, y=160)
    url_entry = Entry(
        window, width=40, bg="#1D1B19", fg="white", highlightthickness=0, borderwidth=0
    )
    url_entry.place(x=135, y=165)

    lbl = Label(
        window, text="Username: ", font=("Great Vibes", 13), bg="#23262B", fg="white"
    )
    lbl.place(x=30, y=190)
    username_entry = Entry(
        window, width=40, bg="#1D1B19", fg="white", highlightthickness=0, borderwidth=0
    )
    username_entry.place(x=135, y=195)

    lbl = Label(
        window, text="Password: ", font=("Great Vibes", 13), bg="#23262B", fg="white"
    )
    lbl.place(x=30, y=220)
    password_entry = Entry(
        window, width=40, bg="#1D1B19", fg="white", highlightthickness=0, borderwidth=0
    )
    password_entry.place(x=135, y=225)

    def generate_password():
        password = calc_password()
        password_entry.insert(10, password)

    def calc_password():
        password_entry.delete(0, END)

        MAX_LEN = length.get()

        DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        LOCASE_CHARACTERS = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
        ]

        UPCASE_CHARACTERS = [
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "M",
            "N",
            "O",
            "p",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z",
        ]

        SYMBOLS = [
            "@",
            "#",
            "$",
            "%",
            "=",
            ":",
            "?",
            ".",
            "/",
            "|",
            "~",
            ">",
            "*",
            "(",
            ")",
            "<",
        ]

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

    button = Button(
        window,
        text="Generate Password",
        command=generate_password,
        bg="#4658E0",
        fg="white",
        highlightthickness=0,
        borderwidth=0,
    )
    button.place(x=135, y=255)

    combo = Combobox(
        window, textvariable=length, width=4, background="#1D1B19", foreground="black"
    )
    combo["values"] = (
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
        27,
        28,
        29,
        30,
        31,
        32,
        33,
        34,
        35,
        36,
        37,
        38,
        39,
        40,
        41,
        42,
        43,
        44,
        45,
        46,
        47,
        48,
        49,
        50,
        51,
        52,
        53,
        54,
        55,
        56,
        57,
        58,
        59,
        60,
        61,
        62,
        63,
        64,
        65,
        66,
        67,
        68,
        69,
        70,
        71,
        72,
        73,
        74,
        75,
        76,
        77,
        78,
        79,
        80,
        81,
        82,
        83,
        84,
        85,
        86,
        87,
        88,
        89,
        90,
        91,
        92,
        93,
        94,
        95,
        96,
        97,
        98,
        99,
        100,
        101,
        102,
        103,
        104,
        105,
        106,
        107,
        108,
        109,
        110,
        111,
        112,
        113,
        114,
        115,
        116,
        117,
        118,
        119,
        120,
    )
    combo.current(0)
    combo.bind("<<ComboboxSelected>>")
    combo.place(x=468, y=225)

    def copy_password():
        password = password_entry.get()
        pyperclip.copy(password)

    copy_button = Button(
        window,
        text="Copy",
        command=copy_password,
        bg="#4658E0",
        fg="white",
        highlightthickness=0,
        borderwidth=0,
    )
    copy_button.place(x=295, y=255)

    lbl = Label(
        window, text="Note: ", font=("Great Vibes", 13), bg="#23262B", fg="white"
    )
    lbl.place(x=30, y=288)
    note_entry = Text(
        window,
        width=40,
        height=12,
        bg="#1D1B19",
        fg="white",
        highlightthickness=0,
        borderwidth=0,
    )
    note_entry.place(x=135, y=293)

    def save_user_data():
        title = title_entry.get()
        url = url_entry.get()
        username = username_entry.get()
        password = password_entry.get()
        note = note_entry.get("1.0", "end")

        entry = {
            "title": title,
            "url": url,
            "username": username,
            "password": password,
            "note": note,
        }

        userdata.insert_one(entry)
        title_entry.delete(0, END)
        url_entry.delete(0, END)
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        note_entry.delete(1.0, END)
        title_entry.focus()

        tkinter.messagebox.showinfo("Message", "Password successfully added.")

    button = Button(
        window,
        text="Save",
        command=save_user_data,
        width=10,
        bg="#4658E0",
        fg="white",
        highlightthickness=0,
        borderwidth=0,
    )
    button.place(x=275, y=520)


def view_saved_entry():
    window.title("SafePass - View Entry")

    def title_viewer(password):
        root = Tk()
        root.geometry("770x500")
        root.configure(bg="#23262B")
        root.title("SafePass - Details")
        my_query = {"password": password}
        saved_title = userdata.find(my_query)

        for x in saved_title:
            user_title = x["title"]
            user_url = x["url"]
            user_username = x["username"]
            user_password = x["password"]
            user_note = x["note"]

            lbl = Label(
                root, text="Title: ", font=("Great Vibes", 13), bg="#23262B", fg="white"
            )
            lbl.place(x=20, y=15)
            lbl = Label(root, text=user_title, bg="#23262B", fg="white")
            lbl.place(x=130, y=17)

            lbl = Label(
                root, text="URL: ", font=("Great Vibes", 13), bg="#23262B", fg="white"
            )
            lbl.place(x=20, y=50)
            lbl = Label(root, text=user_url, bg="#23262B", fg="white")
            lbl.place(x=130, y=52)
            copy_button = Button(
                root,
                text="Copy URL",
                command=partial(copy_me, user_url),
                width=15,
                bg="#4658E0",
                fg="white",
                highlightthickness=0,
                borderwidth=0,
            )
            copy_button.place(x=600, y=50)
            open_me = Button(
                root,
                text="Open URL",
                command=partial(callback, user_url),
                width=15,
                bg="#4658E0",
                fg="white",
                highlightthickness=0,
                borderwidth=0,
            )
            open_me.place(x=440, y=50)

            lbl = Label(
                root,
                text="Username: ",
                font=("Great Vibes", 13),
                bg="#23262B",
                fg="white",
            )
            lbl.place(x=20, y=85)
            lbl = Label(root, text=user_username, bg="#23262B", fg="white")
            lbl.place(x=130, y=87)
            copy_button = Button(
                root,
                text="Copy Username",
                command=partial(copy_me, user_username),
                width=15,
                bg="#4658E0",
                fg="white",
                highlightthickness=0,
                borderwidth=0,
            )
            copy_button.place(x=600, y=85)

            lbl = Label(
                root,
                text="Passowrd: ",
                font=("Great Vibes", 13),
                bg="#23262B",
                fg="white",
            )
            lbl.place(x=20, y=120)
            lbl = Label(root, text=user_password, bg="#23262B", fg="white")
            lbl.place(x=130, y=122)
            copy_button = Button(
                root,
                text="Copy Password",
                command=partial(copy_me, user_password),
                width=15,
                bg="#4658E0",
                fg="white",
                highlightthickness=0,
                borderwidth=0,
            )
            copy_button.place(x=600, y=120)

            lbl = Label(
                root, text="Note: ", font=("Great Vibes", 13), bg="#23262B", fg="white"
            )
            lbl.place(x=20, y=155)
            lbl = Label(root, text=user_note, bg="#23262B", fg="white")
            lbl.place(x=130, y=157)
            copy_button = Button(
                root,
                text="Copy Note",
                command=partial(copy_me, user_note),
                width=15,
                bg="#4658E0",
                fg="white",
                highlightthickness=0,
                borderwidth=0,
            )
            copy_button.place(x=600, y=155)

        root.mainloop()

    scroll_win = Tk()
    scroll_win.title("SafePass - Saved Passwords")
    scroll_win.geometry("550x600")

    main_frame = Frame(scroll_win)
    main_frame.pack(fill=BOTH, expand=1)

    sec = Frame(main_frame)
    sec.pack(fill=X, side=BOTTOM)
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    y_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    y_scrollbar.pack(side=RIGHT, fill=Y)

    my_canvas.configure(yscrollcommand=y_scrollbar.set)
    my_canvas.bind(
        "<Configure>", lambda e: my_canvas.config(scrollregion=my_canvas.bbox(ALL))
    )

    second_frame = Frame(my_canvas)
    second_frame.configure(bg="#23262B")

    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
    my_canvas.configure(bg="#23262B")

    lbl1 = Label(
        second_frame,
        text="Saved Entry",
        font=("Manjari Thin", 30),
        bg="#23262B",
        fg="white",
    )
    lbl1.grid(row=1, column=1, pady=20, padx=20)

    def destroy_open_vault():
        scroll_win.destroy()

    def delete_me(password):
        my_query = {"password": password}
        userdata.delete_one(my_query)
        tkinter.messagebox.showinfo("Result", "Password Successfully Deleted")
        scroll_win.destroy()
        view_saved_entry()

    def update_me(password):
        my_query = {"password": password}
        saved_title = userdata.find(my_query)

        for x in saved_title:
            title1 = x["title"]
            url1 = x["url"]
            username1 = x["username"]
            password1 = x["password"]
            note1 = x["note"]

        to_be_update = {
            "title": title1,
            "url": url1,
            "username": username1,
            "password": password1,
            "note": note1,
        }

        root2 = Toplevel()
        root2.geometry("530x455")
        root2.title("SafePass - Edit")
        root2.configure(bg="#23262B")

        lbl = Label(
            root2, text="Title: ", font=("Great Vibes", 13), bg="#23262B", fg="white"
        )
        lbl.place(x=30, y=30)
        title_entry = Entry(
            root2,
            width=40,
            bg="#1D1B19",
            fg="white",
            highlightthickness=0,
            borderwidth=0,
        )
        title_entry.place(x=130, y=30)
        title_entry.insert(10, title1)
        title_entry.focus()

        lbl = Label(
            root2, text="URL: ", font=("Great Vibes", 13), bg="#23262B", fg="white"
        )
        lbl.place(x=30, y=60)
        url_entry = Entry(
            root2,
            width=40,
            bg="#1D1B19",
            fg="white",
            highlightthickness=0,
            borderwidth=0,
        )
        url_entry.insert(10, url1)
        url_entry.place(x=130, y=60)

        lbl = Label(
            root2, text="Username: ", font=("Great Vibes", 13), bg="#23262B", fg="white"
        )
        lbl.place(x=30, y=90)
        username_entry = Entry(
            root2,
            width=40,
            bg="#1D1B19",
            fg="white",
            highlightthickness=0,
            borderwidth=0,
        )
        username_entry.insert(10, username1)
        username_entry.place(x=130, y=90)

        lbl = Label(
            root2, text="Password: ", font=("Great Vibes", 13), bg="#23262B", fg="white"
        )
        lbl.place(x=30, y=120)
        password_entry = Entry(
            root2,
            width=40,
            bg="#1D1B19",
            fg="white",
            highlightthickness=0,
            borderwidth=0,
        )
        password_entry.insert(10, password1)
        password_entry.place(x=130, y=120)

        def generate_password():
            password = calc_password()
            password_entry.insert(10, password)

        def calc_password():
            password_entry.delete(0, END)

            MAX_LEN = length.get()

            DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            LOCASE_CHARACTERS = [
                "a",
                "b",
                "c",
                "d",
                "e",
                "f",
                "g",
                "h",
                "i",
                "j",
                "k",
                "m",
                "n",
                "o",
                "p",
                "q",
                "r",
                "s",
                "t",
                "u",
                "v",
                "w",
                "x",
                "y",
                "z",
            ]

            UPCASE_CHARACTERS = [
                "A",
                "B",
                "C",
                "D",
                "E",
                "F",
                "G",
                "H",
                "I",
                "J",
                "K",
                "M",
                "N",
                "O",
                "p",
                "Q",
                "R",
                "S",
                "T",
                "U",
                "V",
                "W",
                "X",
                "Y",
                "Z",
            ]

            SYMBOLS = [
                "@",
                "#",
                "$",
                "%",
                "=",
                ":",
                "?",
                ".",
                "/",
                "|",
                "~",
                ">",
                "*",
                "(",
                ")",
                "<",
            ]

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

        button = Button(
            root2,
            text="Generate Password",
            command=generate_password,
            bg="#4658E0",
            fg="white",
            highlightthickness=0,
            borderwidth=0,
        )
        button.place(x=130, y=150)

        combo = Combobox(root2, textvariable=length, width=4)
        combo["values"] = (
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
            21,
            22,
            23,
            24,
            25,
            26,
            27,
            28,
            29,
            30,
            31,
            32,
            33,
            34,
            35,
            36,
            37,
            38,
            39,
            40,
            41,
            42,
            43,
            44,
            45,
            46,
            47,
            48,
            49,
            50,
            51,
            52,
            53,
            54,
            55,
            56,
            57,
            58,
            59,
            60,
            61,
            62,
            63,
            64,
            65,
            66,
            67,
            68,
            69,
            70,
            71,
            72,
            73,
            74,
            75,
            76,
            77,
            78,
            79,
            80,
            81,
            82,
            83,
            84,
            85,
            86,
            87,
            88,
            89,
            90,
            91,
            92,
            93,
            94,
            95,
            96,
            97,
            98,
            99,
            100,
            101,
            102,
            103,
            104,
            105,
            106,
            107,
            108,
            109,
            110,
            111,
            112,
            113,
            114,
            115,
            116,
            117,
            118,
            119,
            120,
        )
        combo.current(0)
        combo.bind("<<ComboboxSelected>>")
        combo.place(x=468, y=120)

        def copy_password():
            password = password_entry.get()
            pyperclip.copy(password)

        copy_button = Button(
            root2,
            text="Copy",
            command=copy_password,
            bg="#4658E0",
            fg="white",
            highlightthickness=0,
            borderwidth=0,
        )
        copy_button.place(x=295, y=150)

        lbl = Label(
            root2, text="Note: ", font=("Great Vibes", 13), bg="#23262B", fg="white"
        )
        lbl.place(x=30, y=188)
        note_entry = Text(root2, width=40, height=12, bg="#242424", fg="white")
        note_entry.insert(INSERT, note1)
        note_entry.place(x=130, y=188)

        def update_button():
            title = title_entry.get()
            url = url_entry.get()
            username = username_entry.get()
            password = password_entry.get()
            note = note_entry.get("1.0", "end")

            entry = {
                "$set": {
                    "title": title,
                    "url": url,
                    "username": username,
                    "password": password,
                    "note": note,
                }
            }

            userdata.update_one(to_be_update, entry)
            tkinter.messagebox.showinfo("Result", "Password Updated Successfully")
            root2.destroy()
            scroll_win.destroy()
            view_saved_entry()

        button = Button(
            root2,
            text="Save",
            command=update_button,
            width=10,
            bg="#4658E0",
            fg="white",
            highlightthickness=0,
            borderwidth=0,
        )
        button.place(x=270, y=410)

        button = Button(
            root2,
            text="Cancel",
            command=root2.quit,
            width=10,
            bg="#4658E0",
            fg="white",
            highlightthickness=0,
            borderwidth=0,
        )
        button.place(x=400, y=410)

        root2.mainloop()

    document_list = userdata.find({}, {"_id": 0})
    document_list = list(document_list)

    a = 2
    b = 2
    c = 2

    for x in document_list:
        title = x["title"]
        password = x["password"]

        button1 = Button(
            second_frame,
            text=title.title(),
            command=partial(title_viewer, password),
            width=20,
            bg="#4658E0",
            fg="white",
            highlightthickness=0,
            borderwidth=0,
        )
        button1.grid(row=a, column=1, pady=10, padx=10)
        a += 1

        button1 = Button(
            second_frame,
            text="Delete",
            command=partial(delete_me, password),
            width=10,
            bg="#4658E0",
            fg="white",
            highlightthickness=0,
            borderwidth=0,
        )
        button1.grid(row=b, column=2, pady=10, padx=10)
        b += 1

        button1 = Button(
            second_frame,
            text="Edit",
            command=partial(update_me, password),
            width=10,
            bg="#4658E0",
            fg="white",
            highlightthickness=0,
            borderwidth=0,
        )
        button1.grid(row=c, column=3, pady=10, padx=10)
        c += 1

    scroll_win.mainloop()


def options():
    window.title("SafePass - Options")
    for widget in window.winfo_children():
        widget.destroy()

    lbl1 = Label(
        window, text="Options", font=("Manjari Thin", 30), bg="#23262B", fg="white"
    )
    lbl1.place(x=30, y=22)

    button1 = Button(
        window,
        text="Add new entry",
        command=add_new_entry,
        width=14,
        bg="#4658E0",
        fg="white",
        highlightthickness=0,
        borderwidth=0,
    )
    button1.place(x=15, y=80)

    button2 = Button(
        window,
        text="View saved entry",
        command=view_saved_entry,
        width=14,
        bg="#4658E0",
        fg="white",
        highlightthickness=0,
        borderwidth=0,
    )
    button2.place(x=195, y=80)

    button3 = Button(
        window,
        text="Options",
        command=options,
        width=14,
        bg="#4658E0",
        fg="white",
        highlightthickness=0,
        borderwidth=0,
    )
    button3.place(x=377, y=80)

    button = Button(
        window,
        text="Cancel",
        command=window.quit,
        width=10,
        bg="#4658E0",
        fg="white",
        highlightthickness=0,
        borderwidth=0,
    )
    button.place(x=405, y=520)

    button = Button(
        window,
        text="Help",
        command=help,
        width=10,
        bg="#4658E0",
        fg="white",
        highlightthickness=0,
        borderwidth=0,
    )
    button.place(x=13, y=520)

    button1 = Button(
        window,
        text="Change master password",
        command=change_master_password,
        bg="#4658E0",
        fg="white",
        highlightthickness=0,
        borderwidth=0,
    )
    button1.place(x=30, y=145)


def help():
    root1 = Toplevel()
    root1.geometry("513x300")
    root1.configure(bg="#E0E0E0")
    root1.title("SafePass - About")

    lbl = Label(
        root1, text="SafePass", font=("Great Vibes", 13), bg="#060606", fg="white"
    )
    lbl.place(x=215, y=170)
    lbl = Label(root1, text="1.0", font=("Great Vibes", 13), bg="#060606", fg="white")
    lbl.place(x=241, y=200)
    lbl = Label(
        root1,
        text="SafePass keeps all your Passoword in a Digital Vault",
        font=("Great Vibes", 13),
        bg="#060606",
        fg="white",
    )
    lbl.place(x=25, y=230)
    link = Label(
        root1,
        text="Homepage - Help",
        font=("Great Vibes", 13),
        bg="#4658E0",
        fg="white",
        cursor="hand2",
    )
    link.place(x=180, y=265)
    link.bind("<Button-1>", lambda e: callback("https://zexceed012.github.io"))

    # def new_copy():
    #   pyperclip.copy("https://zexceed012.github.io")
    #   tkinter.messagebox.showinfo("Link Copied!", "Please paste & open the link in your browser.")

    # copy_button = Button(root1, text="Homepage - Help", command = new_copy ,width = 15, bg = "#4658E0", fg="white", highlightthickness=0, borderwidth=0)
    # copy_button.place(x = 180, y = 265)

    global imgq
    imgq = PhotoImage(
        file="/home/user/Documents/STUDIEZ/Projects/04-Password-Manager/Project_files/images/locked.ppm"
    )
    Label(root1, image=imgq).place(x=192, y=10)
    root1.mainloop()


def copy_me(data):
    pyperclip.copy(data)


def callback(url):
    webbrowser.open_new_tab(url)


def first_window():
    window.geometry("500x244")
    window.title("SafePass - Open Vault")

    lbl1 = Label(
        window,
        text="Enter Credentials",
        font=("Manjari Thin", 30),
        bg="#23262B",
        fg="white",
    )
    lbl1.place(x=32, y=22)

    lbl2 = Label(
        window,
        text="Enter first name: ",
        font=("Great Vibes", 13),
        bg="#23262B",
        fg="white",
    )
    lbl2.place(x=32, y=80)

    txt1 = Entry(
        window, width=33, bg="#1D1B19", fg="white", highlightthickness=0, borderwidth=0
    )
    txt1.place(x=190, y=83)
    txt1.focus()

    lbl2 = Label(
        window,
        text="Enter last name: ",
        font=("Great Vibes", 13),
        bg="#23262B",
        fg="white",
    )
    lbl2.place(x=32, y=115)

    txt2 = Entry(
        window, width=33, bg="#1D1B19", fg="white", highlightthickness=0, borderwidth=0
    )
    txt2.place(x=190, y=118)

    lbl2 = Label(
        window,
        text="Enter password: ",
        font=("Great Vibes", 13),
        bg="#23262B",
        fg="white",
    )
    lbl2.place(x=32, y=150)

    txt3 = Entry(
        window,
        width=33,
        show="●",
        bg="#1D1B19",
        fg="white",
        highlightthickness=0,
        borderwidth=0,
    )
    txt3.place(x=190, y=153)

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
        new_key = hashlib.pbkdf2_hmac(
            "sha256", password.encode("utf-8"), salt.encode("utf-8"), 1000000
        )
        new_key = str(new_key)

        if key != new_key:
            tkinter.messagebox.showinfo(
                "Unable to open vault!", "Sorry, that didn't work.\nPlease try again."
            )
        else:
            password_vault()

    button = Button(
        window,
        text="Ok",
        command=check_credentials,
        width=8,
        bg="#4658E0",
        fg="white",
        highlightthickness=0,
        borderwidth=0,
    )
    button.place(x=284, y=200)

    button = Button(
        window,
        text="Help",
        command=help,
        width=8,
        bg="#4658E0",
        fg="white",
        highlightthickness=0,
        borderwidth=0,
    )
    button.place(x=17, y=200)

    def reset_password():
        for widget in window.winfo_children():
            widget.destroy()
        window.geometry("500x180")
        window.title("SafePass - Forgot Password")

        lbl1 = Label(
            window,
            text="Reset Password",
            font=("Manjari Thin", 30),
            bg="#23262B",
            fg="white",
        )
        lbl1.place(x=35, y=28)

        lbl2 = Label(
            window, text="Enter Email-ID: ", font=("Alef", 12), bg="#23262B", fg="white"
        )
        lbl2.place(x=32, y=85)

        txt1 = Entry(
            window,
            width=33,
            bg="#1D1B19",
            fg="white",
            highlightthickness=0,
            borderwidth=0,
        )
        txt1.place(x=170, y=87)
        txt1.focus()

        def send_me_otp():
            entered_email = txt1.get()

            for x in user_metadata.find({}, {"_id": 0}):
                email = x["email"]
                fname = x["fname"]

            if entered_email == email:

                def generateOTP():
                    digits = "0123456789"
                    OTP = ""
                    for i in range(4):
                        OTP += digits[math.floor(random.random() * 10)]

                    return OTP

                def send_otp(otp):
                    port = 587  # For starttls
                    smtp_server = "smtp.gmail.com"
                    sender_email = "safepass.helpdesk@gmail.com"
                    receiver_email = email
                    password = "YOURPASSWORD"
                    message = f"""\
                        Subject: Hi there
                        
                        This message is sent from SafePass.
                        Your OTP is {otp}."""
                    context = ssl.create_default_context()
                    with smtplib.SMTP(smtp_server, port) as server:
                        server.ehlo()  # Can be omitted
                        server.starttls(context=context)
                        server.ehlo()  # Can be omitted
                        server.login(sender_email, password)
                        server.sendmail(sender_email, receiver_email, message)

                otp = generateOTP()
                send_otp(otp)

                for widget in window.winfo_children():
                    widget.destroy()

                lbl1 = Label(
                    window,
                    text="Reset Password",
                    font=("Manjari Thin", 30),
                    bg="#23262B",
                    fg="white",
                )
                lbl1.place(x=40, y=28)

                lbl2 = Label(
                    window,
                    text="Enter OTP: ",
                    font=("Alef", 12),
                    bg="#23262B",
                    fg="white",
                )
                lbl2.place(x=32, y=85)

                txt = Entry(
                    window,
                    width=33,
                    bg="#1D1B19",
                    fg="white",
                    highlightthickness=0,
                    borderwidth=0,
                )
                txt.place(x=170, y=87)
                txt.focus()

                def check_otp():
                    if otp == txt.get():
                        change_master_password()
                    else:
                        tkinter.messagebox.showinfo(
                            "Warning!", "Incorrect OTP\nTry again"
                        )

                button = Button(
                    window,
                    text="Ok",
                    command=check_otp,
                    width=8,
                    bg="#4658E0",
                    fg="white",
                    highlightthickness=0,
                    borderwidth=0,
                )
                button.place(x=282, y=135)

                def just_send_it():
                    def generateOTP():
                        digits = "0123456789"
                        OTP = ""
                        for i in range(4):
                            OTP += digits[math.floor(random.random() * 10)]

                        return OTP

                    def send_otp(otp):
                        port = 587  # For starttls
                        smtp_server = "smtp.gmail.com"
                        sender_email = "safepass.helpdesk@gmail.com"
                        receiver_email = email
                        password = "M8*5wbYCECzNdf!vPZ#jywJ3*zs*XFe8!hVERTfWS&R"
                        message = f"""\
                        Subject: Hi there
                        
                        This message is sent from SafePass.
                        Your OTP is {otp}."""
                        context = ssl.create_default_context()
                        with smtplib.SMTP(smtp_server, port) as server:
                            server.ehlo()  # Can be omitted
                            server.starttls(context=context)
                            server.ehlo()  # Can be omitted
                            server.login(sender_email, password)
                            server.sendmail(sender_email, receiver_email, message)

                    otp = generateOTP()
                    send_otp(otp)

                button = Button(
                    window,
                    text="Send again",
                    command=just_send_it,
                    width=8,
                    bg="#4658E0",
                    fg="white",
                    highlightthickness=0,
                    borderwidth=0,
                )
                button.place(x=182, y=135)

                button = Button(
                    window,
                    text="Help",
                    command=help,
                    width=8,
                    bg="#4658E0",
                    fg="white",
                    highlightthickness=0,
                    borderwidth=0,
                )
                button.place(x=17, y=135)

                button = Button(
                    window,
                    text="Cancel",
                    command=window.quit,
                    width=8,
                    bg="#4658E0",
                    fg="white",
                    highlightthickness=0,
                    borderwidth=0,
                )
                button.place(x=385, y=135)

            else:
                tkinter.messagebox.showinfo(
                    "Warning!", "Enter Registered Email-ID\nTry again"
                )

        button = Button(
            window,
            text="Send OTP",
            command=send_me_otp,
            width=8,
            bg="#4658E0",
            fg="white",
            highlightthickness=0,
            borderwidth=0,
        )
        button.place(x=282, y=135)

        button = Button(
            window,
            text="Help",
            command=help,
            width=8,
            bg="#4658E0",
            fg="white",
            highlightthickness=0,
            borderwidth=0,
        )
        button.place(x=17, y=135)

        button = Button(
            window,
            text="Cancel",
            command=window.quit,
            width=8,
            bg="#4658E0",
            fg="white",
            highlightthickness=0,
            borderwidth=0,
        )
        button.place(x=385, y=135)

    button = Button(
        window,
        text="Forget Password",
        command=reset_password,
        width=15,
        bg="#4658E0",
        fg="white",
        highlightthickness=0,
        borderwidth=0,
    )
    button.place(x=121, y=200)

    button = Button(
        window,
        text="Cancel",
        command=window.quit,
        width=8,
        bg="#4658E0",
        fg="white",
        highlightthickness=0,
        borderwidth=0,
    )
    button.place(x=390, y=200)


def new_identity():
    window.geometry("500x307")
    window.title("SafePass - New Vault")

    lbl1 = Label(
        window,
        text="Create New Vault",
        font=("Manjari Thin", 30),
        bg="#23262B",
        fg="white",
    )
    lbl1.place(x=35, y=22)

    lbl2 = Label(
        window, text="Enter first name: ", font=("Alef", 12), bg="#23262B", fg="white"
    )
    lbl2.place(x=35, y=80)

    txt1 = Entry(
        window, width=33, bg="#1D1B19", fg="white", highlightthickness=0, borderwidth=0
    )
    txt1.place(x=196, y=83)
    txt1.focus()

    lbl2 = Label(
        window, text="Enter last name: ", font=("Alef", 12), bg="#23262B", fg="white"
    )
    lbl2.place(x=35, y=115)

    txt2 = Entry(
        window, width=33, bg="#1D1B19", fg="white", highlightthickness=0, borderwidth=0
    )
    txt2.place(x=196, y=118)

    lbl2 = Label(
        window, text="Enter your E-mail: ", font=("Alef", 12), bg="#23262B", fg="white"
    )
    lbl2.place(x=35, y=150)

    txt3 = Entry(
        window, width=33, bg="#1D1B19", fg="white", highlightthickness=0, borderwidth=0
    )
    txt3.place(x=196, y=153)

    lbl2 = Label(
        window, text="Enter a password: ", font=("Alef", 12), bg="#23262B", fg="white"
    )
    lbl2.place(x=35, y=185)

    txt4 = Entry(
        window, width=33, bg="#1D1B19", fg="white", highlightthickness=0, borderwidth=0
    )
    txt4.place(x=196, y=188)

    lbl2 = Label(
        window, text="Re-enter Password: ", font=("Alef", 12), bg="#23262B", fg="white"
    )
    lbl2.place(x=35, y=220)

    txt5 = Entry(
        window, width=33, bg="#1D1B19", fg="white", highlightthickness=0, borderwidth=0
    )
    txt5.place(x=196, y=223)

    def check_new_credentials():
        s = txt4.get()

        def uppercase_check(password):
            if re.search("[A-Z]", password):  # atleast one uppercase character
                return False
            return True

        def lowercase_check(password):
            if re.search("[a-z]", password):  # atleast one lowercase character
                return False
            return True

        def digit_check(password):
            if re.search("[0-9]", password):  # atleast one digit
                return False
            return True

        if (
            "".__eq__(txt1.get())
            or "".__eq__(txt2.get())
            or "".__eq__(txt3.get())
            or "".__eq__(txt4.get())
            or "".__eq__(txt5.get())
        ):
            tkinter.messagebox.showinfo("Error!", "Enter all the fields")

        elif len(txt4.get()) < 8:
            tkinter.messagebox.showinfo(
                "Error!",
                "Password should be longer than 8 characters. Please try again.",
            )

        elif uppercase_check(s):
            tkinter.messagebox.showinfo("Error!", "No uppercase char found.")

        elif lowercase_check(s):
            tkinter.messagebox.showinfo("Error!", "No lowercase char found.")

        elif digit_check(s):
            tkinter.messagebox.showinfo("Error!", "No digits found.")

        elif txt4.get() != txt5.get():
            tkinter.messagebox.showinfo(
                "Error!", "Passwords do not match\nPlease try again"
            )

        else:
            tkinter.messagebox.showinfo(
                "Message", "New user successfully added. Please login to continue."
            )
            save_new_credentials()

    def save_new_credentials():
        fname = txt1.get()
        lname = txt2.get()
        email = txt3.get()
        # password1 = txt4.get()
        password2 = txt5.get()

        user_credentials = {"fname": fname, "lname": lname, "email": email}

        user_metadata.insert_one(user_credentials)

        salt = os.urandom(32)
        salt = str(salt)
        key = hashlib.pbkdf2_hmac(
            "sha256", password2.encode("utf-8"), salt.encode("utf-8"), 1000000
        )
        key = str(key)

        keyring.set_password("safepass", fname, salt)
        keyring.set_password("safepass", lname, key)

        for widget in window.winfo_children():
            widget.destroy()

        first_window()

    button = Button(
        window,
        text="Ok",
        command=check_new_credentials,
        width=8,
        bg="#4658E0",
        fg="white",
        highlightthickness=0,
        borderwidth=0,
    )
    button.place(x=285, y=265)

    button = Button(
        window,
        text="Help",
        command=help,
        width=8,
        bg="#4658E0",
        fg="white",
        highlightthickness=0,
        borderwidth=0,
    )
    button.place(x=17, y=265)

    button = Button(
        window,
        text="Cancel",
        command=window.quit,
        width=8,
        bg="#4658E0",
        fg="white",
        highlightthickness=0,
        borderwidth=0,
    )
    button.place(x=395, y=265)


def check_collection():
    check_me = "userdata"
    if check_me in db.list_collection_names():
        first_window()
    else:
        new_identity()


def change_master_password():
    for widget in window.winfo_children():
        widget.destroy()

    window.geometry("500x207")
    window.title("SafePass - Reset Password")
    lbl1 = Label(
        window,
        text="Resetting Password",
        font=("Manjari Thin", 30),
        bg="#23262B",
        fg="white",
    )
    lbl1.place(x=35, y=22)

    lbl2 = Label(
        window, text="Enter New Password: ", font=("Alef", 12), bg="#23262B", fg="white"
    )
    lbl2.place(x=35, y=80)

    txt1 = Entry(
        window, width=30, bg="#1D1B19", fg="white", highlightthickness=0, borderwidth=0
    )
    txt1.place(x=220, y=84)
    txt1.focus()

    lbl2 = Label(
        window, text="Re-enter Password: ", font=("Alef", 12), bg="#23262B", fg="white"
    )
    lbl2.place(x=35, y=115)

    txt2 = Entry(
        window, width=30, bg="#1D1B19", fg="white", highlightthickness=0, borderwidth=0
    )
    txt2.place(x=220, y=119)

    def set_new_password():
        salt = os.urandom(32)
        salt = str(salt)
        key = hashlib.pbkdf2_hmac(
            "sha256", txt1.get().encode("utf-8"), salt.encode("utf-8"), 1000000
        )
        key = str(key)

        for x in user_metadata.find({}, {"_id": 0}):
            fname = x["fname"]
            lname = x["lname"]

        keyring.set_password("safepass", fname, salt)
        keyring.set_password("safepass", lname, key)

        for widget in window.winfo_children():
            widget.destroy()

        first_window()
        tkinter.messagebox.showinfo(
            "Success!", "Passwords reset successful\nRestart the application & login"
        )

    button = Button(
        window,
        text="Ok",
        command=set_new_password,
        width=8,
        bg="#4658E0",
        fg="white",
        highlightthickness=0,
        borderwidth=0,
    )
    button.place(x=285, y=165)

    button = Button(
        window,
        text="Help",
        command=help,
        width=8,
        bg="#4658E0",
        fg="white",
        highlightthickness=0,
        borderwidth=0,
    )
    button.place(x=17, y=165)

    button = Button(
        window,
        text="Cancel",
        command=window.quit,
        width=8,
        bg="#4658E0",
        fg="white",
        highlightthickness=0,
        borderwidth=0,
    )
    button.place(x=395, y=165)


# -----------------------------------------------------------------------------------------------------------------------------#

window = Tk()
length = IntVar()
window.configure(bg="#23262B")

# check_collection()
password_vault()
window.mainloop()
