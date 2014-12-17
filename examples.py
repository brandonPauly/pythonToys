def example1():
    'returns true if no duplicates exist, otherwise returns false'
    l = [4, 1, 7, 2, 8, 3, 9]
    l.sort()
    for i in range(len(l)-1):
        if l[i] == l[i+1]:
            return False
    return True

def example2():
    'returns true if no duplicates exist, otherwise returns false'
    l = [4, 1, 7, 2, 8, 2, 3, 9]
    l.sort()
    for i in range(len(l)-1):
        if l[i] == l[i+1]:
            return False
    return True

def example3():
    'creates a new list from an old list, with no duplicates'
    l = [4, 1, 1, 7, 2, 8, 2, 3, 9, 8]
    l.sort()
    new=[]
    for i in range(len(l)):
        if i==0 or l[i] != l[i-1]:
            new.append(l[i])
    l = new
    return l

def example4(k):
    'returns the kth smallest number in the list'
    l = [4, 1, 7, 2, 8, 3, 9]
    l.sort()
    return l[k-1]

def example5():
    'returns the number in the list with the most occurrences'
    l = [4, 2, 7, 4, 5, 1, 4, 7, 7, 7, 7, 3, 2, 8, 9, 4, 6, 7, 3, 4, 5, 3, 5, 4, 5, 7, 7]
    l.sort()
    print(l)
    count = 1
    maxn = 1
    most = l[0]
    for i in range(1,len(l)):
        if l[i] == l[i-1]:
            count += 1
            continue
        elif count > maxn:
            maxn = count
            most = l[i-1]
        count = 0
    return most

import recBinarySearch
def example6():
    l = [4,1,7,2,8,3,9]
    l.sort()
    print(l)
    print(recBinarySearch.recBinarySearch(7,l))
    print(recBinarySearch.recBinarySearch(6,l))
