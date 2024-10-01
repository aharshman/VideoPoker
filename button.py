# -*- coding: utf-8 -*-
"""
Alexander Harshman
04/18/2023

Description: This class creates buttons that can be clicked, activated and deactivated
"""

from graphics import *

class Button:
    """ Button Class"""
    
    def __init__(self, win, center, width, height, label, color):
        
        w = width / 2.0
        h = height / 2.0
        
        x = center.getX()
        y = center.getY()
        
        self.xmax = x+w # Self in fornt of a variable lets it be shared with other functions
        self.xmin = x-w
        self.ymax = y+h
        self.ymin = y-h
        
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        
        self.rect = Rectangle(p1, p2)
        self.rect.setFill(color)
        self.rect.draw(win)
        
        self.label = Text(center, label)
        self.label.draw(win)
        
        self.deactivate() #Sets all buttons to off be default 
        
    def clicked(self, p): # p = the point where we clicked
       return (self.active and (self.xmin <= p.getX() <= self.xmax) and \
                               (self.ymin <= p.getY() <= self.ymax))
       
    
    def activate(self):
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True
        
        
    def deactivate(self):
        self.label.setFill('darkgray')
        self.rect.setWidth(1)
        self.active = False
        
    def getlabel(self):
        return self.label.getText()
        
    
    def Choose(self, choices):
        
        buttons = self.button
        
        for b in buttons:
            if b.getLabel() in choices:
                b.activate()
            else:
                b.deactivate()
        
        while True:
            p = self.win.getMouse()
            for b in buttons:
                if b.clicked(p):
                    return b.getLabel() 
        
        
        