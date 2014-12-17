from turtle import Turtle, bgcolor

n = 4

def koch(n):
##  directions = 'F'
##  for i in range(n):
##    directions = directions.replace("F","FLFRFLF")
##  return directions
  if n == 0:
    return 'F'
  else:
    s = koch(n-1)
    return s+'L'+s+'R'+s+'L'+s
  
directions = koch(n)

print('directions: ', directions)

t = Turtle()
bgcolor('black')
t.penup()
t.goto(-300,0)
t.pendown()
t.pencolor('yellow') 
t.pensize(3)

for move in directions:
    if move == 'F': t.fd(100/2**n)
    if move == 'L': t.lt(60)
    if move == 'R': t.rt(120)
