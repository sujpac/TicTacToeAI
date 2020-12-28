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

def makes_winning_move_ai(board, player):
    line_coords = engine.get_all_line_coords()
    for line_coord in line_coords:
        line = [board[row][col] for (row, col) in line_coord]
        idx = _get_winning_move(line, player)
        if idx >= 0:
            return line_coord[idx]

    return random_ai(board, player)

def makes_winning_and_blocks_losing_move_ai(board, player):
    line_coords = engine.get_all_line_coords()
    for line_coord in line_coords:
        line = [board[row][col] for (row, col) in line_coord]
        idx = _get_winning_move(line, player)
        if idx >= 0:
            return line_coord[idx]
    for line_coord in line_coords:
        line = [board[row][col] for (row, col) in line_coord]
        idx = _get_losing_move(line, player)
        if idx >= 0:
            return line_coord[idx]

    return random_ai(board, player)

def _get_winning_move(line, player):
    # if the line has 2 taken spaces and 1 empty space, there is a winning move
    # this function returns the index of the winning move
    # TODO: change this function so it works for any board size
    if EMPTY_SPACE not in line:
        return -1
    if line[0] == player and line[1] == player:
        return 2
    if line[0] == player and line[2] == player:
        return 1
    if line[1] == player and line[2] == player:
        return 0
    return -1

def _get_losing_move(line, player):
    # a line with 2 opponent-taken spaces and 1 empty space has a losing move
    # this function returns the index of the losing move
    # TODO: change this function so it works for any board size
    # TODO: change this function to get & use the opposite player's symbol
    if EMPTY_SPACE not in line:
        return -1
    if player in line:
        return -1
    if line[0] != EMPTY_SPACE and line[1] != EMPTY_SPACE:
        return 2
    if line[0] != EMPTY_SPACE and line[2] != EMPTY_SPACE:
        return 1
    if line[1] != EMPTY_SPACE and line[2] != EMPTY_SPACE:
        return 0
    return -1
