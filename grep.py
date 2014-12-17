class textfile(object):
    ''' a class used to represent text files and
        to provide wordcount and grep functionalities'''
    ntfiles = 0 # count of number of textfile objects

    def linecount(self):
        self.nlines=0
        for line in self.lines:
            self.nlines+=1
        

    def charcount(self):
        self.nchar=0
        for line in self.lines:
            for char in line:
                self.nchar+=1
        
                
        
        
    
    def __init__(self,fname):
        textfile.ntfiles += 1
        self.name = fname # name
        self.nwords = 0
        self.nlines=0
        self.nchar=0
        self.fh = open(fname, 'r') # handle for the file
        self.lines = self.fh.readlines()
        self.wordcount()
        self.linecount()
        self.charcount()
        self.fh.close()
        
    def wordcount(self):
        "finds the number of words in the file"
        for l in self.lines:
            w = l.split()
            self.nwords += len(w)
            
    def grep(self,target):
        "prints out all lines containing target"
        for l in self.lines:
            if l.find(target) > 0:
                print(l, end='')

a = textfile('grep.py')
b = textfile('methods.py')
print("the number of text files available is", textfile.ntfiles)
print("here is some information about them (name, words, lines, characters):")
for f in [a,b]:
    print(f.name, f.nwords,f.nlines,f.nchar)
    f.grep('self')
