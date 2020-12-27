from ast import literal_eval
import simple_ais as ai

BOARD_WIDTH = 3
BOARD_HEIGHT = 3
EMPTY_SPACE = '-'

def new_board():
    board = [[EMPTY_SPACE] * BOARD_WIDTH for _ in range(BOARD_HEIGHT)]
    return board

def render(board):
    for row in board:
        print(' '.join(row))
    print()

def get_move():
    tup_string = input('Enter Move (row, column): ')
    return literal_eval(tup_string)

def is_valid_move(board, move_coords):
    # check out-of-bounds
    if move_coords[0] < 0 or move_coords[0] >= BOARD_HEIGHT\
        or move_coords[1] < 0 or move_coords[1] >= BOARD_WIDTH:
        return False
    # check if the space is already taken
    if board[move_coords[0]][move_coords[1]] != EMPTY_SPACE:
        return False

    return True

def make_move(board, move_coords, player):
    if not is_valid_move(board, move_coords):
        raise Exception('{0} is an invalid move!'.format(move_coords))

    # TODO: change function to not mutate the arguments
    board[move_coords[0]][move_coords[1]] = player
    return True

def get_line_coords():
    line_coords = []
    # Add horizontal lines
    for row in range(BOARD_HEIGHT):
        line_coords.append([])
        for col in range(BOARD_WIDTH):
            line_coords[-1].append((row, col))
    # Add vertical lines
    for col in range(BOARD_WIDTH):
        line_coords.append([])
        for row in range(BOARD_HEIGHT):
            line_coords[-1].append((row, col))
    # Add diagonal lines
    # TODO: diagonal horizontal lines independent of board size
    line_coords.append([(0, 0), (1, 1), (2, 2)])
    line_coords.append([(0, 2), (1, 1), (2, 0)])

    return line_coords

def get_winner(board):
    line_coords = get_line_coords()
    lines = []

    for line_coord in line_coords:
        lines.append([board[row][col] for (row, col) in line_coord])

    for line in lines:
        if len(set(line)) == 1 and line[0] != EMPTY_SPACE:
            return line[0]

    return None

def is_board_full(board):
    for row in range(BOARD_HEIGHT):
        for col in range(BOARD_WIDTH):
            if board[row][col] == EMPTY_SPACE:
                return False
    return True

def play():
    players = [
        'X',
        'O'
    ]
    turn_number = 0
    board = new_board()

    while True:
        current_player = players[turn_number % 2]
        render(board)
        print("It's %s's turn!\n" % current_player)

        move_coords = get_move()
        # TODO: check if move is valid, raise exception if invalid
        # TODO: change make_move to be immutable
        make_move(board, move_coords, current_player)
        winner = get_winner(board)

        if winner:
            render(board)
            print('Winner is %s!\n' % winner)
            break

        if is_board_full(board):
            render(board)
            print("It's a draw!\n")
            break

        turn_number += 1
