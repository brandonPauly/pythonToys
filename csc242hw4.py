# CSC 242, Spring 2013
# Assignment 4 
# Brandon Pauly

from tkinter import Frame, Tk
from tkinter.messagebox import showinfo
from math import sqrt

# Question 1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class BankAccount(object):
    '''A sub-class of the object class that represents simple bank accounts
    and supports withrawls, deposits, and balance inquiries.'''
    
    def __init__(self, value = None):
        '''Constructor that takes one parameter, and sets the balance of
        the bank account to value. If no parameter is entered it sets the value
        to zero. Should a negative value be given, no bank account is created.'''
        if value == None:
            self.amount = 0
        elif value < 0:
            raise(NegativeBalanceError('Account created with a negative balance of ${}.'.format(value)))
        else:
            self.amount = value

            
    def withdraw(self, value):
        '''Withdraws the specified amount from the account. Should the value
        be greater than the balance in the account, the user is notified
        and no transaction occurs.'''
        if value > self.amount:
            raise(OverdraftError('Withdrawl would result in a negative balance of ${}'.format(self.amount-value)))
        else:
            self.amount -= value

        
    def deposit(self, value):
        '''Deposits the specified amount from the account. Should the value
        be less than zero, the user is notified and no transaction occurs'''
        if value < 0:
            raise(DepositError('Negative deposit of ${} attempted'.format(value)))
        self.amount += value

        
    def balance(self):
        'Returns the current balance on the account.'
        return self.amount
    
    def __repr__(self):
        'Returns a representation of the BankAccount item.'
        return "BankAccount({})".format(self.amount)


class NegativeBalanceError(Exception):
    '''Sub-class of the exception class, which is raised if the constructor
    in the BankAccount class is given a negative value as a parameter'''
    
    def __init__(self,a):
        '''Constructor that takes a string as a parameter to describe the error
        in account creation with a negative value.'''
        self.nBErr=a

    def __str__(self):
        '''Returns the string describing the error in account creation with a
        negative value.'''
        return(str(self.nBErr))


class OverdraftError(Exception):
    '''Sub-class of the exception class, which is raised if the value given
    to the withdrawl function in the BankAccount class is greater than the
    balance of the account.'''

    def __init__(self,a):
        '''Constructor that takes a string as a parameter to describe the error
        in a withdrawl procedure, should the withdrawl amount be greater than
        the balance of the account.'''
        self.oErr=a

    def __str__(self):
        '''Returns the string describing the error in a withdrawl procedure if
        the withdrawl request is greater than the balance of the account.'''
        return(str(self.oErr))


class DepositError(Exception):
    '''Sub-class of the exception class, which is raised if the value given to
    the deposit function in the BankAccount class is a negative value.'''

    def __init__(self,a):
        '''Constructor that takes a string as a parameter to describe the error
        in a deposit procedure, should the deposit amount be a negative value'''
        self.dErr=a
    
    def __str__(self):
        '''Returns the string describing the error in a deposit procedure if
        the deposit amount is of a negative value'''
        return(str(self.dErr))
    
# Question 2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def processTrans(fname):
    '''Function that takes a file name as a parameter. If the file is available,
    the program opens and reads the file, then stores each line in a list.
    Each line is then attempted as a transaction and the outcome of the
    transaction is prited.  After all functional transactions are made, the
    balance is given and the account is returned.'''
    
    acct=BankAccount()
    trans=[]
    try:
        infile=open(fname,'r')
        for line in infile:
            line=line.replace('\t','')
            line=line.replace('\n','')
            trans.append(line.lower())
        infile.close()
    except FileNotFoundError:
        print('File {} could not be opened. Exiting program.'.format(fname))
        quit()
    for op in trans:
        if op[0]=='w':
            try:
                op=op.replace('w','')
                op=op.strip()
                acct.withdraw(eval(op))
                print('Withdrawl: $ {}'.format(op))
            except OverdraftError as b:
                print('Withdrawl skipped in file {}: {}'.format(fname,b))
        elif op[0]=='d':
            try:
                op=op.replace('d','')
                op=op.strip()
                acct.deposit(eval(op))
                print('Deposit: $ {}'.format(op))
            except DepositError as c:
                print('Deposit skipped in file {}: {}'.format(fname,c))
    print('Final balance: $ {}'.format(acct.balance()))        
    return(acct)

# Question 3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def check(Event):
    '''An event driven function that responds to left mouse clicks. If the
    click is within an invisible circle with a radius of ten surrounding point
    (50,50), then the user has won and is notified.  Should the click reside
    outside of the invisible circle, the user is notified of the location of
    their click and urged to try again.'''
    dist=sqrt(((50-Event.x)**2)+((50-Event.y)**2))
    if dist < 10:
        showinfo(title='Notification',message='You got it!')
    else:
        showinfo(title='Notification',message='Try again! You left-clicked at ({}, {}). The goal is to within a circle of radius 10 centered around (50,50)'.format(Event.x,Event.y))

def create_window():
    '''Function to create a GUI window of 100x100 that checks the event of a
    left mouse click that occurs within the window.'''
    root = Tk()

    widget = Frame(root, width=100, height=100)
    widget.bind("<Button-1>", check)
    widget.pack()

    root.mainloop()
