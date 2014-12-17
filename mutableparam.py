def g(lst):
    print("lst (in g), before assignment = ", lst)
    print("id(lst) (in g) = ", id(lst))
    print("id(lst[0]) (in g) = ", id(lst[0]))
    lst[0] = 5
    print("lst (in g), after assignment = ", lst)
    print("id(lst) (in g) = ", id(lst))
    print("id(lst[0]) (in g) = ", id(lst[0]))

def f():
    lst = [3, 6, 9, 12]
    print("lst (in f), before calling g = ", lst)
    print("id(lst) (in f) = ", id(lst))
    print("id(lst[0]) (in f) = ", id(lst[0]))
    g(lst)
    print("lst (in f), after calling g = ", lst)
    print("id(lst) (in f) = ", id(lst))
    print("id(lst[0]) (in f) = ", id(lst[0]))
