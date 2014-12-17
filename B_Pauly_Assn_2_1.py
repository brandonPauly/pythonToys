x_r=eval(input('Enter x-coordinate for top right corner of your plane: '))
y_r=eval(input('Enter y-coordinate for top right corner of your plane: '))
x_l=eval(input('Enter x-coordinate for bottom left corner of the plane: '))
y_l=eval(input('Enter y-coordinate for bottom left corner of the plane: '))

if x_l>=x_r or y_l>=y_r:
    print('Error in coordinates! No plane exists. Restart program and enter new coordinates.')

x=eval(input('Enter x-coordinate for test point: '))
y=eval(input('Enter y-coordinate for test point: '))

if x_l<x<x_r and y_l<y<y_r:
    print('Your point resides within the plane!')

else:
    print('Your point resides outside of the plane.')
