def finalScore(scores):            #Function to remove highest and lowest scores, then returns sum of remaining six scores
                
    scores.remove(min(scores))
    scores.remove(max(scores))
    return(sum(scoreList))

def validate(scores):               #Function to ensure that the score list meets the correct criteria

    if len(scores)!=8:
        return False

    for n in scores:
        if 0<=n<=10:
            pass
        else:
            return False
    else:
        return True


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
    val=False
    while val is False:         #Ensures that the list meets the criteria (8 scores, numbers between 0 and 10
        
        scores=input('Input 8 scores for '+contestant+' seperated by a comma.\nPress Enter when finished.\n')
        scoreList=scores.split(',')
        for n in range(len(scoreList)):
            scoreList[n]=float(scoreList[n])
        val=validate(scoreList)

        
    masterList.append(finalScore(scoreList))
    

goldCount=masterList.count(max(masterList))

for n in range(len(contList)):      #Finds gold medal winner(s)
    print('Contestant: '+contList[n])
    print('Score: '+str(masterList[n]))
    if max(masterList)==masterList[n]:
        print('Gold Medal Winner!')
        print('\n')
    else:
        print('\n')
