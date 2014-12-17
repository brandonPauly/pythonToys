mult3=set()
mult5=set()
mult7=set()

setList=[mult3,mult5,mult7]

for i in range(100):
    if i%3==0:
        mult3.add(i)
    if i%5==0:
        mult5.add(i)
    if i%7==0:
        mult7.add(i)
a=set()
b=set()
for x in setList:
    for y in x:
        if y%35==0:
            a.add(y)
        if y%105==0:
            b.add(y)
c=mult3|mult7
d=mult3^mult7
e=mult7-mult3
