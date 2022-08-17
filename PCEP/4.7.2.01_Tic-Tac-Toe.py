import random

def display_board(board):
    hbar =  '+-------+-------+-------+'
    elin =  '|       |       |       |'

    for e,r in enumerate(board):
        print(hbar)
        print(elin)
        print(f'|   {r[0]}   |   {r[1]}   |   {r[2]}   |')
        print(elin)
        if e>1:
            print(hbar)

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    get_in = int(input('Your move:'))

    if get_in in range(1,10):
        for e,r in enumerate(board):
            if get_in in r:
                if get_in > 3:
                    if board[e][(get_in)%3-1] == get_in:
                        board[e][(get_in)%3-1] = 'O'
                else:
                    if board[e][get_in-1] == get_in:
                        board[e][get_in-1] = 'O'
    else:
        print('Wrong number!!!')

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_pairs = []
    for e,r in enumerate(board):
        for c in range(0,len(r)):
            if board[e][c] not in ('X','O'):
                free_pairs.append((e,c,))
    return free_pairs

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game

    victory_positions = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(2, 0), (1, 1), (0, 2)],
    ]

    # Collect the existing moves for a specific sign
    moves = []
    for e,r in enumerate(board):
        for c in range(0,len(r)):
            if board[e][c] == sign:
                moves.append((e,c,))

    # Now, I need to check if these moves can match any of winning positions
    rd = {}
    for m in moves:
        for e,v in enumerate(victory_positions):
            for vp in v:
                if m == vp:
                    if e in rd:
                        rd[e] += 1
                    else:
                        rd[e] = 1

    for k,v in rd.items():
        if v == 3:
            return sign


def computer_move(board):
    # The function draws the computer's move and updates the board.
    options = make_list_of_free_fields(board)
    # print('OPTIONS: ',options)

    a = random.randint(0,len(options)-1)
    # print('RANDOM:', a)

    if a:
        move = options[a]
        # print(options, a, move)
        board[move[0]][move[1]] = 'X'

init_board = [[1,2,3],[4,'X',6],[7,8,9]]
display_board(init_board)

while True:
    enter_move(init_board)
    try:
        computer_move(init_board)
    except:
        print('No more moves...')
        break
    finally:
        display_board(init_board)

    # print(init_board)
    if victory_for(init_board, 'O'):
        print('WINNER IS O!')
        break
    if victory_for(init_board, 'X'):
        print('WINNER IS X!')
        break
