def f2():
    'enter and print an integer'
    #this needs fixed
    num=eval(input('Enter an integer: '))
    while type(num) != int:
        num=eval(input('Your number is not of integer type.\nPlease enter an integer: '))
    print(num)
def f1(fname):
    'display the contents of fname to the console window'
    while True:
        try:
            infile=open(fname,'r')
            break
        except:
            print('I couldn\'nt find the file',fname)
            fname=input('Enter a file name: ')
        print(infile.read())
        infile.close()
