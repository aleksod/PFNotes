import numpy

def array_normalizer(array):
    return (array-array.mean())/array.std()

if __name__ == "__main__":
    x = numpy.array([1,2,3,4,5])
    print array_normalizer(x)
