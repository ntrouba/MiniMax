import chess
import random
from datetime import datetime

def botMoves(board):
    capture_moves = [move for move in board.legal_moves if board.is_capture(move)]
    if capture_moves:
        return random.choice(capture_moves)
    else:
        return random.choice(list(board.legal_moves))

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
                print("Invalid move. Please enter a legal move in UCI format.")
        except ValueError:
            print("Invalid input format. Please enter a move in UCI format (e.g., e2e4).")

def main():
    print("=====================================================")
    print("             CS 290 Chess Bot Version 0.1            ")
    print("=====================================================")
    print("Time:", datetime.today().strftime('%Y-%m-%d %H:%M:%S'))

    player_color = input("Computer Player? (w=white/b=black): ").strip().lower()
    while player_color not in ['w', 'b']:
        player_color = input("Invalid input. Please enter 'w' for white or 'b' for black: ").strip().lower()

    
    starting_FEN = input("Starting FEN position? (hit ENTER for standard starting position): ").strip()
    if starting_FEN:
        board = chess.Board(starting_FEN)
    else:
        board = chess.Board() 

   
    while not board.is_game_over():
        print_board(board)

        if (board.turn == chess.WHITE and player_color == 'w') or (board.turn == chess.BLACK and player_color == 'b'):
            user_input(board)
        else:
            print("Bot is thinking...")
            bot_move = botMoves(board)
            update_board(board, bot_move)
            print(f"Bot played: {bot_move.uci()}")

    
    if board.is_checkmate():
        print("Checkmate!")
    elif board.is_stalemate():
        print("Stalemate!")
    else:
        print("Game over!")

if __name__ == "__main__":
    main()


    

main()