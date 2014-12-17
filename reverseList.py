class ReverseList(object):

    def __init__(self,l):
        self.lst=l
        #self.index=len(l)-1
        self.index=len(l)
        
    def __next__(self):
        self.index-=1
        if self.index<0:
            raise StopIteration
##        res=self.lst[self.index]
##        self.index-=1
        return self.lst[self.index]
        
