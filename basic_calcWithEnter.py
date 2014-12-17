from tkinter import Tk, Label, Entry, Button, END
from tkinter.messagebox import showinfo

# This function takes an Entry widget as a parameter
# It evaluates the expression in the widget and replaces
# the expression with the result of the evaluation
def evaluate(entry):
    try:
        val = entry.get()
        result = eval(val)
        entry.delete(0,END)
        entry.insert(END, result)
    except:
        showinfo(title="Notification", message="Cannot compute: {}".format(val))
        entry.delete(0,END)

# Define the main function
def main():
    root = Tk()
    root.title('Basic calculator')

    Label(root, text="Enter an arithmetic expression:").grid(row=0,column=0, columnspan=2)

    ent = Entry(root)
    # Make the entry evaluate upon return
    # The e is the event triggered by the return which we ignore
    ent.bind("<Return>", lambda e: evaluate(ent))
    ent.grid(row=1, column=0, columnspan=2)

    Button(master=root, text="Evaluate", command=lambda: evaluate(ent)).grid(row=2, column=0)
    Button(root, text="Clear", command=lambda: ent.delete(0, END)).grid(row=2, column=1)
    
    root.mainloop()

# Call the main function
main()
