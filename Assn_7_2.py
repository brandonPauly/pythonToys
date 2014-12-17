def randomizer(x,y):#Random Number Generator
    
    import random
    outcome=random.randrange(x,y)
    return(outcome)


def coinFlip():#coin flip function, also allows the winner of the coin flip to choose first or second

    flipChoice=input('Choose heads or tales for the coin toss.\nInput \'h\' for heads, \'t\' for tails.\n')
    flipChoice=flipChoice.lower()

    while flipChoice!='h' and flipChoice!='t':
        flipChoice=input('Invalid entry! Please input \'h\' for heads, \'t\' for tails.\n')

    if flipChoice=='h':
        flipChoice=1

    else:
        flipChoice=2

    num1=randomizer(1,3)
    
    if num1==1:
        print('And the flip is heads!')
        
    else:
        print('And the flip is tails!')

    if num1==flipChoice:
        winChoice=eval(input('You won the flip!\nWould you like to go first, or would you prefer to go second?\nInput \'1\' to go first, \'2\' to pass the turn.\n'))
        
        while winChoice!=1 and winChoice!=2:
            winChoice=eval(input('Invalid entry!\nPlease input \'1\' to go first, \'2\' to go second.\n'))
            
        if winChoice==1:
            return(1)
        
        else:
            return(2)

    else:
        lossChoice=randomizer(1,3)
        
        if lossChoice==1:
            print('CPU won the flip and chose to go 1st.\n')
            return(2)
        
        else:
            print('CPU won the flip and chose to go 2nd.\n')
            return(1)

            
def gameOn():#Function to run game, filters game if player goes first or if CPU goes first, returns outcome to main code

    global marbles
    
    if coinToss==1:
        print('There are '+str(marbles)+' marbles in the pile.\n')
        outcome=turns()
        return(outcome)
            
    else:
        print('There are '+str(marbles)+' marbles in the pile.\n')
        tempMarbles=randomizer(1,marbles//2)
        marbles-=tempMarbles
        print('The CPU took '+str(tempMarbles)+' marbles from the pile.\n')
        print('There are '+str(marbles)+' marbles in the pile.\n')
        outcome=turns()
        return(outcome)


def turns():#Function to run turn sequence and return outcome to gameOn function
    
    global marbles
    
    while marbles>2:
        if marbles//2==1:
            removal=eval(input('Input \'1\' to take your marble.\n'))
            while removal!=1:
                removal=eval(input('Invalid input!\nType 1 and press enter to continue.\n'))
        else:
            removal=eval(input('How many marbles would you like to take?\nEnter a number from 1 to '+str(marbles//2)+'.\n'))
        
        while not(1<=removal<=(marbles//2)) and removal!=int:
            removal=eval(input('Invalid input! Please enter a whole number from 1 to '+str(marbles//2)+'.\n'))
            
        marbles-=removal
        print('\n'+str(marbles)+' marbles remain in the pile.\n')
        tempMarbles=randomizer(1,(marbles//2)+1)
        marbles-=tempMarbles
        print('The CPU removed '+str(tempMarbles)+' marbles from the pile.\n')
        
        if marbles>2:
            print(str(marbles)+' marbles remain in the pile.\n')
            
        if marbles==1:
            print('1 marble remains in the pile.')

    if marbles==2:
        print('You take your 1 marble, and the CPU takes the last one.\nYou\'ve won this round!\n')
        return(1)

    else:
        print('Sorry.\nYou lost this round.\n')
        return(0)


def endGame():#Function to end the game and display rounds and wins

    if gameCount>1:
        print('You played a total of '+str(gameCount)+' rounds.')

    elif gameCount==1:
        print('You played one round.')

    else:
        quit

    if wins>1:
        print('You won '+str(wins)+' rounds!')

    elif wins==1:
        print('You won one round!')

    else:
        print('No winning rounds!')





welcome='Hello! Welcome to the game of NIM! You will be playing against the computer in this game.\nBetween you and your opponent there will be a random number of marbles between 10 and 100.\nThe first player takes a number of marbles from 1 to no more than half the marbles in the pile.\nPlayers alternate turns, taking from 1 to no more than half the number of marbles from the pile.\nThe player that takes the last marble from the pile loses the round.\nA coin flip will determine which player goes first.'

for l in welcome:
    print(l, end='')

play=input('\n\nWould you like to play a game?\nInput \'y\' yes, \'n\' for no.\n')
play=play.lower()
gameCount=0
wins=0

while play!='y' and play!='n':
    play=input('Invalid entry! Please input \'y\' for yes, \'n\' for no.\n')

while play=='y':
    print('Game on!')
    coinToss=coinFlip()
    marbles=randomizer(10,101)
    wins+=gameOn()
    gameCount+=1
    play=input('Would you like to play another round?\nInput \'y\' for yes, \'n\' for no.\n')
    play=play.lower()
    
    while play!='y' and play!='n':
        play=input('Invalid entry! Please input \'y\' for another round, \'n\' to quit.\n')

if play=='n':

    endGame()
