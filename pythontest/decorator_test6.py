def funA(a):
    def insideA(*args):
        print "funA"
        return a(*args)
    return insideA

def funB(b):
    def insideB(*args):
        print "funB"
        return b(*args)
    return insideB

@funA
@funB
def funC():
    print "funC"

funC()
