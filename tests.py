import engine
import simple_ais as ai

try:
    board = engine.new_board()
    move_coords = (2, 0)
    engine.make_move(board, move_coords, "X")
    engine.make_move(board, move_coords, "X")
except Exception as exption:
    print('Threw an exception: {0}\n'.format(exption))
# => should always throw exception

board = [
  ['X', 'O', '-'],
  ['-', 'O', '-'],
  ['X', '-', '-']
]
print(ai.finds_winning_move_ai(board, 'X'))
print(ai.finds_winning_move_ai(board, 'X'))
# => should always print (1, 0)

print(ai.finds_winning_move_ai(board, 'O'))
print(ai.finds_winning_move_ai(board, 'O'))
# => should always print (2, 1)
