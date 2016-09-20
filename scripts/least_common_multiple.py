num1 = int(raw_input('enter the first number: '))
num2 = int(raw_input('enter the second number: '))

if num1 <= num2:
    current = num1 + 1
else:
    current = num2 + 1

condition = 1
while 1:
    if current % num1 == 0 and current % num2 == 0 :
        print 'The least common multiple is ', current
        break
    current += 1
