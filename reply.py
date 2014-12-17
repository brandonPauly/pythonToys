from tkinter import Button, Tk
from tkinter.messagebox import showinfo

# The event-handler for button clicks
def reply():
    showinfo(title='Button', message='Button pressed!')

# The master window
root = Tk()

# A slave widget representing a button
widget = Button(master = root, text="Press here", command=reply)

# Place the button into the master window
widget.pack()

# Invoke the main loop on the master window
root.mainloop()
