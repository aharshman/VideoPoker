# -*- coding: utf-8 -*-
"""
Alexander Harshman
04/18/2023

Description: This class creates circle buttons that can be clicked, activated and deactivated
"""

from graphics import *
from math import sqrt

class CButton:
    """ Circle Button"""
    
    def __init__(self, win, center, radius, label, color):
        
        self.r = radius
        self.center = center
        
        self.centerx = center.getX()
        self.centery = center.getY()
        
        self.CircleButton = Circle(center, radius)
        self.CircleButton.setFill(color)
        self.CircleButton.setOutline('black')
        self.CircleButton.setWidth(2)
        self.CircleButton.draw(win)
        
        self.label = Text(center, label)
        self.label.draw(win)
        
        self.deactivate() #Sets all buttons to off be default 
        
    def move(self, x, y):
        self.CircleButton.move(x, y)
        
    def clicked(self, p): # p = the point where the mouse clicked
        self.distance = sqrt((((self.centerx - p.getX())**2) + (self.centery - p.getY())**2))
        return (self.active and self.distance <= self.r)
       
    
    def activate(self):
        self.label.setFill('black')
        self.active = True
        
        
    def deactivate(self):
        self.label.setFill('light grey')
        self.active = False
        
    def getlabel(self):
        return self.label.getText()