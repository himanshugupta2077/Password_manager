from functools import partial
from tkinter import *
import webbrowser
from tkHyperlinkManager import *

root = Tk()
text = Text()
text.pack()
hyperlink = HyperlinkManager(text)
text.insert(INSERT, "Hello, ")
text.insert(INSERT, "Stack Overflow",
            hyperlink.add(partial(webbrowser.open, "http://stackoverflow.com")))
text.insert(INSERT, "!\n\n")
text.insert(INSERT, "And here's ")
text.insert(INSERT, "a search engine",
            hyperlink.add(partial(webbrowser.open, "http://duckduckgo.com")))
text.insert(INSERT, ".")

root.mainloop()