from board import Board
from roster import Roster





class Screen:

    def __init__(self):
        self.board = Board()
        self.player_1 = roster.player1
        self.player_2 = roster.player2
       
"""
The resposibility of this class is to take 
all of the information (Names, guesses, hints, turns) from other classes 
and print it in the correct order.
"""

def print_board(self):
    self.board.to_string(self.player_1, self.player_2)

"""
calls the methods within board and prints everything to the screen
"""

    

  

