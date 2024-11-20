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

def firstStep(board: chess.Board, player: str) -> chess.Move:

    if player == 'w':
        best_score = float('-inf')
    else:
        best_score = float('inf')

    best_move = chess.Move.null()  

    for player_move in board.legal_moves:
        temp_board = board.copy()
        temp_board.push(player_move)
      
        for opponent_move in temp_board.legal_moves:
            temp_board2 = temp_board.copy()
            temp_board2.push(opponent_move)
            score = evaluate_board(temp_board2)

            if player == 'w' and score > best_score:
                best_score = score
                best_move = player_move
            elif player == 'b' and score < best_score:
                best_score = score
                best_move = player_move

    return best_move

def botMoves(board: chess.Board, player: str):

    best_move = firstStep(board, player)
    if best_move != chess.Move.null():
        board.push(best_move)
        print(f"Bot played: {best_move.uci()}")
        print("New FEN position:", board.fen())
    else:
        print("No valid moves available. Game over.")

def print_board(board):
    print("Current Board:")
    print(board)
    print("FEN position:", board.fen())

def update_board(board: chess.Board, move: chess.Move):
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
    print("             CS 290 Chess Bot Version 0.1            ")
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
            botMoves(board, bot_color)

    if board.is_checkmate():
        print("Checkmate!")
    elif board.is_stalemate():
        print("Stalemate!")
    else:
        print("Game over!")

if __name__ == "__main__":
    main()
