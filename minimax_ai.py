import copy
import engine
import utils

def minimax_ai(board, player):
    legal_moves = utils.get_legal_moves(board, player)
    opponent = utils.get_opponent(player)
    scores = []

    for move in legal_moves:
        _board = copy.deepcopy(board)
        engine.make_move(_board, move, player)
        score = _cached_minimax_score(_board, opponent, player)
        scores.append(score)

    sorted_best_moves = [x for _, x in sorted(zip(scores, legal_moves))]
    return sorted_best_moves[-1]

def _minimax_score(board, player_current, player_main):
    winner = engine.get_winner(board)
    opponent = utils.get_opponent(player_current)

    if winner == player_main:
        return 10
    elif winner == opponent:
        return -10
    elif engine.is_board_full(board):
        return 0

    legal_moves = utils.get_legal_moves(board, player_current)
    scores = []

    for move in legal_moves:
        _board = copy.deepcopy(board)
        engine.make_move(_board, move, player_current)
        score = _minimax_score(_board, opponent, player_main)
        scores.append(score)

    if player_current == player_main:
        return max(scores)
    else:
        return min(scores)

cache = {}

def _cached_minimax_score(board, player_current, player_main):
    winner = engine.get_winner(board)
    opponent = utils.get_opponent(player_current)

    if winner == player_main:
        return 10
    elif winner == opponent:
        return -10
    elif engine.is_board_full(board):
        return 0

    board_cache_key = str(board)
    is_main_player = player_current == player_main
    if board_cache_key in cache:
        scores = cache[board_cache_key]
        return max(scores) if is_main_player else min(scores)

    legal_moves = utils.get_legal_moves(board, player_current)
    scores = []

    for move in legal_moves:
        _board = copy.deepcopy(board)
        engine.make_move(_board, move, player_current)
        score = _cached_minimax_score(_board, opponent, player_main)
        scores.append(score)

    cache[board_cache_key] = scores
    if player_current == player_main:
        return max(scores)
    else:
        return min(scores)
