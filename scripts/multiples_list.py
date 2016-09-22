num_mult = int(raw_input('Enter the number to produce multiples of: '))
num_max = int(raw_input('Enter the number to obtain multiples up to: '))
the_list = list()
i = 1
while num_mult*i < num_max:
    the_list.append(num_mult*i)
    i += 1
print the_list
