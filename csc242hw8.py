# CSC 242, Spring 2012
# Assignment 8 template
# Brandon Pauly

import os

# Question 1
def itemCount(lst):
    '''Function that takes an arbitrarily nested list as a parameter
and returns the number of items in the list.'''
    items = 0
    if len(lst) == 0:
        return 0
    if type(lst[0]) != list:
        items += 1
    else:
        items += itemCount(lst[0])
    items += itemCount(lst[1:])
    return items

# Question 2
def fileCount(path):
    '''Function that takes a string representing a directory path as a parameter
and returns the number of files in the directory path, and any subdirectory
underneath the directory path.'''
    files = 0
    for obj in os.listdir(path):
        n = os.path.join(path, obj)
        try:
            files += fileCount(n)
        except:
            files += 1
    return files
