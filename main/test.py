from tkinter import * 
 
txtWin = Tk() 
scrollbar = Scrollbar(txtWin) 
scrollbar.pack(side = RIGHT, fill = Y) 
     
area = Text(txtWin, yscrollcommand = scrollbar.set)
area.pack(expand=True, fill='both') 
     
scrollbar.config(command = area.yview) 
txtWin.mainloop()