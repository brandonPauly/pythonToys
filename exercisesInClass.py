def pattern(n):
    'print a recursive pattern'
    if n == 1:
        print(1, end = ' ')
    else:
        pattern(n-1)
        print(n, end=' ')
        pattern(n-1)
    
def cheer(n):
    'recursively print a cheer'
    if n <= 1:
        print('Hurrah!')
    else:
        print("Hip")
        cheer(n-1)
    
def printLst(lst):
    '''recursively prints the items in lst, one per line,
starting with the item in index 0, without modifying lst'''
    if len(lst) == 0:
        return
    elif len(lst) == 1:
        print(lst[0])
    else: # lst has at least two items
        print(lst[0])
        printLst(lst[1:])
    
def recFact(n):
    'return the product of the numbers between 1 and n'
    if n == 1:
        return 1
    else:
        return n * recFact(n-1)

def iterFact(n):
    'return the product of the numbers between 1 and n'
    prod = 1
    for i in range(1, n+1):
        #print(i)
        prod = prod * i
    return prod

def revVertical(n):           
    '''recursively print the digits of n, least significant to
most significant, one per line'''
    if n < 10:             
        print(n)           
    else:
        print(n % 10) 
        revVertical (n // 10)      
