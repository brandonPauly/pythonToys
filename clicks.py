from tkinter import Frame
from tkinter.messagebox import showinfo

def handler(e):
    print('you left clicked at ({}, {})'.format(e.x, e.y))

def handler2(e):
    print('you right clicked at ({}, {})'.format(e.x, e.y))
    
def makeWindow():
    'create GUI'
    frame = Frame(width=100, height=100, background = "blue")
    frame.bind("<Button-1>", handler)
    frame.bind('<Button-3>', handler2)
    frame.pack()
    frame.mainloop()
