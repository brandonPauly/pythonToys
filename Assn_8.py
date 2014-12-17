def print1(s):#Print function for "cute" printing method
    for l in s:
       print(l,end='')

def menu():#Function that runs the menu
    print1('\nMain Menu:\nPlease input the corresponding number and press enter\n\n')
    print1('1) Deposit\n2) Withdrawl\n3) Balance Inquiry\n4) Quit\n\n\n')
    menuChoice=input()
    if len(menuChoice)==1 and menuChoice in '1234':
        return menuChoice            
    else:
        while len(menuChoice)!=1 or menuChoice not in '1234':
            print1('\n\nInvalid entry!\nPlease enter a corresponding value to a menu option\n\n\n1) Deposit\n2) Withdrawl\n3) Balance Inquiry\n4) Quit\n\n\n')
            menuChoice=input()
        return menuChoice

def balanceMod():#Updates account file if changes are made

    outfile=open('accounts.txt','w')
    for k in actDict.keys():
        outfile.write(k+' '+actDict.get(k)[0][0]+' '+actDict.get(k)[0][1]+' '+str(actDict.get(k)[1])+'\n')
    outfile.close()    
    
                    
def deposit(actNum):#Function to run deposit procedures
    while True:    
        while True:
            try:
                print1('\n\nWould you like to make a deposit?\nInput \'y\' for yes, \'n\' for no and press enter\n\n\n')
                depositVer=input()
                depositVer=depositVer.lower()
                if depositVer=='n':
                    return
                elif depositVer!='y':
                    print1('\n\nInvalid entry!\nPlease re-enter either \'y\' to enter a deposit, or \'n\' to go back to the main menu\n\n\n')
                    continue
                break
            except:
                print1('\n\nInvalid entry!\nPlease re-enter either \'y\' to enter a deposit, or \'n\' to go back to the main menu\n\n\n')
                continue
        while True:
        
            try:
                print1('\n\nHow much would you like to deposit today?\nPlease input a number and press enter\n\n\n')
                depositAmt=eval(input())
                if depositAmt<=0:
                    print1('\n\nInvalid entry!\nPlease re-enter a number greater than 0\n\n')
                    continue
                break
            except:
                print1('\n\nInvalid entry!...\n\n')
                continue

        while True:
            try:
                print1('\n\nIs '+'${:0.2f}'.format(depositAmt)+' the correct amount you would like to deposit today?\nInput \'y\' for yes, \'n\' for no, then press enter\n\n\n')
                correctAmt=input()
                correctAmt=correctAmt.lower()
                if correctAmt=='y':
                    actDict[actNum][1]+=depositAmt
                    balanceMod()
                    print1('\n\n'+'${:0.2f}'.format(depositAmt)+' have been deposited to your account\n\n\n')
                    return
                elif correctAmt!='n':
                    print1('\n\nInvalid entry!...\n\n')
                    continue
                else:
                    print1('\n\nDeposit cancelled\n\n')
                    break
                    continue
            except:
                print1('\n\nInvalid entry!...\n\n')
                continue
            
    
    


def withdrawl(actNum):#Function to run withdrawl procedures
    while True:    
        while True:
            try:
                print1('\n\nWould you like to make a withdrawl?\nInput \'y\' for yes, \'n\' for no and press enter\n\n\n')
                withdrawlVer=input()
                withdrawlVer=withdrawlVer.lower()
                if withdrawlVer=='n':
                    return
                elif withdrawlVer!='y':
                    print1('\n\nInvalid entry!\nPlease re-enter either \'y\' to make a withdrawl, or \'n\' to go back to the main menu\n')
                    continue
                break
            except:
                print1('\n\nInvalid entry!\nPlease re-enter either \'y\' to make a withdrawl, or \'n\' to go back to the main menu\n')
                continue
        while True:
        
            try:
                print1('\n\nHow much would you like to withdraw today?\nPlease input a number and press enter\n\n\n')
                withdrawlAmt=eval(input())
                if withdrawlAmt<=0:
                    print1('\n\nInvalid entry!\nValue must be greater than 0\n')
                    continue
                if withdrawlAmt>actDict[actNum][1]:
                    print1('\n\nInsufficient funds!\nPlease input a value up to '+'${:0.2f}'.format(actDict[actNum][1])+'\n')
                    continue
                break
            except:
                print1('\n\nInvalid entry!...\n')
                continue

        while True:
            try:
                print1('\n\nIs '+'${:0.2f}'.format(withdrawlAmt)+' the correct amount you would like to withdraw today?\nInput \'y\' for yes, \'n\' for no, then press enter\n\n\n')
                correctAmt=input()
                correctAmt=correctAmt.lower()
                if correctAmt=='y':
                    actDict[actNum][1]-=withdrawlAmt
                    balanceMod()
                    print1('\n\n'+'${:0.2f}'.format(withdrawlAmt)+' have been withdrawn from your account\n\n\n')
                    return
                elif correctAmt!='n':
                    print1('\n\nInvalid entry!...\n\n')
                    continue
                else:
                    print1('\n\nWithdrawl cancelled\n\n')
                    break
                    continue
        
            except:
                print1('\n\nInvalid entry!...\n\n')
                continue

            


def balance(actNum):#Function to grab balance
    amount=actDict[actNum][1]
    return amount

while True:
    
    actDict={}
    try:
        infile=open('accounts.txt')
        actHolders=infile.readlines()
    
        for aH in actHolders:
            aHMash=aH.split()
            if len(aHMash)>0:
                actDict[aHMash[0]]=[[aHMash[1],aHMash[2]],float(aHMash[3])]
        infile.close()

    except:
        print1('We seem to be experiencing technical difficulties\nWe apologize for the inconvenience\nPlease visit any of our branch locations or another ATM\nThank You\n\n\n\n')
        quit
    

    print1('Welcome to Bank of Pauly \nPlease input your account number and press enter to begin\n\n\n')
    actNum=input()


    if actNum not in actDict.keys():
        print1('\n\n\nError!\nAccount not found\n\n\n\n')
        continue
    else:
        print1('\n\nHello '+str(actDict.get(actNum)[0][0])+' '+str(actDict.get(actNum)[0][1])+'\n')
        while True:
            menuChoice=menu()
            if menuChoice=='1':
                deposit(actNum)
            elif menuChoice=='2':
                withdrawl(actNum)
            elif menuChoice=='3':
                print1('\n\nYour account balance is '+'${:0.2f}'.format(actDict[actNum][1])+'\n\n')
                continue
            else:
                print1('\n\nThank you choosing Bank of Pauly\nHave a wonderful day!\n\n\n')
                break
                continue
                
