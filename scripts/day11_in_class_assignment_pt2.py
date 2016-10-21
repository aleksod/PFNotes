import numpy

def array_normalizer(X):
    return (X-X.mean(axis=0))/X.std(axis=0)

if __name__ == "__main__":
    x = numpy.array([[1,2,3,4,5], [6,7,8,9,0]])
    print array_normalizer(x)
