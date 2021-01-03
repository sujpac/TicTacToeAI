import engine
import simple_ais as ai
import minimax_ai as mm

try:
    board = engine.new_board()
    move_coords = (2, 0)
    engine.make_move(board, move_coords, "X")
    engine.make_move(board, move_coords, "X")
except Exception as exption:
    print('Threw an exception: {0}'.format(exption))
# => should always throw exception


print()
board = [
  ['X', 'O', '-'],
  ['-', 'O', '-'],
  ['X', '-', '-']
]
print(ai.makes_winning_move_ai(board, 'X'))
print(ai.makes_winning_move_ai(board, 'X'))
# => should always print (1, 0)

print(ai.makes_winning_move_ai(board, 'O'))
print(ai.makes_winning_move_ai(board, 'O'))
# => should always print (2, 1)

print()
board = [
  ['O', '-', '-'],
  ['-', 'O', 'X'],
  ['O', 'X', 'X']
]
print(ai.makes_winning_and_blocks_losing_move_ai(board, 'X'))
# => should always print (0, 2)
# => if it's printing (1, 0), the ai is blocking the losing move prematurely

print()
board = [
  ['O', '-', '-'],
  ['-', 'O', 'X'],
  ['O', 'X', 'X']
]
print(mm.minimax_ai(board, 'X'))
# => should always print (0, 2)
