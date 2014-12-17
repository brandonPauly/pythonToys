def avgWordLength(text):


    infile=open(text,'r')
    string=infile.read()
    words=string.split()
    infile.close()

    char=0
    for x in words:
        char+=len(x)

    average=char/len(words)

    return(average)
        
