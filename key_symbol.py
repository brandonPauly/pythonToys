from tkinter import Tk, Text

def reportEvent(event):
    print('keysym={}, keysym_num={}'.format(event.keysym, event.keysym_num))
def makeWindow():
    root = Tk()
    root.title("Keysym Logger")
                    
    text=Text(root, width=20, height=5, highlightthickness=2)
            
    text.bind('<KeyPress>', reportEvent)

    text.pack(expand=1, fill="both")
    root.mainloop()
