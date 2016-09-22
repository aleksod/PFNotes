user_num = int(raw_input("Please enter your integer: "))
the_list = list()
for i in range(user_num):
    if i % 2 == 0:
        the_list.append(i)
print the_list
