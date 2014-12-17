def errorf():
    try:
        f = open('m2file.txt')
        s = f.readline()
        f.close()
        i = int(s)
        print(s)
        raise Exception("Here was the problem")
    except (IOError, FileNotFoundError) as err:
        print("I/O error: {}".format(err))
    except ValueError as e:
        print("Could not convert data to an integer {}.".format(e))
    except Exception as problem:
        print("Unexpected error: {}".format(problem))
        raise
