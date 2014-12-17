def countWords():
    while True:
        try:
            content = open(input('Please enter the path of a file you want me to process:\n'))
            lst = content.read().split()
            return (len(lst))
            break
        except:
            print('No file can be found...')
            continue
        
