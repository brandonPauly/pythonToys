def censor(fileName):
    infile=open(fileName,'r')
    content=infile.read()
    removep=content.replace('\'','')
    hold=str.maketrans('?.,\\;-/$%&():"!',15*' ')
    newStr=removep.translate(hold)
    words=newStr.split()

    infile.close()

    newList=[]
    for word in words:

        
        if len(word)==4:
            newList.append('xxxx')

        else:
            newList.append(word)




    b2string=('')
    for i in newList:
        b2string=(str(b2string)+' '+i+' ')

    

    outfile=open('censor.txt','w')
    outfile.write(str(b2string))
    outfile.close()
