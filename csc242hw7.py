# CSC 242, Spring 2013
# Assign 7 
# Brandon Pauly

import os

rules={'Virus1':'iyfp9fg394g539gf',
       'Virus2':'9f8g8408h3498hff'}

# Put here for your reference only
# DO NOT MODIFY
def originalscan(pathname, signatures):
    'a version from the CSC 242 students'
    for item in os.listdir(pathname):
        n = os.path.join(pathname, item)
        try:
            originalscan(n, signatures) 
        except:
            f = open(n, 'r')
            s = f.read()
            for virus in signatures:
                if s.find(signatures[virus]) > 0:
                    print('{}, found virus {}'.format(n,virus))
            f.close()

# Question 1
# Write this function for the assignment
def scan(pathname, signatures, depth):
    for item in os.listdir(pathname):
        n = os.path.join(pathname, item)
        if depth < 0:
            return
        else:
            try:
                scan(n, signatures, depth-1)
            except:
                f = open(n, 'r')
                s = f.read()
                for virus in signatures:
                    if s.find(signatures[virus]) > 0:
                        print('{}, found virus {}'.format(n,virus))
                f.close()
            

# Question 2
def traverse(path, depth):
    tab=depth*2
    for item in os.listdir(path):
        n = os.path.join(path, item)
        print(' '*tab,end='')
        print(n)
        try:
            traverse(n, depth+1)
        except:
            pass
            

# Question 3
def search(fname, path):
    for item in os.listdir(path):
        n = os.path.join(path, item)
        if item == fname:
            return n
        else:
            try:
                x = search(fname, n)
                if x != None:
                    return x
                # If x is something other than None, you need
                # to return it
                # Right now you're not returning anything in this branch
            except:
                pass
    # Down here you need to return something but not x
    # If you've reached this point it's because you havne't
    # found anything yet
    # What you do you want to return in that case?
    return None

