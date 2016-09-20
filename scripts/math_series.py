num = int(raw_input('Please enter the nth element in the series: '))
num_index = 1
a = 1
while num_index <= num:
    a = 2*a + 1
    num_index += 1
print 'The', num, 'st/nd/rd/th element in the series is', a
