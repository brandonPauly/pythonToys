# CSC 242-603
# Midterm
# Brandon Pauly



from tkinter import Label, Entry, Button, END, Frame, RIGHT, LEFT
from tkinter.messagebox import showinfo
            
# Question 1
class Collection(object):
    'an object to hold a collection of items'
    def __init__(self, m = 10):
        'the constructor'
        self.max = m
        self.items = list()

    # Write this method
    def add(self, item):
        'add an item to the collection'
        if len(self.items)== self.max:
            raise OverCapacityError('Maximum capacity reached. Item {} not added.'.format(item))
        elif self.__contains__(item)== True:
            raise DuplicateError('Item already in collection. Item {} not added.'.format(item))
        else:
            self.items.append(item)

##        if len(self.items) < self.max:
##            if item not in self.items:
##                self.items.append(item)
##            else:
##                raise DuplicateError('...')
##        else:
##            raise OverCapacityError('...')
        
            
    # Write this method
    def __contains__(self, item):
        'returns True if item is in the collection and False otherwise'
        if item in self.items:
            return True
        else:
            return False
        #return item in self.items (would have been better)

    def __str__(self):
        'return a string representing the object'
        return str(self.items)

    def __repr__(self):
        'return the canonical representation of the object'
        return repr(self.items)

# The exception classes -- do not modify these
class CollectionError(Exception):
    'the base class for Collection exceptions'

    def __init__(self, m):
        'the constructor'
        self.message = m

    def __str__(self):
        'return a string representing the exception'
        return str(self.message)

class OverCapacityError(CollectionError):
    'the exception for overcapacity collections'

    def __repr__(self):
        'return the canonical representation of the exception'
        return "OverCapacityError({})".format(self.message)

class DuplicateError(CollectionError):
    'the exception for duplicated items'

    def __repr__(self):
        'return the canonical representation of the exception'
        return "DuplicateError({})".format(self.message)

# Question 2
class Memorabilia(Collection):
    'a class for a memorabilia collection'

    def __init__(self, m = 10, v = 10):
        'the constructor'
        Collection.__init__(self, m)
        self.value = v
        self.profit = 0

    # Write this method
    def sell(self, item):
        'if a book is in the library, borrow it'
        if item in self.items:
            self.items.remove(item)
            #self.profit+=eval(repr(self.value))
            self.profit+=self.value
        else:
            raise UnavailableError('{} could not be found in the collection'.format(item))

        

    # Write this method
    def __iter__(self):
        'an iterator for the Library class'
        return self.items.__reversed__()

# The exception class -- do not modify this
class UnavailableError(CollectionError):
    'an exception raised when an attempt to sell a non-existent item is made'

    def __repr__(self):
        'return the canonical representation of the exception'
        return "UnavailableError({})".format(self.message)

# Question 3
class PlusTwo(Frame):
    def __init__(self):
        'the constructor for the GUI'
        Frame.__init__(self)
        self.make_widgets()
        self.pack()
    
    def make_widgets(self):
        'create the widgets for the GUI'
        Label(self, text="Please enter a numeric expression:").pack()

        self.ent = Entry(self)
        self.ent.pack()

        Button(self, text="+2", command=self.addtwo).pack(side=LEFT)
        Button(self, text="Clear", command=lambda: self.ent.delete(0, END)).pack(side=RIGHT)

    # Write this method
    def addtwo(self):
        'the event handler for the +2 button'
        try:
            val=eval(self.ent.get())
            res=val+2
            self.ent.delete(0,END)
            self.ent.insert(END,res)
        except:
            showinfo(title='Error',message='You need to enter numeric values!')
            self.ent.delete(0,END)
