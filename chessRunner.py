import chess
import random


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


board = chess.Board()
moves = []

while not board.is_game_over():
    #adding side helping material
    print("    a b c d e f g h")
  
    
    #printing rows and columns
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
 
    #Computer's / User's turn, appending the board
    if board.turn:
        move = input("Enter your move in UCI notation (e.g. e2e4): ")
        try:
            board.push_uci(move)
            moves.append(move)
        except ValueError:
            print("Invalid move, try again.")
    else:
        # Generate a random legal move for the computer
        #Returns a set of legal moves
        legal_moves = list(board.legal_moves)
        computer_move = random.choice(legal_moves)
        print("Computer's move:", computer_move.uci())
        board.push(computer_move)
        moves.append(computer_move.uci())

    # Display previous moves
    print("Previous moves:")
    for i, move in enumerate(moves):
        if i % 2 == 0:
            print(f"{i // 2 + 1}. {move}", end=" ")
        else:
            print(move)

    # Give player hints
    #I tried to select hints using Alpha beta or minmax, but there seem to be an error
    #anyways, not the requiremtns
    if board.turn:
        print("It's your turn. You can:")
        for move in board.legal_moves:
            print(move.uci(), end=" ")
        print()


def evaluate_board(board):
    if board.is_checkmate():
        if board.turn:
            return float('-inf')
        else:
            return float('inf')
    elif board.is_stalemate() or board.is_insufficient_material():
        return 0
    else:
        material_score = sum([value for _, value in board.piece_map().items()])
        if board.turn:
            return material_score
        else:
            return -material_score


# Updating the computer's random moves using Alpha beta pruning
def minimax(board, depth, alpha, beta, maximizing_player):
    """
    The minimax algorithm with alpha-beta pruning to determine the best move for the computer player
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


def play():
    """
    Main function to play the game against the computer
    """
    board = chess.Board()
    while not board.is_game_over():
        print(board)
        if board.turn == chess.WHITE:
            move = input("Enter your move in UCI notation (e.g. e2e4): ")
            while chess.Move.from_uci(move) not in board.legal_moves:
                print("Illegal move, try again")
                move = input("Enter your move in UCI notation (e.g. e2e4): ")
            board.push(chess.Move.from_uci(move))
            print("Your move: ", move)
        else:
            eval, move = minimax(board, 3, float("-inf"), float("inf"), True)
            board.push(move)
            print("Computer's move: ", move)
            print("Computer's evaluation: ", eval)
        print("Previous moves: ", list(board.move_stack))
    print("Game over, winner: ", board.result())


play()


print(board.result())
