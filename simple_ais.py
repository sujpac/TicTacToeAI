import random

BOARD_WIDTH = 3
BOARD_HEIGHT = 3
EMPTY_SPACE = '-'

def random_ai(board, player):
    possible_moves = []
    for row in range(BOARD_HEIGHT):
        for col in range(BOARD_WIDTH):
            if board[row][col] == EMPTY_SPACE:
                possible_moves.append((row, col))
    return possible_moves[random.randint(0, len(possible_moves) - 1)]

def finds_winning_move_ai(board, player):
    return None
