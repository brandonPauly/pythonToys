from tkinter import Button, Tk
from tkinter.messagebox import showinfo

def reply00():
    showinfo(title='popup', message='Button00 pressed!')
def reply01():
    showinfo(title='popup', message='Button01 pressed!')
def reply10():
    showinfo(title='popup', message='Button10 pressed!')
def reply11():
    showinfo(title='popup', message='Button11 pressed!')
    
root = Tk()

b1 = Button(root, text="00", width = 10, command=reply00)
b1.grid(row=0,column=0)
Button(root, text="01", width=10,command=reply01).grid(row=0,column=1)
Button(root, text="10", width=10,command=reply10).grid(row=1,column=0)
Button(root, text="11", width=10,command=reply11).grid(row=1,column=1)

root.mainloop()
