print 'Enter elements of the first list separated by "Enter" key'
list1 = list()
for i in range(7):
    list1.append(int(raw_input()))

print 'Enter elements of the second list separated by "Enter" key'
list2 = list()
for i in range(7):
    list2.append(int(raw_input()))

list3 = list()

for i1 in list1:
    for i2 in list2:
        if i1 == i2:
            list3.append(i2)
list3.sort()
print list3
