from tkinter import Tk, Label, Entry, Button, TOP, LEFT
from tkinter.messagebox import showinfo

def reply(name):
    showinfo(title='Reply', message='Hello {}!'.format(name))

# Define the main function
def main():
    top = Tk()
    top.title('Echo')

    Label(top, text="Enter your name:").pack(side=TOP)

    ent = Entry(top)
    ent.pack(side=TOP)

##    cmd = lambda: reply(ent.get())
    #could also have this as a function in this context

    btn=Button(top, text="Submit", command=lambda: reply(ent.get()))

    btn.pack(side=LEFT)

    top.mainloop()

# Call the main function
main()
