def iterBinSearch(item,lst):
    '''return the index of the first occurrence of item in list
using binary search'''
    low = 0
    high = len(lst) - 1
    while low <= high:
        #still searching
        mid = (high + low) // 2
        if lst[mid] == item:
            return mid
        elif lst[mid] < item:
            #search right
            low = mid + 1
        else:
            #search left
            high = mid - 1
    return -1
    
def linearSearch(item,lst):
    '''returns the index of the first occurrence of item in list or -1
if item is not found in lst'''
    for i in range(len(lst)):
        if item == lst[i]:
            return i
        elif lst[i] > item:
            return-1
    return -1

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

def betterExp(a,n):
    if n == 0:
        return 1
    else:
        res = betterExp(a,n//2)
        if n%2==0:
            return res*res
        else:
            return res*res*a

def recExp(a,n):
    if n == 0:
        return 1
    else:
        return a * recExp(a,n-1)
        
    
def iterExp(a,n):
    'returns a to the power n'
    res = 1
    for i in range(n):
        res=res*a
    return res
