# -*- coding: utf-8 -*-
"""
Alexander Harshman
4/28/2023
Description: This class makes all playing Cards except for the Jokers. 
"""

class Card:
    """Normal Card"""
    
    def __init__(self, rank, suit):
       self.rank = rank
       self.suit = suit
      
    def getRank(self):
       return self.rank
       
    def getSuit(self):
       return self.suit
           
    def value(self):
       if self.rank in [2, 3, 4, 5, 6, 7, 8, 9, 10]:
           value = self.rank
       elif self.rank in [11, 12, 13]:
           value = 10
       else:
           value = 11
       return value
           
       
    def __str__(self):
       
       ranklist = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 
                   'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
       realrank = self.rank - 1
       rankstring = ranklist[realrank]
           
       if self.suit == "s":
           suitstring = 'Spades'
       elif self.suit == "d":
           suitstring = 'Diamonds'
       elif self.suit == "h":
           suitstring = 'Hearts'
       else:
           suitstring = 'Clubs'
       
       return rankstring + ' of  '+ suitstring
       
       
       
       