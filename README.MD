best_score = -infinity
best_move = nil
for all moves i available to white
  for all moves j available to black after making move i
    score = positive or zero score for white move i
          + negative or zero score for black move j
    if score > best_score
      // new best move !!
      best_score = score
      best_move = i

To perform a minimax search at greater depths through the tree, we recommend using recursion.  One suggested way is to implement two functions which call each other, Max() and Min().  

Max() takes a game position as input and returns the maximum score of all of the moves available to the player in that position as well as the move which resulted in that score.  It can have code similar to the "answer" pseudocode above, except that, in place of the "for all moves j available to black after making move i", Max() should have a loop that calls Min() with the game position after making a particular move.  Min() should be a "mirror" function to Max() which takes a game position and calculates the best move for the opponent.  Min should, in turn call Max(), and it should return the best opponent move and its score, which should be the minimum of the zero or negative scores of all available opponent's moves.

Your program should be able to play as both white or black.  You will be graded based on whether your program properly generates and accepts valid chess moves and FEN positions without crashing or needing to be terminated and restarted.