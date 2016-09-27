input = raw_input("input a list of words separated by commas: ")
inp = set([x.strip() for x in input.split(',')])

print ', '.join(inp) #input1.intersection(input2)
