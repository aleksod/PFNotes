def list_prod(l):
    lprod = 1
    for n in l:
        lprod *= n
    return lprod

print list_prod([2,3,4,5,6,7])
