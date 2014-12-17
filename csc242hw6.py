# CSC 242, Spring 2013
# Assignment 6
# Brandon Pauly

# Question 1
def recVowelCount(s):
    '''function that takes string 's' as input and returns
    the number of vowels (excluding y) in 's' '''
    
    vwls='aeiouAEIOU'
    n=len(s)
    count=0
    if n == 0:
        return count
    else:
        if s[0] in vwls:
            count += 1
        x = recVowelCount(s[1:n+1])
        return x + count
        

# Question 2
def printPattern(n):
    '''function that prints a pattern of 'n' *'s, then 'n' !'s'''
    
    a='*!'
    if n <= 0:
        return
    else:
        print('*',end='')
        printPattern(n-1)
        print('!',end='')


# Question 3
def sumSquares(n):
    '''function that returns the sum of all squares from zero
    up to and including 'n'''
    
    if n <= 0:
        return 0
    else:
        return sumSquares(n-1) + n**2
    

# Question 4
def crawl(fname): 
    '''function that crawls through links within files to other files and prints
    a message pertaining to which file it is currently visiting'''
    
    infile=open(fname)
    print('Visiting {}'.format(fname))
    s=infile.readlines()
    infile.close()
    if len(s)== 0:
        return
    else:
        for f in s:
            f=f.replace('\n','')
            crawl(f)
    

# Question 5
def pascalLine(n):
    '''function that returns the nth line of pascals triangle'''
    
    pLine=[1]
    if n <= 0:
        return [1]
    else:
        prevLine = pascalLine(n-1)
        for i in range(n-1):
            pLine.append(prevLine[i]+prevLine[i+1])
        pLine.append(1)
        return pLine
