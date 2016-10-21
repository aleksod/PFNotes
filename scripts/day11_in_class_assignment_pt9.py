import numpy as np

def f(integer):
    array = np.arange(integer)
    return np.cumsum(array)

if __name__=="__main__":
    print np.arange(9)
    print f(9)
