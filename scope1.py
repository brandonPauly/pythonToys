#global scope
x = 99

# x and func are assigned in the module and are global

def func(y):
    z = x+y
    return z

def main():
    print(func(3))
    print(x)

main()
