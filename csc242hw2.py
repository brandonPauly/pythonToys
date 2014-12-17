#Brandon Pauly
#CSC 242-603
#Assignment 2

class Polygon(object):
    '''superclass that represents a polygon by setting the selected number of
    sides and chosen length of those sides, all being equal'''
    
    def __init__(self,sides=0,length=0):
        'constructor to set the number of sides and length of sides'
        self.nSides=sides
        self.sideLen=length

    def setLength(self,length):
        'sets the length of the polygons sides'
        self.sideLen=length

    def perimeter(self):
        'returns the perimeter of the polygon'
        return(self.sideLen*self.nSides)

    def area(self):
        'returns the area of the polygon'
        import math
        return(((self.sideLen**2)*self.nSides)/(4*math.tan((math.pi/self.nSides))))

    def __str__(self):
        'returns a string representing the polygon'
        return('A polygon with {} sides, each of length {}.'.format(self.nSides,self.sideLen))

    def __repr__(self):
        'returns a canonical representation of the polygon'
        return('Polygon({},{})'.format(self.nSides,self.sideLen))


class Square(Polygon):
    '''Polygon subclass that represents a square by setting sides to four
    and the selected length of the sides'''

    def __init__(self,length):
        '''overloaded constructor that pulls from the Polygon constructor, but eliminates the
        need for a parameter representing the number of sides'''
        Polygon.__init__(self,4,length)

    def area(self):
        'returns the area of the square'
        return(self.sideLen**2)


class Triangle(Polygon):
    '''Polygon subclass that represents a triangle by setting sides to three and
    the selected length of the sides.'''

    def __init__(self,length):
        '''overloaded constructor that pulls from the Polygon constructor, but eliminates the
        need for a parameter representing the number of sides.'''
        Polygon.__init__(self,3,length)

    def area(self):
        'returns the area of the triangle'
        import math
        return((self.sideLen**2)*(math.sqrt(3))/4)


class Person(object):
    '''superclass that represents a person and sets that persons birth year'''

    def __init__(self,name='Jane Doe',birDate=2013):
        'constructor that sets the string of the person\'s name and their birthyear'
        self.fullName=name
        self.dOB=birDate

    def age(self):
        'uses current time to calculate the person\'s age in years'
        import time
        return((int(time.strftime('%Y',time.localtime()))-int(self.dOB)))

    def name(self):
        'returns the name of the person'
        return(self.fullName)

    def __repr__(self):
        'returns the canonical representation of the person'
        return('Person({}, {})'.format(self.fullName,self.dOB))

    def __str__(self):
        'returns the string representation of the person'
        return('{} is {} years old.'.format(self.fullName,self.age()))


class Student(Person):
    '''Person subclass that represents a student by including the person\'s
    major as an attribute'''
    
    def __init__(self,name,birDate,arStudy):
        'overloaded constructor that adds major as a parameter'
        self.maj=arStudy
        Person.__init__(self,name,birDate)

    def major(self):
        'returns the major of the person'
        return(self.maj)


class Instructor(Person): 
    '''Person subclass that represents an instructor by including the person\'s
    degree as an attribute'''

    def __init__(self,name,birDate,edLvl):
        'overloaded constructor that adds degree as a parameter'
        self.deg=edLvl
        Person.__init__(self,name,birDate)

    def degree(self):
        'returns the degree of the person'
        return(self.deg)
