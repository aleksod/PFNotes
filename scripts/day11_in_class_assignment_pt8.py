import numpy

def f(array):
    array[array.argmax()] = 0
    return array

if __name__=="__main__":
    print f(numpy.array([1,2,3,4,5,6,3,2,1]))
