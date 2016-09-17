my_num = int(raw_input('Enter a number to find the factorial of: '))
fac_result = 1
current = my_num
while current > 0:
    fac_result *= current
    current -= 1
print fac_result
