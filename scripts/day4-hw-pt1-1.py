usr_nums = (raw_input('enter a list of items separated by commas: ')).split(',')
input = [int(i) for i in usr_nums]
if len(input) % 2 == 1:
    input.pop()
zipped = zip(input[0::2], input[1::2])
print zipped
