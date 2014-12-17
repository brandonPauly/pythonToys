# CSC 242
# Lab 3 
# Brandon Pauly

# Question 1
class Student(object):
    'a class representing a student'

    roster = {'undergrad': 0, 'grad': 0, 'other':0}

    def __init__(self, st = 'other', name = 'default'):
        'the default constructor for the Student class'
        self.sType = st
        self.lName = name
        Student.addStudent(st)

    def getName(self):
        'get the (last) name of the student'
        return self.lName

    def getType(self):
        'get the type of the student'
        return self.sType 

    def addStudent(t):
        'add a student to the roster'
        t=t.lower()
        if t in Student.roster:
            Student.roster[t]+=1
        else:
            Student.roster['other']+=1

    def displayRoster():
        'display the roster'
        print('The students registered so far:')
        for categ in Student.roster:
            print('{:9} : {}'.format(categ,Student.roster[categ]))

    def __repr__(self):
        'return the canonical representation of a Student'
        return('Student({}, {})'.format(self.sType,self.lName))

    def __str__(self):
        'return the pretty representation of a Student'
        return('{} is a Student, at the {} level.'.format(self.lName,self.sType))

# Question 2
def processClass(fname):
    inFile=open(fname)
    stuList=[]
    for line in inFile:
        line=line.replace('\n','')
        line=line.split()
        if len(line)==2:
            s=Student(line[0],line[1])
        elif len(line)==1:
            s=Student(line[0])
        print(s)
        stuList.append(s)       
    inFile.close()
    if len(stuList)>0:
        print('\n')
        Student.displayRoster()
        print('\n')
    print(stuList)
    
    
        
            

