import numpy

def f(num_rows, num_cols):
    return numpy.random.random_sample((num_rows, num_cols))

if __name__=="__main__":
    print f(5,3)
    print type(f(7,8))
    print f(3,5).shape
