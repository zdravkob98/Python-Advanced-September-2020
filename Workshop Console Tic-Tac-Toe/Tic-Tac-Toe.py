from math import ceil

def setup():
    global player_one, player_two
    player_one_name = input('Player on name: ')
    player_two_name = input('Player on name: ')
    player_one_sign = input(f'{player_one_name} would you like to play with "X" or "O"?')
    player_two_sign = 'X' if player_one_sign == 'O' else 'O'
    player_one = [player_one_name, player_one_sign]
    player_two = [player_two_name, player_two_sign]
    print('This is the numeration of the board:')
    board = []
    n = 1
    for i in range(board_size):
        board.append([])
        for j in range(board_size):
            if len(str(n)) == 1:
                board[i].append(f'{n} ')
                
            else:
                board[i].append(n)
            n += 1
    for row in board:
        print('| ', end='')
        print(' | '.join([str(x) for x in row]), end='')
        print('|')
    print(f'{player_one_name} starts first!')

def play(current, board, board_size):
    choice = int(input(f'{current[0]} choose a free position [1-9]: '))
    row = ceil(choice / board_size) - 1
    col = choice % board_size - 1
    board[row][col] = current[1]
    draw_board(board)
    check_if_won(current, board, board_size)

def draw_board(board):
    for row in board:
        print('| ', end='')
        print(' | '.join([str(x) for x in row]), end='')
        print('|')

def check_if_won(current, board, board_size):
    global loop
    for i in range(board_size):
        if all([x == current[1] for x in board[i]]):
            print(f'{current[0]} won!')
            loop = False
    #rotate for checking
    new_board = [list(elem) for elem in list(zip(*board))]
    for i in range(board_size):
        if all([x == current[1] for x in new_board[i]]):
            print(f'{current[0]} won!')
            loop = False
    #first diagonal
    flag = True
    for i in range(board_size):
        if board[i][i] != current[1]:
            flag = False
            break
    if flag:
        print(f'{current[0]} won!')
        loop = False

    #second diagonal
    flag = True
    for i in range(board_size):
        for j in range(board_size):
            if i + j == board_size - 1:
                if board[i][j] != current[1]:
                    flag = False
                    break
    if flag:
        print(f'{current[0]} won!')
        loop = False




board_size = 3
player_one = None
player_two = None

board = [[' ']*board_size for i in range(board_size)]
setup()
current = player_one
other = player_two
loop = True

while loop:
    play(current, board, board_size)
    current, other = other, current
