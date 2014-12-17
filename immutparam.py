def g(x):
    print("x (in g), before assignment = ", x)
    print("id(x) (in g) = ", id(x))
    x = 5
    print("x (in g), after assignment = ", x)
    print("id(x) (in g) = ", id(x))

def f():
    x = 3
    print("id(x) (in f) = ", id(x))
    g(x)
    print("x (in f) = ", x)
    print("id(x) (in f) = ", id(x))
