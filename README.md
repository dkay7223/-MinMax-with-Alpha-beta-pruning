# MinMax-with-Alpha-beta-pruning
# Chess Game with Min-Max Algorithm and Alpha-Beta Pruning Implementation

## I. Introduction

### Problem Statement
The assignment involves implementing a chess game where a player can play against the computer. The computer utilizes the Min-Max Algorithm with Alpha-Beta Pruning to make intelligent moves. The game is played on an 8x8 chessboard, with the objective of capturing the opponent's king to win the game.

## II. Requirements

1. **Chess Game Implementation:**
    - Develop a chess game playable against the computer.
    - Use the Min-Max Algorithm with Alpha-Beta Pruning for the computer's moves.
    - Display the chessboard and pieces after each move.
    - Keep track of moves made by both players.
    - Detect checkmate and declare the winner.
    - Detect stalemate and declare a draw.
    - Utilize a command-line-based user interface for displaying the chessboard.

## III. Solution Overview

### 1. **Chess Piece Symbol Function**

```python
def get_piece_symbol(piece):
    # Function returns Unicode symbols representing chess pieces based on their type.
    # Implemented for visual representation of the chessboard.
    # ...
```

### 2. **Board Initialization and Moves Tracking**

```python
# Board initialization using the chess library and moves tracking list
board = chess.Board()
moves = []
```

### 3. **Game Loop**

```python
while not board.is_game_over():
    # Display the chessboard and pieces after each move
    # Accept player's move in UCI notation or generate a random legal move for the computer
    # ...
```

### 4. **Evaluate Board Function**

```python
def evaluate_board(board):
    # Determine the score of a given chess position
    # Returns infinity or negative infinity for checkmate, 0 for stalemate, or material score otherwise
    # ...
```

### 5. **Minimax Algorithm with Alpha-Beta Pruning**

```python
def minimax(board, depth, alpha, beta, maximizing_player):
    # Implement the minimax algorithm with alpha-beta pruning to find the best move for the computer
    # ...
```

### 6. **Play Function**

```python
def play():
    # Main function to play the game against the computer
    # Accepts user input for moves and computes the computer's moves using the minimax algorithm
    # ...
```

## IV. Example Usage

```python
play()
print(board.result())
```

## V. Conclusion

The implementation provides an interactive chess game experience, allowing users to play against the computer. The use of the Min-Max Algorithm with Alpha-Beta Pruning ensures intelligent decision-making for the computer player. The code includes features to track moves, detect game outcomes, and display the chessboard after each move. Further enhancements can be explored, such as improving the user interface or experimenting with different algorithm parameters for increased gameplay sophistication.
