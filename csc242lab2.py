# CSC 242
# Lab 2 template
# Brandon Pauly
# 

# Make the modifications described in the lab
class Animal(object):
    'a class representing an abstraction of an animal'

    def __init__(self, s = 'default', l = 'default', years=0):
        'the default constructor for the Animal class'
        self.species = s
        self.language = l
        self.age=years

    def setSpecies(self, s):
        'set the species of the animal'
        self.species = s

    def setLanguage(self, l):
        'set the language of the animal'
        self.language = l

    def setAge(self,years):
        'set the age of the animal in years'
        self.age=years

    def getAge(self):
        'returns the age of the animal'
        return self.age
    
    def speak(self):
        'return a string the animal would say'
        return "I am a {} year-old {} and I {}".format(self.age,self.species, self.language)
    
    def __str__(self):
        'the pretty representation of an animal'
        return 'The animal is a {}-year-old {}, which {}s.'.format(self.age,self.species, self.language)

    def __repr__(self):
        'the canonical representation of an animal'
        return 'Animal({}, {}, {})'.format(self.species, self.language,self.age)



def processAnimals(fname):
    '''The function takes a file that has lines of text consisting of an animal species,
the language of the animal, and the age in years of the animal. Assuming that each instance is
seperated by a comma, the function seperates the pieces of information to place into an item of the
Animal class.  Then calls the speak function for each animal in the list'''
    Animals=[]
    infile=open(fname)
    for line in infile:
        if '\n' in line:
            line=line.replace('\n','')
        anList=line.split(',')
        Animals.append(anList)
    infile.close()
    clAnim=[]
    for b in Animals:
        a=Animal()
        a.setSpecies(b[0])
        a.setLanguage(b[1])
        a.setAge(int(b[2]))
        clAnim.append(a)
    for animal in clAnim:
        print(animal.speak())
    return(clAnim)
        
        
