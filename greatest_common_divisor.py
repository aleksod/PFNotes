num1 = int(raw_input('enter the first number: '))
num2 = int(raw_input('enter the second number: '))

if num1 <= num2:
    current = num1 - 1
else:
    current = num2 - 1

while current > 1:
    if num1 % current == 0 and num2 % current == 0 :
        print current
        break
    current -= 1
