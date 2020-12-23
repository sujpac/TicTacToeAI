from ast import literal_eval
import random

BOARD_WIDTH = 3
BOARD_HEIGHT = 3
EMPTY_SPACE = '-'

def new_board():
    board = [[EMPTY_SPACE] * BOARD_WIDTH for _ in range(BOARD_HEIGHT)]
    return board

def render(board):
    for row in board:
        print(' '.join(row))
    print('')

def get_move():
    tup_string = input('Enter Move (row, column): ')
    return literal_eval(tup_string)

def make_move(board, move, player):
    board[move[0]][move[1]] = player
    # TODO: add logic for invalid moves
    return True

def get_winner(board):
    lines = []
    # Add horizontal lines
    for row in range(BOARD_HEIGHT):
        lines.append([])
        for col in range(BOARD_WIDTH):
            lines[-1].append(board[row][col])
    # Add vertical lines
    for col in range(BOARD_WIDTH):
        lines.append([])
        for row in range(BOARD_HEIGHT):
            lines[-1].append(board[row][col])
    # Add diagonal lines
    # TODO: diagonal horizontal lines independent of board size
    lines.append([board[0][0], board[1][1], board[2][2]])
    lines.append([board[0][2], board[1][1], board[2][0]])

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

        move_coords = random_ai(board, current_player)
        # TODO: check if move is valid, raise exception if invalid
        # TODO: change make_move to be immutable
        make_move(board, move_coords, current_player)
        winner = get_winner(board)

        if winner:
            print('Winner is %s!\n' % winner)
            render(board)
            break

        if is_board_full(board):
            print("It's a draw!")
            render(board)
            break

        turn_number += 1

def random_ai(board, player):
    possible_moves = []
    for row in range(BOARD_HEIGHT):
        for col in range(BOARD_WIDTH):
            if board[row][col] == EMPTY_SPACE:
                possible_moves.append((row, col))
    return possible_moves[random.randint(0, len(possible_moves) - 1)]
