def coin():
    import random
    flip=random.randrange(1,3)

    if flip==1:
        return('Heads')
    else:
        return('Tails')
