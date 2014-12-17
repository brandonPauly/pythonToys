def finalScore():
    
    scrLst=[]
    while True:
        score=input('Input score for '+contestant+':\n')

            
        if score == '':
            if len(scrLst)<8:
                print('You are missing '+str(8-len(scrLst))+' score(s).')
                print('Here are the scores you have entered for '+contestant+':\n')
                for n in scrLst:
                    print(n)
                continue 
            for n in range(len(scrLst)):
                scrLst[n]=float(scrLst[n])

            
                
            scrLst.remove(min(scrLst))
            scrLst.remove(max(scrLst))
            return(sum(scrLst))
        if 0<=float(score)<=10:
            scrLst.append(score)
        else:
            print('Invalid input! Please re-enter last score:\n')
            continue


print('Good day, welcome to Judging Tool!')

contList=[]
masterList=[]

cont1=input('Please enter the name of the first contestant:\n')
contList.append(cont1)

cont2=input('Please enter the name of the second contestant:\n')
contList.append(cont2)

cont3=input('Please enter the name of the third contestant:\n')
contList.append(cont3)

for contestant in contList:
    print('Input 8 scores individually for '+contestant+'.\nPress Enter between scores.\nPress enter when finished.')
    contScore=finalScore()
    masterList.append(contScore)
    
    
