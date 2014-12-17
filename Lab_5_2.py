def inputValidation(x):

    x=11

    while x<0 or x>10:
        x=eval(input('Please input a number:\n'))
        
        if x>=0 and x<=10:
            quit()

x=eval(input('Please input a number:\n'))        
inputValidation(x)
