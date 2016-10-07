def perfect_square(num):
   '''
   Input:  Int
   Output: Bool

   Return True if num is a perfect square, e.g. 9 = 3 x 3. Return False if num is not
   a perfect square, 8 isn't any integer multiplied by itself.
   '''
   if int(num**0.5)**2 == num:
       return True
   else:
       return False

def next_perfect_square(num):
   '''
   Input:  Int
   Output: Int

   Ex: next_perfect_square(10) --> -1
       next_perfect_square(9) ---> 16
       next_perfect_square(25) --> 36
       next_perfect_square(37) --> -1

   Returns the next perfect square (a number that is the square of an integer e.g. 81 = 9 x 9)
   greater than the inputted number. If the inputted number is not a perfect square, return -1.
   (i.e. the inputted number must also be a perfect square).
   '''
   if perfect_square(num):
       return (int(num**0.5) + 1)**2
   else:
       return -1

print next_perfect_square(10)
print next_perfect_square(9)
print next_perfect_square(25)
print next_perfect_square(37)
