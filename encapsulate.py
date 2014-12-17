def restore(someTuple,file):
    outfile = open(file, 'w')
    for f in someTuple:
        outfile.write(f + '\n')

def fourLetters(someTuple):
    count = 0
    for f in someTuple:
        if len(f) == 4:
            count+=1
    return count

myFriends ={'Tom', 'Paul', 'Mary', 'Nina', 'Ayse', 'Zheng', 'Carlos', 'Anne'}
fourF = fourLetters(myFriends)
restore(myFriends,'friends.txt')
print(fourF)
            
