list_Animals=['goat','octopus','platypus','rat','lion','eel','snake','eagle','tarantula','bat']
list_Values=[3,6,10,1,7,8,3,6,9,5]
animal=input('Go ahead. Try to guess an animal in my list: ')

if animal in list_Animals:
    print('Nice going! '+animal.capitalize()+' is in my list!')
    print('You\'ve earned '+str(list_Values[list_Animals.index(animal)])+' points!')
else:
    list_Animals.append(animal)
    print('You\'ve contributed a new animal to the game!')
    new_Val=eval(input('Select a value for your animal between 1 & 10. The more rare the animal, the more points it should be worth: '))
    list_Values.append(new_Val)
    print(list_Animals)
