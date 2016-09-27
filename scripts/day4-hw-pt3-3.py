usr_set = set()
usr_inp = str()
while usr_inp != 'q':
    usr_inp = str(raw_input("Please enter a word: "))
    if usr_inp != 'q' and usr_inp != 'v':
        usr_set.add(usr_inp)
    elif usr_inp == 'v':
        print ', '.join(usr_set)
    else:
        break
