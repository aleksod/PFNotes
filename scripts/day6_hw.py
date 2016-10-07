if __name__ == "__main__":
    tic_tac_toe()

# Main function ================================================================
def tic_tac_toe():

    board_row1 = [(0, 0), (1, 0), (2, 0)]
    board_row2 = [(0, 1), (1, 1), (2, 1)]
    board_row3 = [(0, 2), (1, 2), (2, 2)]
    turn = 0

    game_is_not_over = True
    while game_is_not_over or turn != 9:
        current_player, current_symbol = whos_turn(turn)
        print_board(board_row1, board_row2, board_row3)
        input = tuple(str(raw_input("%s ( %s ), where will you play?"
        % current_player % current_symbol)).split(',').strip())
        if which_row(input, board_row1, board_row2, board_row3) == 1:
            board_row1 = alter_rows(input, board_row1, current_symbol)
        elif which_row(input, board_row1, board_row2, board_row3) == 2:
            board_row2 = alter_rows(input, board_row2, current_symbol)
        else:
            board_row3 = alter_rows(input, board_row3, current_symbol)
        turn += 1

    pass
# ==============================================================================

# Function for altering rows after input =======================================
def alter_rows(input, board_row, current_symbol):
    board_row[board_row.index(input)] = ' X '
    return board_row
# ==============================================================================

# Function for figuring out which row the user coordinate entry belongs to =====
def which_row(input, board_row1, board_row2, board_row3):
    if input in board_row1:
        return 1
    elif input in board_row2:
        return 2
    else:
        return 3
# ==============================================================================

# Function to print out the board after each turn ==============================
def print_board(a1, a2, a3):
    print a1
    print a2
    print a3
    pass
# ==============================================================================

# Function to print out whose turn this is and to return player name and his/her
# symbol (X or O) ==============================================================
def whos_turn(t):
    if t%2 + 1 == 1:
        player_name = "Player 1"
        symbol = 'X'
    elif t%2 + 1 == 2:
        player_name = "Player 2"
        symbol = 'O'
    print "{}'s turn".format(player_name)
    return player_name, symbol
# ==============================================================================
