import random
import engine

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
    line_coords = engine.get_line_coords()
    for line_coord in line_coords:
        line = [board[row][col] for (row, col) in line_coord]
        idx = _has_winning_move(line, player)
        if idx > 0:
            return line_coord[idx]

    return random_ai(board, player)

def _has_winning_move(line, player):
    # the line should have 2 taken cells and 1 empty cell
    if EMPTY_SPACE not in line:
        return -1
    if line[0] == player and line[1] == player:
        return 2
    if line[0] == player and line[2] == player:
        return 1
    if line[1] == player and line[2] == player:
        return 0
    return -1
