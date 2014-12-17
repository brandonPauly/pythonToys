name=input('What is your name? ')
age=eval(input('What is your age? '))
if age>=21:
    print('You can legally drink.')
else:
    print(name+', you have '+str(21-age)+' years until you are old enough to drink.')
if age<16:
    print('You also have '+str(16-age)+' years until you are old enough to drive.')
