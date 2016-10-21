import numpy

def f(array, integer):
    return numpy.random.choice(array, size = integer)

if __name__=="__main__":
    print f(numpy.array([1,2,3,4,5,6]),3)
