class MyClass(object):
    '''a user-defined wrapper class'''

    version = 1.0               # add a version number to the class
        
    def setTo(self, value):    # setTo is a class method
        'sets the instance variable data to value'
        self.data = value      # data is an instance variable

    def get(self):             # get is a class method
        'returns the value of the instance variable data'
        return self.data       # data is an instance variable

    def double(self):
        
        #self.data=self.data*2
        self.data*=2

    def ntimes(self,mult):

        #self.data=self.data*mult
        self.data*=mult

class Animal(object):

    def setspec(self,spec):
        self.setspec=spec

    def setlang(self,lang):
        self.setlang=lang

    def speak(self):
        return('I am a '+self.setspec+' and I '+self.setlang+'.')

class Bird(Animal):

    def fly(self,n):
        return 'I am flying {} feet.'.format(n)
