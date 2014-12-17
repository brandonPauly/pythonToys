def convert(degreesF):  #Function to convert celcius degrees to farenheit
    degreesC=(degreesF-32)*5/9
    return(degreesC)

x=50
y=100
z=2

def table(x,y,z):
    for temp in range(50,101,2):
        print('{:4.1f}\t{:5.2f}'.format(temp,convert(temp)))
