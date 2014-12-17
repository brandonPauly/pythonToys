# CSC 242, Spring 2013
# Lab 7 
# Brandon Pauly

# Question 1
class OddList(list):
    'a class representing an odd-behaving list'

    def __iter__(self):
        'returns an iterator for the class'
        return OddListIterator(self)

class OddListIterator:
    'a odd-behaving iterator for a list class'

    def __init__(self, l):
        'constructor'
        self.lst=l
        self.index = 1

    def __next__(self):
        'returns the next OddList item'
        if self.index > len(self.lst)-1:
            raise StopIteration()
        ans = self.lst[self.index]
        self.index += 2
        return ans

# Question 2
def printPattern(indent, n):
    'print a fancy, indented pattern'
    if n == 0:
        return
    elif n == 1:
        print(indent*' '+'*')
    else:
        printPattern(indent,n//2)
        print(indent*' '+'*'*n)
        printPattern(indent+n//2,n//2)


