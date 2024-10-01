# -*- coding: utf-8 -*-
"""
Alexander Harshman
04/18/2023

Description: This class makes and can shuffle a deck of the card objects from the Cards class
"""

from VCard import vCard
from Cards import Card
from random import randint
from graphics import *

class Deck:
    """Normal Deck"""
    
    def __init__(self, win):
        
        self.suits = ['s', 'h', 'c', 'd']
        
        self.deck = []
        self.iDeck = []
        self.newdeck = []
        self.newideck = []
        
        for i in range(1, 14):
            
            for suit in self.suits:
                
                card = (Card(i, suit))
                self.deck.append(card)
                
                iCard = (vCard(win, Point(708.5, 105), i, suit))
                self.iDeck.append(iCard)
                
        
        
    def getdeck(self):
        
        return self.deck
    
    def getcard(self, i):
        
        return self.deck[i]
    
    def getVcard(self, i):
        return self.iDeck[i]
        
    def shuffle(self, n):
        
        for t in range(n):
            
            for c in range(52):
                
                index = randint(0, len(self.deck) - 1)
                    
                self.newdeck.append(self.deck[index])
                self.newideck.append(self.iDeck[index])
                
                self.deck.pop(index)
                self.iDeck.pop(index)
                
            for i in range(52):
                self.deck.append(self.newdeck[i])
                self.iDeck.append(self.newideck[i])
            
            self.newdeck = []
            self.newideck = []

    def Move(self, i, x, y):
        self.iDeck[i].move(x, y)
            
            
            
            
            
            
            
            