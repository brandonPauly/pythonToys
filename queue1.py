# A very simple queue class that could use some doc strings

class queue(object):
    def __init__(self):
        'a constructor to initialize the queue to empty'
        self.q = []
        
    def dequeue(self):
        'removes an item from the front of the queue'
        return self.q.pop(0)
    
    def enqueue (self, item):
        'put an item into the back of the queue'
        return self.q.append(item)
    
    def size(self):
        'returns the number of items in the queue'
        return len(self.q)
    
    def isEmpty(self):
        'returns True is the queue is empty, False otherwise'
        return (self.size() == 0)
    
    def __repr__(self): # for the official string representation of queues
        #return self.q.__repr__()
        return repr(self.q)
    
    def __str__(self): # for the unofficial string representation, like printing queue objects
        return 'none of your business'
    
    # Ignore what follows for now
    def __getitem__(self, key):
        return self.q[key]
    def __setitem__(self, key, value):
      self.q[key] = value
    def __iter__(self):
        return self.q.__iter__()
