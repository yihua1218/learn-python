try:
    a = 1.0 + "a"
    raise StopIteration("a", "b", "c")
    raise StopIteration("a")
    fh = open("testfile", "r")
    a = 1 / 0
    # raise IndexError #as test error
except Exception as e:
    excepName = type(e).__name__ # returns the name of the exception
    print(excepName)
    print(e.args)