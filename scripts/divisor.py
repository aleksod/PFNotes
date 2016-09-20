my_num = int(raw_input('enter a number to find divisors of: '))
current = my_num - 1
while current > 1:
    if my_num % current == 0:
        print current
    current -= 1
