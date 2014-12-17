# CSC 242
# Spring 2013
# Lab 1 template

# Brandon Pauly
# Rachael Ramos & Gybran Somoza

# Question 1
def printTwoLargest():
    numSet=[]
    num=1
    while num>0:
        num=eval(input('Please enter a number: '))
        numSet.append(num)
    if len(numSet)>=2:
        print('The largest is ',max(numSet))
        numSet.remove(max(numSet))
        print('The second largest is ',max(numSet))
    elif len(numSet)<2 and numSet[0]<1:
        print('No positive numbers were entered.')
        

# Question 2
def printWordsLines(fname):
    infile=open(fname,'r')
    lineCount=0
    wordCount=0
    for line in infile:
        lineCount+=1
        sLine=line.split()
        for word in sLine:
            wordCount+=1
    print('The file ',fname,' contains ',lineCount,' lines and ',wordCount,' words.')
    infile.close()
        
        

# Question 3
def vote(clst):
    cDict={}
    unknown=0
    for cand in clst:
        cand1=cand.lower()
        cDict[cand1]=0
    choice=input('Enter a vote: ')
    choice1=choice.lower()
    if choice1 in cDict:
            cDict[choice1]+=1
    else:
        unknown+=1
    
    while choice!='':
        choice=input('Enter a vote:  ')
        choice1=choice.lower()
        if choice1 in cDict:
            cDict[choice1]+=1
        else:
            unknown+=1
    for key in cDict:
        if cDict[key]>1:
            print('There were '+str(cDict[key])+' votes for '+key.capitalize())
        else:
            print('There was 1 vote for '+key.capitalize())
    if unknown>1:
        print('There were '+str(unknown)+' votes for unknown.')
    else:
        print('There was 1 vote for unknown.')
        
        
