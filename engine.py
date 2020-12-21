BOARD_WIDTH = 3
BOARD_HEIGHT = 3

def new_board():
    board = [[None] * BOARD_WIDTH for _ in range(BOARD_HEIGHT)]
    return board

def render(board):
    for row in board:
        print(' '.join(row))

def get_move():
    pass

def make_move():
    pass

def get_winner():
    pass

def is_board_full():
    pass
