usr_dictionary = dict()

while 1:
    input1 = str()
    input1 = str(raw_input(
    "Please enter a coordinate-word pair in the format (x, y, word): ")
    ).split(',')
    if input1[0] != str(''):
        input1[0] = input1[0].strip()
        input1[1] = input1[1].strip()
        input1[2] = input1[2].strip()
        usr_dictionary[input1[0] + ', ' + input1[1]] = input1[2]
    else:
        break
input2 = str(raw_input(
"Please provide a coordinate to look up a word at in the format (x, y): ")
).split(',')
input2[0] = input2[0].strip()
input2[1] = input2[1].strip()
print usr_dictionary.get(input2[0] + ', ' + input2[1], 'Coordinate not found')
