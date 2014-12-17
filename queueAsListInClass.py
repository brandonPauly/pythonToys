# A very simple queue class that could use some doc strings
from reverseList import ReverseList

class queue(list):

    def dequeue(self):
        'removes an item from the back of the queue'
        return self.pop(0)
    
    def enqueue (self, item):
        'put an item into the front of the queue'
        return self.append(item)

    def sort(self):
        pass
    
    def size(self):
        'return the number of items in the queue'
        return len(self)
    
    def isEmpty(self):
        'returns True if the queue is empty, False otherwise'
        return (self.size() == 0)
    

