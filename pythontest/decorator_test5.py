def decorator(fn):
    def test(*args):
        print "My god!"*3
        return fn(*args)
    return test

@decorator
def other(a,b):
    print a**2 + b**2

if __name__=="__main__":
    other(4,3)
    other(3,4)
