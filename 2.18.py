def multmult(x,y):
    newList=[]
    for i in x:
        for j in y:
            newList.append(i*j)

    return(newList)


def add2D(lst):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            lst[i][j]+=1

    return(lst)

def greater2(lst,x):
    for i in range(len(lst)):
        if lst[i]>x:
            return(i)
    return len(lst)


def greater(lst,x):
    i=0
    while i<len(lst):
        if lst[i]>x:
            return (i)

        i+=1
    return len(lst)
            

def interest(x):
    amt=1
    amt2=amt*2
    year=0
    while amt<=amt2:
        amt+=amt*x
        year+=1

    return(year)

def hello():
    while True:
        name=input('What\'s your name?\n')
        if name=='':
            return
        print('Hello,',name)


def interact():
    numList=[]
    intg=eval(input('Enter value: '))
    numList.append(intg)

    while intg !=0:
        intg=eval(input('Enter value: '))
        if intg >0:
            numList.append(intg)

    return(numList)
        
        
def csv2py(fname):
    infile=open(fname,'r')
    list=[]
    for line in infile:
        subList=line.replace('\n','')
        newList=subList.split(',')
        list.append(newList)
    print(list)
    infile.close()
    
