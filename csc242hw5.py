# CSC 242, Spring
# Assignment 5 template
# Brandon Pauly

from tkinter import Label, Frame, Entry, Button, TOP, LEFT, RIGHT, END, BOTTOM
from tkinter.messagebox import showinfo
from random import randrange

# Question 1
class Game(Frame):
    'Number guessing application'
    def __init__(self,parent=None):
        'constructor'
        Frame.__init__(self, parent)
        self.pack()
        Game.make_widgets(self)
        Game.new_game(self)
        

    def make_widgets(self):
        'defines Game widgets'
        Label(self,text='Enter your guess:').pack()
        self.ent=Entry(self)
        self.ent.pack()
        Button(self,text='Enter',command=self.reply).pack()
        self.ent.bind('<Return>', lambda e: self.reply())

    def new_game(self):
        'starts a new game by choosing secret number'
        self.secNum=randrange(1,101) 

    def reply(self):
        'handles button "Enter" clicks'
        try:
            guess=eval(self.ent.get())
            num=self.secNum
            if guess > num:
                showinfo(title='Report',message='{} is too high!'.format(guess))
            elif guess < num:
                showinfo(title='Report',message='{} is too low!'.format(guess))
            else:
                showinfo(title='Report',message='You got it!')
                Game.new_game(self)
        except:
            showinfo(title='Ooops!',message='Invalid number!')
        self.ent.delete(0,END)


# Question 2
class BMI(Frame):
    'Body Mass Index app'
    def __init__(self,parent=None):
        'constructor'
        Frame.__init__(self, parent)
        self.grid()
        BMI.make_widgets(self)

    def make_widgets(self):
        'defines BMI widgets'
        Label(self,text='Enter your height: ').grid(row=0,column=0)
        self.htEnt=Entry(self)
        self.htEnt.grid(row=0,column=1)
        Label(self,text='Enter your weight: ').grid(row=1,column=0)
        self.wtEnt=Entry(self)
        self.wtEnt.grid(row=1,column=1)
        Button(self,text='Compute BMI',command=self.compute).grid(row=2,column=0,columnspan=2)

    def compute(self):
        'the handler for button "Compute BMI"'
        try:
            hgt=eval(self.htEnt.get())
            wgt=eval(self.wtEnt.get())
            res=wgt*703/hgt**2
            showinfo(title='Result',message='Your BMI is {}'.format(res))
        except:
            showinfo(title='Ooops!',message='Invalid number!')
        self.wtEnt.delete(0,END)
        self.htEnt.delete(0,END)

        

# Question 3
class Ed(Frame):
    'Simple arithmetic education app'
    def __init__(self,parent=None):
        'constructor'
        Frame.__init__(self, parent)
        self.pack()
        Ed.make_widgets(self)
        Ed.new_problem(self)

    def make_widgets(self):
        'defines Ed widgets'
        self.exp=Entry(self)
        self.exp.grid(row=0,column=0)
        self.res=Entry(self)
        self.res.grid(row=0,column=1)
        Button(self,text='Enter',command=self.evaluate).grid(row=0,column=3)
        

    def new_problem(self):
        'creates new arithmetic problem'
        temp1=randrange(1,10)
        temp2=randrange(1,10)
        if temp1 > temp2:
            self.num1=temp1
            self.num2=temp2
        else:
            self.num1=temp2
            self.num2=temp1
        coinflip=randrange(1,3)
        if coinflip == 1:
            self.exp.insert(0,self.num1)
            self.exp.insert(END,' - ')
            self.exp.insert(END,self.num2)
            self.exp.insert(END,' =')
        else:
            self.exp.insert(0,self.num1)
            self.exp.insert(END,' + ')
            self.exp.insert(END,self.num2)
            self.exp.insert(END,' =')

    def evaluate(self):
        'handles button "Enter" clicks by comparing answer in entry to correct result'
        temp=self.exp.get()
        exprs=temp[0:5]
        try:
            reslt=self.res.get()
            if eval(exprs) == eval(reslt):
                showinfo(title='Way to go!',message='That is correct!')
                self.res.delete(0,END)
                self.exp.delete(0,END)
                Ed.new_problem(self)
            else:
                showinfo(title='Incorrect',message='Try again')
                self.res.delete(0,END)
        except:
            showinfo(title='I\'m sorry. I didn\'t get that.',message='Please enter your answer using digits (0 through 9).')
            self.res.delete(0,END)
                
            
