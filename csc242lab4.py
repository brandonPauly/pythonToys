# CSC 242, Spring 2013
# Lab 4 
# Brandon Pauly

# Question 1
def inValues():
    'input non-zero numbers from the user, computing the sum'
    num=1
    sumNum=0
    errCount=0
    while num !=0:
        try:
            num=float(input('Please enter a positive number (zero to quit): '))
            sumNum+=num
            errCount=0
        except:
            errCount+=1
            if errCount==2:
                print('There were two errors in a row. This program is quitting')
                break
            else:
                print('Invalid number format.  Please re-enter the value')
                continue
    if errCount != 2:
        print('The sum of the numbers is {:.1f} '.format(sumNum))
                

# Question 2
class Animal(object):
    'a class representing an abstraction of an animal'

    def __init__(self, s = 'default', l = 'default', w = 1):
        self.setSpecies(s)
        self.setLanguage(l)
        self.setWeight(w)

    def setSpecies(self, s):
        'set the species of the animal'
        self.species = s

    def setLanguage(self, l):
        'set the language of the animal'
        self.language = l

    def setWeight(self, w):
        '''set the weight of the animal in pounds, raising an exception
        for a non-positive weight'''
        if w<=0:
            raise(InvalidWeight('weight must be positive (>0)'))
        else:
            self.pounds=w

    def getKilos(self):
        'returns the weight of the animal in kilos'
        return self.pounds * 0.4535
        
    def speak(self):
        'return a string the animal would say'
        return "I am {} pound {} and I {}".format(self.pounds,\
                                                       self.species,\
                                                       self.language)

class InvalidWeight(Exception):
    'an exception class for the Animal class'

    def __init__(self, m):
        'constructor'
        self.error=m

    def __str__(self):
        'return a string showing the exception information'
        return(str(self.error))

