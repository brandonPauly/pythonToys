def startUp():
    """Read accounts from file and create dictionary with secret code as key.
       Returns True if successful, False otherwise"""
    global accts
    try:
        infile = open('accounts.txt')
    except:
        print('We are very sorry. This ATM is current uder maintainance.\nPlease try later.')
        return False
    for line in infile:
        if len(line) > 1:
            lineList = line.split()
            accts[lineList[0]] = lineList[1:3]+[ float(lineList[3])]#need to make sure the balance is a float
    infile.close()
    return True
    
 
def getUser():
    """obtain secret code and validate account"""
    global accts
    global userIntent
    try:
        user = input('Welcome to the CSC241 Bank ATM\nPlease enter your secret code:\n')
        if len(user) == 4 and user in accts:
            return user
        else:
            print('Secret code incorrect. Goodbye.')
            userIntent = False
            return None
    except:
        print('Secret code incorrect. Goodbye.')
        userIntent = False
        return None

def menu():
    global user
    global accts
    return( eval(input(80*'_' +'\n' + 80*'_' +'\n'+
                       'Welcome '+ accts[user][0] + '.\nPlease select your transaction:\n\t'+
                        '1: DEPOSIT\n\t'+
                        '2: WITHDRAW\n\t'+
                        '3: GET BALANCE\n\t'+
                        '4: QUIT\n')))

def deposit():
    global accts
    global user
    accts[user][2]+= getAmount('deposit')
    print('Your transaction was successful')

def withdraw():
    global accts
    global user
    amount = getAmount('withdraw')
    while  amount > accts[user][2]:
        print('You do not have sufficient funds to complete this transaction.')
        amount = getAmount('withdraw')
    else:
        accts[user][2]-=amount
    print('Your transaction was successful')
        
    
def getAmount(mode):
    amountBad = True
    while amountBad:
        try:
            amount = float(input('\nPlease enter the amount you wish to '+ mode+ ' :\n'))
            amountBad = False
        except:
            print('You entered an incorrect amount.\nPlease try again')
    return amount


def balance():
    global accts
    global user
    print(accts[user][0] +', your current balance is ${}'.format(accts[user][2]))

def wrapUp():
    outfile = open('accounts.txt', 'w')
    for user in accts:
        outfile.write(user + ' ')
        for i in range (3):
            outfile.write(str(accts[user][i] )+ ' ')
        outfile.write('\n')
    outfile.close()
    print(80*'_'+'\n'+
          80*'_' + '\n'+
          'Thank you for using the CSC241 Bank ATM.\nGoodbye')

accts = {}#dictionary that stores accounts info as code:[fname lastname balance]
userIntent = True
if startUp():
    user = getUser()
    while userIntent:
        choice = menu()
        if choice == 1:
            deposit()
        elif choice == 2:
            withdraw()
        elif choice == 3:
            balance()
        else:
            wrapUp()
            userIntent = False
