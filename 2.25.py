neighbors={'NE':'Tom',
           'E':'Paul',
           'SE':'Anne',
           'S':'Donna',
           'SW':'Danny',
           'W':'Tim',
           'NW':'Rick',
           'N':'Rham'}
           
def invoice(item,quant):
    merch={'a':2,
           'b':3,
           'c':4,
           'd':4,
           'e':5}

    return(merch[item]*quant)

def wordcount(text):
    counters={}
    wordList=text.split()
    for word in wordList:
        if word in counters:
            counters[word]+=1
        else:
            counters[word]=1
    for word in counters:
        if counters[word]==1:
            print('{:8} appears {} time.'.format(word,counters[word]))
        else:
            print('{:8} appears {} times.'.format(word,counters[word]))


def playRPS():
    import random
    myList=['Rock','Paper','Scissors']
    return random.choice(myList)


