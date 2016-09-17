my_num = int(raw_input('Enter a number to find the sum up to: '))
sum_result = 0
current = my_num
while current > 0:
    sum_result += current
    current -= 1
print sum_result
