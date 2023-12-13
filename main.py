from IPython.display import clear_output

board = ['#','#','#','#','#','#','#','#','#','#',"X","O"]
win = False
def display_board(board):
    clear_output()
    print(board[9] + "|" + board[8] + "|" + board[7])
    print(board[6] + "|" + board[5] + "|" + board[4])
    print(board[3] + "|" + board[2] + "|" + board[1])

def player_input():
    player_one_marker = ''
    player_two_marker = ''
    marker = ''
    while marker != 'x' and marker != 'o':
        marker = input('Please input you marker "x"  or   "o"  ')
        if marker == "x":
            player_one_marker = 'x'
            player_two_marker = 'o'
        else:
            player_two_marker = 'x'
    return player_one_marker,player_two_marker


def check_win():
    global win
    if board[1] == "X" and board[2] == "X" and board[3] == "X" or board[1] == "O" and board[2] == "O" and board[3] == "O":
        win = True
    elif board[4] == "X" and board[5] == "X" and board[6] == "X" or board[4] == "O" and board[5] == "O" and board[6] == "O":
        win = True
    elif board[7] == "X" and board[8] == "X" and board[9] == "X" or board[7] == "O" and board[8] == "O" and board[9] == "O":
        win = True
    elif board[3] == "X" and board[5] == "X" and board[7] == "X" or board[3] == "O" and board[5] == "O" and board[7] == "O":
        win = True
    elif board[9] == "X" and board[5] == "X" and board[1] == "X" or board[9] == "O" and board[5] == "O" and board[1] == "O":
        win = True
    elif board[3] == "X" and board[6] == "X" and board[9] == "X" or board[3] == "O" and board[6] == "O" and board[9] == "O":
        win = True
    elif board[2] == "X" and board[5] == "X" and board[8] == "X" or board[2] == "O" and board[5] == "O" and board[8] == "O":
        win = True
    elif board[1] == "X" and board[4] == "X" and board[7] == "X" or board[1] == "O" and board[4] == "O" and board[7] == "O":
        win = True

def game():
    choice_marker = player_input()
    while win != True:
        print(f"First player turn {choice_marker[0]}")
        choice_first_player = int(input('Enter your choise Player # 1 '))
        board[choice_first_player] = 'X'
        display_board(board)
        choice_second_player = int(input('Enter your choise Player # 2 '))
        if board[choice_second_player] != 'X':
             board[choice_second_player] = 'O'
        else:
            print('Make a right choice')
            choice_second_player = int(input('Enter your choise Player # 2 '))
            board[choice_second_player] = 'O'
        display_board(board)
        check_win()


game()
