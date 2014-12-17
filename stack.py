from reverseList import ReverseList

class Stack(object):
    'a representation of a stack'

    def __init__(self):
        'the constructor'
        self.trayStack=[]

    def push(self,item):
        'adds item to the stack'
        self.trayStack.append(item)

    def pop(self):
        'returns the top item from the stack'
        return self.trayStack.pop()

    def __repr__(self):
        'return the canonical representation of a stack'
        return repr(self.trayStack)

    def __str__(self):
        'returns the pretty representation of a stack'
        myS=''
        for i in range(len(self.trayStack)-1,-1,-1):
            myS+=str(self.trayStack[i])
            myS+='\n'
        return myS[0:-1]

    def size(self):
        'return the size of the stack'
        return len(self.trayStack)

    def isEmpty(self):
        'return True if the stack is empty'
        return self.size()==0

    def __iter__(self):
        'returns an iterator for the stack'
        return ReverseList(self.trayStack)
