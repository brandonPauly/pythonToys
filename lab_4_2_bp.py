def empLine(book):
    infile=open(book,'r')
    content=infile.readlines()
    count=0

    for line in content:
        if len(line)==1:
            count=count+1

    infile.close()
    return(count)
