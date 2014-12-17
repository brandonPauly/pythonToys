# CSC 242
# Spring 2013
# Assignment 1
# Brandon Pauly

class BankAccount(object):
    'A user-defined Bank Account class'
    
    def setTo(self, value):
        'sets the Bank Account balance to value'
        self.amount=value
        

    def withdraw(self, value):
        'subtracts value from account balance'
        self.amount-=value
        

    def deposit(self, value):
        'adds value to account balance'
        self.amount+=value
        

    def balance(self):
        'returns balance of the account'
        return(self.amount)
    

    def __str__(self):
        'the method that returns a string representing the account'
        return str(self.amount)
    
    def __repr__(self):
        'the method that returns the canonical representation of the account'
        return repr(self.amount)

def processAccounts(fname):
    '''Supports bank account procedures listed within a text document assuming
that the first line is an appropriate number to set an initial balance.
Subsequent lines must begin with either the letter 'w' or the letter 'd' followed
by an appropriate number for a transaction.'''
    infile=open(fname)
    acct=BankAccount()
    procLines=[]
    for line in infile:
        line=line.replace('\n','')
        procLines.append(line)
    infile.close()
    acct.setTo(float(procLines[0]))
    procLines.remove(procLines[0])
    print('Initial Balance: $ {:0.2f}'.format(float(acct.__str__())))
    for inst in procLines:
        inst=inst.lower()
        if inst[0]=='w':
            inst=inst.replace('w','')
            inst=float(inst.strip())
            acct.withdraw(inst)
            print('Withdrawl: $ {:0.2f}'.format(inst))
        elif inst[0]=='d':
            inst=inst.replace('d','')
            inst=float(inst.strip())
            acct.deposit(inst)
            print('Deposit: $ {:0.2f}'.format(inst))
    print('Final Balance: $ {:0.2f}'.format(float(acct.__str__())))
    return acct
