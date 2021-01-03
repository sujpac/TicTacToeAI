EMPTY_SPACE = '-'

def get_legal_moves(board, player):
    legal_moves = []
    for x, row in enumerate(board):
        for y, val in enumerate(row):
            if val == EMPTY_SPACE:
                legal_moves.append((x, y))
    return legal_moves

def get_opponent(who_am_i):
    if who_am_i == 'X':
        return 'O'
    elif who_am_i == 'O':
        return 'X'
    else:
        raise Exception("Unknown player: ", who_am_i)
