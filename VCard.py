# -*- coding: utf-8 -*-
"""
Alexander Harshman
04/18/2023
Description: This class grabs the right card image from the folder of cards and draws
it onto the screen.
"""

from graphics import *

class vCard:
    """ Visual Card"""
    
    def __init__(self, win, center, rank, suit):
        self.win = win
        
        if rank == 1:
            rank = "ace"
        elif rank == 11:
            rank = "jack"
        elif rank == 12:
            rank = "queen"
        elif rank == 13:
            rank = "king"
        else:
            rank = str(rank)
            
        if suit == "s":
           suit = 'spades'
        elif suit == "d":
           suit = 'diamonds'
        elif suit == "h":
           suit = 'hearts'
        else:
           suit = 'clubs'
        
        
        cardFile = 'images/' + rank + "_of_" + suit + ".gif"
        self.card = Image(center, cardFile).draw(self.win)
        
    def move(self, x, y):
        self.card.move(x, y)
