import chess
import random

#Implemented successfully, but showing some problems.

def get_piece_symbol(piece):
    """
    Using symbols insted of pieces
    """
    if piece.piece_type == chess.PAWN:
        return "♟"
    elif piece.piece_type == chess.KNIGHT:
        return "♞"
    elif piece.piece_type == chess.BISHOP:
        return "♝"
    elif piece.piece_type == chess.ROOK:
        return "♜"
    elif piece.piece_type == chess.QUEEN:
        return "♛"
    elif piece.piece_type == chess.KING:
        return "♚"


def evaluate_board(board):
    """
    Evaluates the current state of the board and returns a score.
    """
    material_score = sum([value for _, value in board.piece_map().items()])
    return material_score


def minimax(board, depth, alpha, beta, maximizing_player):
    """
    Implementation of the Min-Max Algorithm with Alpha-Beta Pruning
    to determine the best move for the computer.
    """
    if depth == 0 or board.is_game_over():
        return evaluate_board(board), None

    if maximizing_player:
        max_eval = float("-inf")
        best_move = None
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, False)[0]
            board.pop()
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float("inf")
        best_move = None
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, True)[0]
            board.pop()
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move


board = chess.Board()
moves = []

while not board.is_game_over():
    # adding side helping material
    print("    a b c d e f g h")

    # printing rows and columns
    for row in range(8):
        print(f"{8 - row} {'|'}", end=" ")
        for col in range(8):
            square = chess.square(col, 7 - row)
            piece = board.piece_at(square)
            if piece is None:
                print(".", end=" ")
            else:
                print(get_piece_symbol(piece), end=" ")
        print(f"{'|'} {8 - row}")

    print("    a b c d e f g h")

    if board.turn:
        move = input("Enter your move in UCI notation (e.g. e2e4): ")
        try:
            board.push_uci(move)
            moves.append(move)
        except ValueError:
            print("Invalid move, try again.")
    else:
        # Use Min-Max Algorithm with Alpha-Beta Pruning to determine the best move
        eval, move = minimax(board, 3, float("-inf"), float("inf"), True)
        print("Computer's move:", move.uci())
        board.push(move)
        moves.append(move.uci())

    # Display previous moves
    print("Previous moves:")
    for i, move in enumerate(moves):
        if i % 2 == 0:
            print(f"{i // 2 + 1}. {move}", end=" ")
        else:
            print(move)


def alpha_beta_minimax(board, depth, alpha, beta, maximizing_player):
    # Implementation of Min-Max Algorithm with Alpha-Beta Pruning
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    if maximizing_player:
        max_eval = float("-inf")
        for move in board.legal_moves:
            board.push(move)
            eval = alpha_beta_minimax(board, depth - 1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if alpha >= beta:
                break
        return max_eval
    else:
        min_eval = float("inf")
        for move in board.legal_moves:
            board.push(move)
            eval = alpha_beta_minimax(board, depth - 1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if alpha >= beta:
                break
        return min_eval


# Give player hints using Min-Max Algorithm with Alpha-Beta Pruning
if board.turn:
    print("It's your turn. You can:")
    best_move = None
    best_score = float("-inf")
    alpha = float("-inf")
    beta = float("inf")
    for move in board.legal_moves:
        board.push(move)
        score = -alpha_beta_minimax(board, 3, alpha, beta, False)
        board.pop()
        if score > best_score:
            best_move = move
            best_score = score
        alpha = max(alpha, score)
        if alpha >= beta:
            break
    print(f"Hint: Consider making move {best_move.uci()}\n")


def evaluate_board(board):
    # Evaluate the current state of the board

    material_score = sum([value for _, value in board.piece_map().items()])
    return material_score


