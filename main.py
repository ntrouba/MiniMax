import chess
import random
from datetime import datetime

PIECE_VALUES = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.ROOK: 5,
    chess.QUEEN: 9,
    chess.KING: 1000  
}


# def minimax(board, depth:int, maximizing_player):

    # if depth == 0 or board.is_game_over():
    #     return evaluate_board(board), chess.Move.null()

    # best_move = chess.Move.null()
    # if maximizing_player:  # White's turn (maximize score)
    #     max_eval = float('-inf')
    #     for move in board.legal_moves:
    #         board.push(move)
    #         eval, _ = minimax(board, depth - 1, False)
    #         board.pop()
    #         if eval > max_eval:
    #             max_eval = eval
    #             best_move = move
    #     return max_eval, best_move
    # else:  # Black's turn (minimize score)
    #     min_eval = float('inf')
    #     for move in board.legal_moves:
    #         board.push(move)
    #         eval, _ = minimax(board, depth - 1, True)
    #         board.pop()
    #         if eval < min_eval:
    #             min_eval = eval
    #             best_move = move
    #     return min_eval, best_move


# def minimax(board, depth, maximizing_player):

#     if depth == 0: 
#         best_move = None
        
#         # if maximizing player == black find max if white find min (or maybe the other way idc)
#         # for move in board.legal_moves:
#         #     temp = board.copy() 
#         #     temp.push(move)
    
#     else: 
        



#     return best_move 


def evaluate_board(board):
    score = 0
    for square in chess.SQUARES:  
        piece = board.piece_at(square)
        print(piece)
        if piece != None:
            value = PIECE_VALUES.get(piece.piece_type, 0)
            print(value)
            if piece.color == chess.WHITE:
                score += value 
            elif piece.color == chess.BLACK: 
                score -= value 
            else:
                print("no color")
    return score

# coded for computer as white right now 
def firstStep(board:chess.Board, player:str) -> chess.Move: 

    if player == 'w':
        best_score:int = -10000 
    elif player == 'b':
        best_score:int = 10000

    best_move:chess.Move|None = None 

    for player_move in board.legal_moves:
        temp1:chess.Board = board.copy()
        temp1.push(player_move)
        for opponent_move in temp1.legal_moves: 
            temp2 = temp1.copy()
            temp2.push(opponent_move)
            s = evaluate_board(temp2)
            #print(temp2)
            #print(s)
            if s > best_score:
                print("s is better")
                best_score = s 
                best_move = player_move

    return best_move 
    
    





def botMoves(board:chess.Board):

    depth = 3

    board_copy = board.copy() 


   # _, best_move = minimax(board_copy, depth, board.turn == chess.WHITE)
    best_move = firstStep(board_copy, 'w')
    board.push(best_move)
    print(f"Bot played: {best_move.uci()}")
    print("New FEN position:", board.fen())
    print("New board:", board)
    # else:
    #     print("No valid moves available. Game over.")
        #return None 

    # player = bot_player 
    # minimax(board, 2, player)

    # player = bot_player 
    # minimax(board, 2, player)


    # generate all legal moves 
    
    #best_score = 0 
    #best_move = None 
    # for all moves in legal_moves 
        # make copy of board 
        # make move on copy 
        # for all moves available to other side after move is made 
        # score = score for white move = score for other move 
        # if score > best score 
            #best_score = score 
            # best_move = move 
    
    # return best_move 

    # capture_moves = [move for move in board.legal_moves if board.is_capture(move)]
    # if capture_moves:
    #     choice = random.choice(capture_moves)
    #     captured_peice = board.piece_type_at(choice.to_square)
    #     print("capture:", captured_peice)
    #     return choice 
    
    
    # else:
    #     return random.choice(list(board.legal_moves))

def print_board(board):
    print("Current Board:")
    print(board)
    print("FEN position:", board.fen())

def update_board(board:chess.Board, move:chess.Move): 
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

    player_color = input("What color would you like to play? (w=white/b=black): ").strip().lower()
    while player_color not in ['w', 'b']:
        player_color = input("Invalid input. Please enter 'w' for white or 'b' for black: ").strip().lower()
    
    ##TODO bot color variable 

    
    starting_FEN = input("Starting FEN position? (hit ENTER for standard starting position): ").strip()
    if starting_FEN:
        board = chess.Board(starting_FEN)
    else:
        board = chess.Board() 

    print("value of board:", evaluate_board(board))

   
    while not board.is_game_over():
        print_board(board)

        if (board.turn == chess.WHITE and player_color == 'w') or (board.turn == chess.BLACK and player_color == 'b'):
            user_input(board)
        else:
            print("Bot is thinking...")
            bot_move = botMoves(board)
            #print("bot move:", bot_move)
            #update_board(board, bot_move)
            #print(f"Bot played: {bot_move.uci()}")

    
    if board.is_checkmate():
        print("Checkmate!")
    elif board.is_stalemate():
        print("Stalemate!")
    else:
        print("Game over!")

if __name__ == "__main__":
    main()


    

main()
