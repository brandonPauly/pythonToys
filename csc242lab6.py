# CSC 242, Spring 2013
# Lab 6
# Brandon Pauly

# Exercise 1
# Modify the following
def countdown(n):
    'counts down from n to 1'
    if n <= 0:
        print("Blast off!")
    elif n == 1:
        print('BOOM!')
        print('Just kidding!')
        print(n)
        countdown(n-1)
    else:
        print(n)
        countdown(n-1)

# Exercise 2
def countup(k, n):
    'counts up from k to n'
    if k <= n:
        countup(k,n-1)
        print(n)
    else:
        print('Let\'s go!')

