# CSC 242, Spring 2013
# Lab 8 
# Brandon Pauly

# Question 1
def rem(nlst):
    'produce a new list with one instance of each value removed'
    nlst.sort()
    tlst=[]
    for indx in range(1,len(nlst)):
        if nlst[indx] == nlst[indx-1]:
            tlst.append(nlst[indx])
    return tlst

# This code is for reference only
# DO NOT CALL this method
def moveTower(n, source, dest, temp):
    if n==1:
        print("Move disk from", source, "to", dest)
    else:
        moveTower(n-1, source, temp, dest)
        moveTower(1, source, dest, temp)
        moveTower(n-1, temp, dest, source)

# This code is for reference only
# DO NOT CALL this method
def hanoi(n):
    moveTower(n,1,3,2)

# Question 2
# Implement this method for the lab
# Again, DO NOT CALL hanoi() or moveTower()
def hanoiCount(n):
    '''recursively counts and returns the number of moves needed for the
Towers of Hanoi with n disks'''
    if n == 0 or n == 1:
        return 1
    else:
        return hanoiCount(n-1)*2+1
        
