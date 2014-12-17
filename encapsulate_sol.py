def restore(myTuple, file):
    outfile = open(file, 'w')
    for f in myTuple:
        outfile.write(f + '\n')

def fourLetters(myTuple):
    count = 0
    for f in myTuple:
        if len(f) == 4:
            count+=1
    return count

myFriends ={'Tom', 'Paul', 'Mary', 'Nina', 'Ayse', 'Zheng', 'Carlos', 'Anne'}
fourF = fourLetters(myFriends)
restore(myFriends,'friends.txt')
print(fourF)
            
