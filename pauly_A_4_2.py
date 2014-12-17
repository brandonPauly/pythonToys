def justWords(plainText): #Created a function to just remove puntuation and seperate words
    rmvApo=plainText.replace('\'','')
    hold=str.maketrans('?.,\\;-/$%&():"!',15*' ')
    noPunct=rmvApo.translate(hold)
    wordList=noPunct.split()
    return len(wordList)

def cesar(inpath,outpath,shift,mode):
    
    if mode<0 or mode>1:
        print('Invalid input. Please restart program... Goodbye.')
        quit()

    if shift > 25:
        shift=shift%25

    
    
    strAlpha='abcdefghijklmnopqrstuvwxyz'
    makeHash=strAlpha[shift:]+strAlpha[0:shift]
    

    infile=open(inpath,'r')
    wholeStr=infile.read()
    lineCount=len(infile.readlines())
    wordCount=justWords(wholeStr)
    charNum=len(wholeStr)
    infile.close()
    #return(lineCount,wordCount,charNum)
    
    
    
    if mode==0:
        transTable=str.maketrans(strAlpha,makeHash)
        encrypt=wholeStr.translate(transTable)
        outfile=open(outpath,'w')
        outfile.write(encrypt)
        outfile.close()

    if mode==1:
        transTable=str.maketrans(makeHash,strAlpha)
        decrypt=wholeStr.translate(transTable)
        outfile=open(outpath,'w')
        outfile.write(decrypt)
        outfile.close()

    
    return lineCount,wordCount,charNum
    

inpath=input('What is the path of your input file?:\n')
outpath=input('What is the path of your output file?:\n')
shift=eval(input('What cypher code are you operating with?\n'))
mode=eval(input('Are you encrypting or decrypting your file?  Please enter "0" for encryption or "1" for decryption:\n'))

cesar(inpath,outpath,shift,mode)
lineCount=cesar(inpath,outpath,shift,mode)[0]
wordCount=cesar(inpath,outpath,shift,mode)[1]
charNum=cesar(inpath,outpath,shift,mode)[2]
print('Line Count: '+str(lineCount)+'\nWord Count: '+str(wordCount)+'\nCharacter Count: '+str(charNum))
print('Your file is available at: '+outpath)

