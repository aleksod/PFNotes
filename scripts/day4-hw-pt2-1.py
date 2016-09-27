usr_nums = (raw_input('enter a list of items separated by dashes ("-"): ')).split('-')
input = [int(i) for i in usr_nums]
usr_dict = dict()

for i in input:
    usr_dict[i] = i**2

print usr_dict
