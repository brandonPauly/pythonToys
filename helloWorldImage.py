from tkinter import Label, Tk, PhotoImage
#import tkinter

# Create a GUI window
root = Tk()

photo=PhotoImage(file='peace.gif')

# Create a Label widget in the master window
widget = Label(master = root, image = photo)

# Place the Label widget into the master window
widget.pack()

# Invoke the main loop on the master window
root.mainloop()
