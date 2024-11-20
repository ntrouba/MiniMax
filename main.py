import chess
from datetime import datetime

PIECE_VALUES = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.ROOK: 5,
    chess.QUEEN: 9,
    chess.KING: 1000
}

def evaluate_board(board):
    score = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            value = PIECE_VALUES.get(piece.piece_type, 0)
            score += value if piece.color == chess.WHITE else -value
    return score

def Max(board, depth):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board), None

    max_eval = float('-inf')
    best_move = None

    for move in board.legal_moves:
        new_board = board.copy()
        new_board.push(move)
        eval, _ = Min(new_board, depth - 1)
        if eval > max_eval:
            max_eval = eval
            best_move = move

    return max_eval, best_move

def Min(board, depth):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board), None

    min_eval = float('inf')
    best_move = None

    for move in board.legal_moves:
        new_board = board.copy()
        new_board.push(move)
        eval, _ = Max(new_board, depth - 1)
        if eval < min_eval:
            min_eval = eval
            best_move = move

    return min_eval, best_move

def botMoves(board, depth=2):
    _, best_move = Max(board, depth)
    if best_move:
        board.push(best_move)
        print(f"Bot played: {best_move.uci()}")
        print("New FEN position:", board.fen())
    else:
        print("No valid moves available. Game over.")

def print_board(board):
    print("Current Board:")
    print(board)
    print("FEN position:", board.fen())

def update_board(board, move):
    board.push(move)
    print_board(board)

def user_input(board):
    while True:
        move_input = input("Your move: ").strip()
        try:
            move = chess.Move.from_uci(move_input)
            if move in board.legal_moves:
                update_board(board, move)
                break
            else:
                print("Invalid move! Please enter a legal move in UCI format.")
        except ValueError:
            print("Invalid input! Use UCI format (e.g., e2e4).")

def main():
    print("=====================================================")
    print("             Chess Bot with Minimax Algorithm        ")
    print("=====================================================")
    print("Time:", datetime.today().strftime('%Y-%m-%d %H:%M:%S'))

    player_color = input("What color would you like to play? (w=white/b=black): ").strip().lower()
    while player_color not in ['w', 'b']:
        player_color = input("Invalid input. Please enter 'w' for white or 'b' for black: ").strip().lower()

    bot_color = 'b' if player_color == 'w' else 'w'

    starting_FEN = input("Starting FEN position? (hit ENTER for standard starting position): ").strip()
    if starting_FEN:
        try:
            board = chess.Board(starting_FEN)
        except ValueError:
            print("Invalid FEN. Starting with the default position.")
            board = chess.Board()
    else:
        board = chess.Board()

    while not board.is_game_over():
        print_board(board)

        if (board.turn == chess.WHITE and player_color == 'w') or (board.turn == chess.BLACK and player_color == 'b'):
            user_input(board)
        else:
            print("Bot is thinking...")
            botMoves(board, depth=3)  

    if board.is_checkmate():
        print("Checkmate!")
    elif board.is_stalemate():
        print("Stalemate!")
    else:
        print("Game over!")

if __name__ == "__main__":
    main()
