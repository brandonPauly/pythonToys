def pattern(n):
    if n==1:
        print(1, end=' ')
    else:
        pattern(n-1)
        print(n, end=' ')
        pattern(n-1)
def cheer(n):
    if n<=1:
        print('Hurrah')
    else:
        print('Hip')
        cheer(n-1)
    
def printLst(lst):
    if len(lst)==0:
        return
    elif len(lst)==1:
        print(lst[0])
    else:
        print(lst[0])
        printLst(lst[1:])
        
def recFact(n):
    if n==1:
        return 1
    else:
        return n*recFact(n-1)
    
def iterFact(n):
    prod=1
    for i in range(1,n+1):
        prod=prod*i
    return prod

def vertical(n):           #1
    print("Entering vertical({})".format(n)) #2
    if n < 10:             #3
        print(n)           #4
        print("Leaving vertical({})".format(n)) #5
    else:                  #6
        print(n%10)
        vertical (n // 10) #7     #8
        print("Leaving vertical({})".format(n)) #9
