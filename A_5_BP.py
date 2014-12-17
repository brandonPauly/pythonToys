
totDist=0
totTime=0
totRuns=0
runList=[]

print('Hello, welcome to your training run log!')
switch=input('Do you have run data to enter?\nEnter y for yes, n for no:\n')


if (switch=='n'):
    print('Goodbye.')
    quit()



while(switch!='n' and switch!='y'):
    switch=input('Invalid input...\nPlease re-enter choice.\nEnter y for yes, n for no:\n')
    

while (switch=='y'):
    
    distance=eval(input('What is the distance of the run in miles?\n'))
    time=eval(input('What was the time taken to run in minutes?\n'))
    totDist+=distance
    totTime+=time
    totRuns+=1
    runList.append(distance)
    print('Your pace was: '+str('{:5.2f}'.format(time/distance))+' min/mile.')



    switch=input('Do you have run data to enter?\nEnter y for yes, n for no:\n')

    while(switch!='n' and switch!='y'):
        switch=input('Invalid input...\nPlease re-enter choice.\nEnter y for yes, n for no:\n')



print('You entered a total of '+str(totRuns)+' runs this session!')
if(totDist)>0:
    print('Your total mileage was: '+str(totDist)+ ' miles')
    print('Your average pace was: '+str('{:5.2f}'.format(totTime/totDist))+' min/mile.')
if len(runList)>0:
    print('Your longest run was: '+str(max(runList))+' miles')
