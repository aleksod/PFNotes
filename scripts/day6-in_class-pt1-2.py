def play_rock_paper_scissors(n_rounds):
   '''
   Input:  Int - number of rounds to play rock paper scissors for
   '''
   for _ in range(n_rounds):
       player_1 = raw_input('Player 1 play (r/p/s): ')
       player_2 = raw_input('Player 2 play (r/p/s): ')
       if player_1 == player_2:
           print("It's a tie!")
       elif player_1 == 'r' and player_2 == 's':
           print('Player 1 wins!')
       elif player_1 == 'r' and player_2 == 'p':
           print('Player 2 wins!')
       elif player_1 == 'p' and player_2 == 'r':
           print('Player 1 wins!')
       elif player_1 == 'p' and player_2 == 's':
           print('Player 2 wins!')
       elif player_1 == 's' and player_2 == 'r':
           print('Player 2 wins!')
       elif player_1 == 's' and player_2 == 'p':
           print('Player 1 wins!')
       else:
           print("Someone didn't play right!")

if p1 == p2:
    print "it is a tie"
elif (p1, p2) in (('r', 's'), ('s', 'p'), ('p', 'r')):
    print "player 1 wins"
else:
    print "player 2 wins"
