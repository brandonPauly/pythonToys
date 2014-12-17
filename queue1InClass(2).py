# A very simple queue class that could use some doc strings
from reverseList import ReverseList

class queue(object):
    def __init__(self):
        'a constructor that initialize the queue to empty'
        self.q = []
        
    def dequeue(self):
        'removes an item from the back of the queue'
        return self.q.pop()
    
    def enqueue (self, item):
        'put an item into the front of the queue'
        return self.q.insert(0,item)
    
    def size(self):
        'return the number of items in the queue'
        return len(self.q)
    
    def isEmpty(self):
        'returns True if the queue is empty, False otherwise'
        return (self.size() == 0)
    
    def __repr__(self): # for the official string representation of queues
        return self.q.__repr__()
        #return repr(self.q)
##        copyQ=list(self.q)
##        copyQ.reverse()
##        return repr(copyQ)
    
    def __str__(self): # for the unofficial string representation, like printing queue objects
        #return 'none of your business'
        return str(self.q)
    

    def __getitem__(self, key):
        return self.q[len(self.q)-key-1]
    def __setitem__(self, key, value):
      self.q[len(self.q)-key-1] = value
    def __iter__(self):
        #return self.q.__iter__()
        #return iter(self.q)
        return ReverseList(self.q)

