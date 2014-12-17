def wordcount(para):
    z=para.replace('\'','') #removes apostrophes, so not to split up contractions
    hold=str.maketrans('?.,\\;-/$%&():"!',15*' ') #sets map for characters to be replaced with whitespace
    newStr=z.translate(hold) #replaces said characters with whitespace
    numList=[]
    paraList=newStr.split()

    for word in paraList:
        numList.append(len(word)) #adds word length to new list considering each word in string list

    numList.sort()
    solList=[]

    for num in numList: #iterates through numbers and counts occurrences, then inserts data into corresponding place in sublist
        x=num
        y=numList.count(num)
        subList=[x,y]
        if subList not in solList:
            solList.append(subList)
    return(solList)

def justWords(punctText): #Created a function to just remove puntuation and seperate words
    a=punctText.replace('\'','')
    stop=str.maketrans('?.,\\;-/$%&():"!',15*' ')
    newStop=a.translate(stop)
    onlyChar=newStop.split()
    return(onlyChar)

text1=input('Please input a piece of text:\n')
text2=input('Please input a second piece of text:\n')

newText1=justWords(text1) #applies function to remove punctuation and create word lists
newText2=justWords(text2)

textList=[]

if len(newText1)==len(newText2): #alternates words from two word lists into new list if length of lists are equal
    for word in newText1:
        textList.append(word)
        textList.append(newText2[newText1.index(word)])

if len(newText1)>len(newText2): #alternates words from two word lists into new list if first list is larger than second
    slc1=newText1[(len(newText1)-(len(newText1)-len(newText2))):]
    slc2=newText1[:(len(newText1)-(len(newText1)-len(newText2)))]
    slc3=newText2[:(len(newText1)-(len(newText1)-len(newText2)))]
    for word in slc2:
        textList.append(word)
        textList.append(slc3[slc2.index(word)])
    for word in slc1:
        textList.append(word)

elif len(newText2)>len(newText1): #alternates words from two word lists into new list if second list is larger than first
    slc1=newText2[(len(newText2)-(len(newText2)-len(newText1))):]
    slc2=newText1[:(len(newText1)-(len(newText1)-len(newText2)))]
    slc3=newText2[:(len(newText1)-(len(newText1)-len(newText2)))]
    for word in slc2:
        textList.append(word)
        textList.append(slc3[slc2.index(word)])
    for word in slc1:
        textList.append(word)

b2string=('') #converts alternated list to a string
for word in textList:
    b2string=(str(b2string)+' '+word+' ')
print(b2string)    
    
fin=wordcount(b2string) #applies wordcount function to alternated string

print(fin)
