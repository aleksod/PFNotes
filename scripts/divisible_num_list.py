divider = int(raw_input("Please enter your integer to use as a divider: "))
divide_max = int(raw_input("Please enter your integer to generate the list: "))
the_list = list()
for i in range(divide_max):
    if i % divider == 0:
        the_list.append(i)
print the_list
