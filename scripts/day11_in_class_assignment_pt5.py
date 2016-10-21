import numpy

def f(x):
    return numpy.random.random_sample(x)

if __name__=="__main__":
    print f(5)
    print type(f(7))
    print f(3).shape
