myList=[[1,1,2],[2,23,4],[34,2,4],[3,3,5],[67,5,45],[23,33,3],[1,0,0],[0,2,1]]
ansList=[]

for lst in myList:
    newList=[]
    for var in lst:
        newList.append(var**2)
    ansList.append(newList)
       

print(ansList)
