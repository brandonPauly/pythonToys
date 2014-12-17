def safeOpen(file,mode):
    try:
        infile=open(file,mode)
        return(infile)
    except IOError:
        return None

def age():
    global age
    try:
        age=eval(input('What is your age?\n'))

    except:
        print('Your entry was invalid!\nPlease enter a numerical value.')
        age()
