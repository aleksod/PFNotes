import random

def flip_coin():
   '''
   Input:  None
   Output: Str - 'H' for head or 'T' for tail

   Perform an "experiment" using random.random(), return 'H' if result is above .5, 'T' otherwise.
   '''
   if random.random()>0.5:
       return 'H'
   else:
       return 'T'

def roll_die():
   '''
   Input:  None
   Output: Int - Between 1 and 6

   Using random.randint(), perform a die roll and return the number that "comes up".
   '''
   return random.randint(1,6)

def flip_coin_roll_die(n_times):
   '''
   Input:  Int - number of times to flip a coin and roll a die
   Output: List - of tuples with the outcomes
      of the flips and rolls from each time
   '''
   return [(flip_coin(), roll_die()) for _ in range(n_times)]

print flip_coin_roll_die(10)
