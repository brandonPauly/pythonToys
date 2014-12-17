def startUp(myDictionary, file):
    """Read accounts from file and create dictionary with secret code as key.
       Returns True if successful, False otherwise"""
    try:
        infile = open(file)
    except:
        print('We are very sorry. This ATM is current uder maintainance.\nPlease try later.')
        return False
    for line in infile:
        if len(line) > 1:
            lineList = line.split()
            myDictionary[lineList[0]] = lineList[1:3]+[ float(lineList[3])]#need to make sure the balance is a float
    infile.close()
    return (True, myDictionary)
    
 
def getUser(wish, myDictionary):
    """obtain secret code and validate account"""
    try:
        user = input('Welcome to the CSC241 Bank ATM\nPlease enter your secret code:\n')
        if len(user) == 4 and user in myDictionary:
            return (user, wish)
        else:
            print('Secret code incorrect. Goodbye.')
            return (None, False)
    except:
        print('Secret code incorrect. Goodbye.')
        return (None, False)

def menu(name):
    return( eval(input(80*'_' +'\n' + 80*'_' +'\n'+
                       'Welcome '+ name + '.\nPlease select your transaction:\n\t'+
                        '1: DEPOSIT\n\t'+
                        '2: WITHDRAW\n\t'+
                        '3: GET BALANCE\n\t'+
                        '4: QUIT\n')))

def deposit(balance):
    balance+= getAmount('deposit')
    print('Your transaction was successful')
    return balance

def withdraw(balance):
    amount = getAmount('withdraw')
    while  amount > balance:
        print('You do not have sufficient funds to complete this transaction.')
        amount = getAmount('withdraw')
    else:
        balance-=amount
    print('Your transaction was successful')
    return(balance)
        
    
def getAmount(mode):
    amountBad = True
    while amountBad:
        try:
            amount = float(input('\nPlease enter the amount you wish to '+ mode+ ' :\n'))
            amountBad = False
        except:
            print('You entered an incorrect amount.\nPlease try again')
    return amount


def balance(name, balance):
    print(name +', your current balance is ${}'.format(balance))

def wrapUp(myDictionary, file):
    outfile = open(file, 'w')
    for key in myDictionary:
        outfile.write(key + ' ')
        for i in range (3):
            outfile.write(str(myDictionary[key][i] )+ ' ')
        outfile.write('\n')
    outfile.close()
    print(80*'_'+'\n'+
          80*'_' + '\n'+
          'Thank you for using the CSC241 Bank ATM.\nGoodbye')


userIntent = True
success, accts = startUp({}, 'accounts.txt')
if success:
    user, userIntent = getUser(userIntent, accts)
    while userIntent:
        choice = menu(accts[user][0])
        if choice == 1:
            accts[user][2] = deposit(accts[user][2])
        elif choice == 2:
            accts[user][2] = withdraw(accts[user][2])
        elif choice == 3:
            balance(accts[user][0],accts[user][2])
        else:
            wrapUp(accts, 'accounts.txt')
            userIntent = False
