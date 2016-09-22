user_string = str(raw_input("Please enter your string: ")).lower()
new_string = str()
for i in range(len(user_string)):
    if i % 2 == 0:
        new_string += user_string[i]
    else:
        new_string += user_string[i].upper()
print new_string
