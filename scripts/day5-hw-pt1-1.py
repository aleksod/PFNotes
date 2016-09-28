def divisors(user_str):
    #user_str = raw_input('Please input a number to get the divisors of: ')
    user_inputted_num = int(user_str)

    print 'Our divisors are: '

    divisor = 1

    while divisor <= user_inputted_num:
        if user_inputted_num % divisor == 0:
            print divisor
        divisor += 1
    pass
