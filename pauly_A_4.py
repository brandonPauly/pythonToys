def justWords(plainText): #Created a function to just remove puntuation and seperate words
    rmvApo=plainText.replace('\'','')
    hold=str.maketrans('?.,\\;-/$%&():"!',15*' ')
    noPunct=rmvApo.translate(hold)
    wordList=noPunct.split()
    return len(wordList) 

def cesar(inpath,outpath,shift,mode):  #Function to evaluate input and encryp or decrypt text
    
    if mode<0 or mode>1:
        print('Invalid input. Please restart program... Goodbye.')
        quit()

    if shift > 25:
        shift=shift%25

    
    
    strAlpha='abcdefghijklmnopqrstuvwxyz'
    makeHash=strAlpha[shift:]+strAlpha[0:shift] #Shifts alphabet by input value
    

    infile=open(inpath,'r')  #Opens file to collect text
    wholeStr=infile.read()
    lineCount=wholeStr.count('\n')
    wordCount=justWords(wholeStr)
    charNum=len(wholeStr)
    infile.close()
    
    
    
    if mode==0:  #Encrypts text
        transTable=str.maketrans(strAlpha,makeHash)
        encrypt=wholeStr.translate(transTable)
        outfile=open(outpath,'w')
        outfile.write(encrypt)
        outfile.close()

    if mode==1: #Decrypts text
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
print('Line Count: '+str(lineCount+1)+'\nWord Count: '+str(wordCount)+'\nCharacter Count: '+str(charNum))
print('Your file is available at: '+outpath)

