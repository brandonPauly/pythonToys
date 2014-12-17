# CSC 242, Spring 2013
# Lab 5 template
# Brandon Pauly

from tkinter import Label, Tk, Entry, Button, END, RIDGE

def dial(key, entry):
    'handle the dial of a number'
    curr=len(entry.get())
    result=str(key)
    if curr > 11:
        entry.delete(0,END)
    elif curr==3 or curr==7:
        entry.insert(END,'-')
        entry.insert(END,result)
    else:
        entry.insert(END,result)

    

def make_window():
    'create the window and widgets for the dialpad'
    root = Tk()
    
    labels = [['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9'],
            ['*', '0', '#']]

    # Add the text entry
    numEntry = Entry(master = root)
    numEntry.grid(row = 0, column = 0, columnspan=2)

    # Add the buttons
    for r in range(4):
        for c in range(3):
            cmd = lambda x = labels[r][c]: dial(x, numEntry)
            rel = 'ridge'
            Button(root, text = labels[r][c], width=8,relief=rel, command = cmd).grid(row=r+1, column=c)

    root.mainloop()
