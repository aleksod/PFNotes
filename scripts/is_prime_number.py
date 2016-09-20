num = int(raw_input('Enter your number: '))
current = num - 1

while current > 1:
    if num % current == 0:
        print 'Your nuber is not a prime number.'
        break
    elif current == 2:
        print 'Your number is a prime number'
        break
    else:
        current -= 1
    
