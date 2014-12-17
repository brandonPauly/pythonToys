# CSC 242, Spring 2013
# Assignment 3
# Brandon Pauly

#*1*1*1*1*1*1*1*1*1*1*1*1*1*1*1*1*1*1*1*1*1*1*1*1*1*1*1*1*1*1*1*1*1*1*1*1*1*1*1*1*1*1


class Stat(object):
    '''a user-defined class to store a sequence of numbers and provide
    statistical information about the sequence'''
    

    def __init__(self,seq=[]):
        '''constructor to take either a list of numbers as the parameter, or
        instantiates an empty list'''
        self.numbers=list(seq)

    def __len__(self):
        'attribute to return the length of the number list'
        return(len(self.numbers))

    def __iter__(self):
        'attribute to support iteration over number list'
        return(iter(self.numbers))
        
    def min(self):
        'method to return the smallest number in the list'
        try:
            return(min(self.numbers))
        except:
            return(0.0)
        
    def max(self):
        'method to return the largest number in the list'
        try:
            return(max(self.numbers))
        except:
            return(0.0)

    def sum(self):
        'method to return the sum of all numbers in the list'
        try:
            return(sum(self.numbers))
        except:
            return(0)

    def mean(self):
        'method to return the average of all numbers in the list'
        try:
            return(self.sum()/len(self.numbers))
        except:
            return(0.0)

    def add(self,num):
        'method to add a number to the list of numbers'
        self.numbers.append(num)


    def clear(self):
        'method to remove all numbers in the list'
        self.numbers=[]


#*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2
    
class PriorityQueue(object):
    '''sub-class of the object class which creates a queue of numbers in
    ascending order'''

    def __init__(self):
        'constructor that instatiates an empty queue'
        self.queue=[]
        
    def insert(self,num):
        '''method to add a number to the queue and sort, to ensure numbers are
        in ascending order'''
        self.queue.append(num)
        self.queue.sort()

    def minimum(self):
        'method to return the minimum number in the queue'
        return(self.queue[0])

    def removeMin(self):
        'method to remove the minimum number and return its value'
        return(self.queue.pop(0))

    def __len__(self):
        'attribute to return the number of numbers in the queue'
        return(len(self.queue))

    def __str__(self):
        'attribute to run the queue through the print function'
        return(str(self.queue))

    def __repr__(self):
        'attribute to return the canonical representation of the queue'
        return(repr(self.queue))

    def __getitem__(self,index):
        'attribute to support indexing within the queue'
        return(self.queue[index])

##    def __iter__(self):
##        'attribute to support iteration over the queue'
##        return(list.__iter__(self.queue))
##
    
#*3*3*3*3*3*3*3*3*3*3*3*3*3*3*3*3*3*3*3*3*3*3*3*3*3*3*3*3*3*3*3*3*3*3*3*3*3*3*3*3
    
def testQueue(file):
    '''function that takes a text file as the parameter. given that the text
    file is in correct format, will code a sequence from the lines of the text
    file and perform the appropriate operations to a priority queue'''
    infile=open(file,'r')
    opList=[]
    for line in infile:
        line=line.replace('\n','')
        line=line.lower()
        opList.append(line)
    infile.close()
    queue=PriorityQueue()
    for op in opList:
        if op[0]=='i':
            op=op.replace('i','')
            op=op.strip()
            queue.insert(op)
        elif op[0]=='m':
            print(queue.minimum())
        elif op[0]=='r':
            print(queue.removeMin())
        elif op[0]=='l':
            print(queue.__len__())
        elif op[0]=='g':
            op=op.replace('g','')
            op=op.strip()
            print(queue.__getitem__(int(op)))
        elif op[0]=='s':
            print(queue)
        elif op[0]=='p':
            for item in queue:
                print(item)
    print(queue)
