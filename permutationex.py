def permutations(lst):
    lstLst = []
    if len(lst) == 0:
        return
    elif len(lst) == 1:
        lstLst.append(lst)
    else:
        x = permutations(lst[1:])
        for tlst in x:
            for num in range(len(lst)):
                y = list(tlst)
                y.insert(num,lst[0])
                lstLst.append(y)
    return lstLst
