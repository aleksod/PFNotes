list1 = [0, 3, 6, 9, 10, 2, 5]
list2 = [2, 6, 4, 7, 8, 1, 15]
list3 = list()

for i1 in list1:
    for i2 in list2:
        if i1 == i2:
            list3.append(i2)
list3.sort()
print list3
