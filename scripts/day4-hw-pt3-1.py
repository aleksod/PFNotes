input1 = set(raw_input("Please enter numbers separated by commas: ").split(','))
input2 = set(raw_input("Please enter numbers separated by commas, again: ").split(','))
common_nums = input1.intersection(input2)
print ', '.join(common_nums) #input1.intersection(input2)
