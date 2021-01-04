# tic-tac-toe-AI

The goal of this project is to build an optimized AI that plays tic-tac-toe. This is done by breaking it up into a few smaller sub-projects:

1. Build a Tic-Tac-Toe game or "engine" that allows two human players to play against each other locally
2. Insert simple, heuristic AI's into this game
3. Repeatedly play AI's against each other to see which of them is the best
4. Write minimax AI that computes the optimal move
5. Cache the intermediate states generated during execution of the minimax algorithm to significantly reduce the runtime

### Play a game against the minimax AI
```
python3 tictactoe.py human_player minimax_ai
```
