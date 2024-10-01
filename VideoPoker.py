# -*- coding: utf-8 -*-
"""
Alexander Harshman
4/28/2023
Description:  This Program is a graphic single player poker game.  The player
strats with five cards and can then bet as much as they have in their total. The 
player then picks which cards they what to swap.  The player then clicks the swap
button AFTER choosing the cards and the player is told what they have and rewarded
their winnings.
"""

from graphics import *
from button import Button
from CircleButton import CButton
from VCard import vCard
from DeckClass import Deck
from random import randint


def main():
    
# Making the window
    win = GraphWin('One Player Poker', 800, 500)
    win.setBackground('green')
    
# Making the spots where the cards go
    CardOutline = Rectangle(Point(127.5, 314.5), Point(672.5, 474.5))
    CardOutline.setFill('black')
    CardOutline.draw(win)
    
# Making the buttons hidden under the cards
    CB1 = Button(win, Point(184, 394.5), 103, 150, ' ', 'green')
    CB2 = Button(win, Point(292, 394.5), 103, 150, ' ', 'green')
    CB3 = Button(win, Point(400, 394.5), 103, 150, ' ', 'green')
    CB4 = Button(win, Point(508, 394.5), 103, 150, ' ', 'green')
    CB5 = Button(win, Point(616, 394.5), 103, 150, ' ', 'green')
    
    CBs = [CB1, CB2, CB3, CB4, CB5]
    
# Setting movement for cards to the hand
    dx1, dy = -524.5, 289.5
    dx2 = -416.5
    dx3 = -308.5
    dx4 = -200.5
    dx5 = -92.5
    c = 0
    
    dxs = [524.5, 416.5, 308.5, 200.5, 92.5]
    
# Making Information Buttons
    SwapButton = Button(win, Point(735, 345), 95, 40, 'Swap', 'lightgray')
    BetButton = Button(win, Point(735, 395), 95, 40, 'Bet', 'lightgray')
    HoldButton = Button(win, Point(735, 445), 95, 40, 'Hold', 'lightgray')
    
    smallChip = CButton(win, Point(65, 445), 45, '100', '#1C448E')
    medChip = CButton(win, Point(65, 345), 45, '200', '#A44A3F')
    bigChip = CButton(win, Point(65, 245), 45, '500', '#4B6858')
    biggerChip = CButton(win, Point(65, 145), 45, '1000', '#F6AE2D')
    
# The circle where the bet is shown
    betcircleoutline = Circle(Point(400, 200), 65)
    betcircleoutline.setFill('black')
    betcircleoutline.draw(win)
    
    betcirc = Circle(Point(400, 200), 50)
    betcirc.setFill('green')
    betcirc.draw(win)
    
# Calling the deck from the deck class
    deck = Deck(win)
    
# Deciding what cards you get
    back = randint(0,7)
    
    if back == 1:
        Cardback = Image(Point(708.5, 105), 'images/back.gif').draw(win)
        Header = Text(Point(400, 50), 'One Player Pokermon')
        Header.setSize(24)
        Header.setStyle('bold')
        Header.setFace('courier')
        Header.draw(win)
        
    else:
        Cardback = Image(Point(708.5, 105), 'images/yback.gif').draw(win)
        Header = Text(Point(400, 50), 'One Player Poker')
        Header.setSize(24)
        Header.setStyle('bold')
        Header.setFace('courier')
        Header.draw(win)
        
    ResultText = Text(Point(400, 100), ' ').draw(win)
    
# Setting bet and total values and text
    bet = 0
    total = 2000
    bettext = Text(Point(400, 275), 'Bet: 0').draw(win)
    totaltext = Text(Point(65, 75), 'Total: 2000').draw(win)
    
    begintext = Text(Point(400, 125), 'Click to begin').draw(win)
      
################################# Game Starts Here ###################################################
    while True:
    
        p = win.getMouse()
        
    # This allows the cards to stay on screen for longer
        if c >= 1:
            for i in range(5):
                newVHand[i].move(dxs[i], -289.5)
            
        
    # Updating Text and values
        ResultText.setText(' ')
        begintext.setText(' ')
        bet = 100
        total -= 100
        
        bettext.setText('$' + str(bet))
        totaltext.setText('Total: $' + str(total))
        
    # Shuffling the deck
        deck.shuffle(1)
            
    # Moving the first five cards in the ceck to the hand
        deck.Move(0, dx1, dy)
        deck.Move(1, dx2, dy)
        deck.Move(2, dx3, dy)
        deck.Move(3, dx4, dy)
        deck.Move(4, dx5, dy)
        
################################ Betting Faze Begins ################################################
        HoldButton.activate()
        BetButton.activate()
            
        while True:
            
        # Ends the betting faze if the hold button is clicked
            p = win.getMouse()
            ChipIdrawn = False
            if HoldButton.clicked(p):
                break

        # Activates and deactivates buttons
            if BetButton.clicked(p):
                while True:
                    
                    BetButton.deactivate()
                    smallChip.activate()
                    medChip.activate()
                    bigChip.activate()
                    biggerChip.activate()
                    
            # Making sure the player can not bet more than they have in the total
                    if total < 1000:
                        biggerChip.deactivate()
                    
                    if total < 500:
                        bigChip.deactivate()
                        
                    if total < 200:
                        medChip.deactivate()
                        
                    if total < 100:
                        smallChip.deactivate()
                        break
                                    
                    p = win.getMouse()
                    if HoldButton.clicked(p):
                        break
                    
                # Adding to the bet and substracting from the total the amount
                # that the button is worth
                    if smallChip.clicked(p):
                        bet += 100
                        total -= 100
                        bettext.setText('$' + str(bet))
                        totaltext.setText('Total: $' + str(total))
                        if not ChipIdrawn:
                            ChipI = Image(Point(400, 200), 'images/Chips.gif').draw(win)
                            ChipIdrawn = True
                        
                    elif medChip.clicked(p):
                        bet += 200
                        total -= 200
                        bettext.setText('$' + str(bet))
                        totaltext.setText('Total: $' + str(total))
                        if not ChipIdrawn:
                            ChipI = Image(Point(400, 200), 'images/Chips.gif').draw(win)
                            ChipIdrawn = True
                        
                    elif bigChip.clicked(p):
                        bet += 500
                        total -= 500
                        bettext.setText('$' + str(bet))
                        totaltext.setText('Total: $' + str(total))
                        if not ChipIdrawn:
                            ChipI = Image(Point(400, 200), 'images/Chips.gif').draw(win)
                            ChipIdrawn = True
                        
                    elif biggerChip.clicked(p):
                        bet += 1000
                        total -= 1000
                        bettext.setText('$' + str(bet))
                        totaltext.setText('Total: $' + str(total))
                        if not ChipIdrawn:
                            ChipI = Image(Point(400, 200), 'images/Chips.gif').draw(win)
                            ChipIdrawn = True
                break
                        
    # Deactivating all buttons now that are no longer needed
        smallChip.deactivate()
        medChip.deactivate()
        bigChip.deactivate()
        HoldButton.deactivate()
        BetButton.deactivate()
        
############################### Select Cards faze ####################################################################
        
    # Activating all card buttons
        for button in CBs:
            button.activate()
        
        CB1count = 0
        CB2count = 0
        CB3count = 0
        CB4count = 0
        CB5count = 0
        
        CBcountlist = [CB1count, CB2count, CB3count, CB4count, CB5count]
        
        while True:
            SwapButton.activate()
            p = win.getMouse()
            
        # Ending the Select faze if the swap button is clicked
            if SwapButton.clicked(p):
                break
            
        # Moving and keeping track of which cards the player whats to swap
            i = 0
            for button in CBs:
                
                if button.clicked(p):
                
                    CBcountlist[i] += 1
                
                    if CBcountlist[i] % 2 == 1:
                        deck.Move(i, 0, -20)
                
                    elif CBcountlist[i] % 2 == 0:
                        deck.Move(i, 0, 20)
                
                i += 1
        
    # Deactivating all card buttons
        for button in CBs:
            button.deactivate()
            
    # Setting card lists
        i = 0
        cardex = []
        newHand = []
        newVHand = []
        newCards = 0
################################## Swaping Cards ######################################################    
    
# Figuring out which cards the user wants to swap
        for i in range(5):
            
            if CBcountlist[i] % 2 == 1:
                cardex.append(i)
                newHand.append(deck.getcard(newCards + 5))
                newVHand.append(deck.getVcard(newCards + 5))
                newCards += 1
                
            else:
                newHand.append(deck.getcard(i))
                newVHand.append(deck.getVcard(i))
                
    # Making and keeping a list of the ranks and suits of the cards in the
    # user's hand
        ranks = []
        suits = []
        
    # Finding out the ranks and suits of each card
        for i in range(5):
            rank = newHand[i].getRank()
            ranks.append(rank)
            suit = newHand[i].getSuit()
            suits.append(suit)
        
        ranks.sort()
            
    # Moving and replacing selected cards
        i = 5
        for card in cardex:
            deck.Move(card, dxs[card], -269.5)
            deck.Move(i, -dxs[card], 289.5)
            i += 1
            
    # Deactivating the swap button
        SwapButton.deactivate()
        
############################ Finding Results and Payout #####################################################
    
    # Finding out if the user has a straight
        straight = True
        for i in range(4):
            if ranks[i + 1] - ranks[i] != 1 or (ranks == [1, 10, 11, 12, 13]):
                straight = False
                break
            
    # Finding out if the user has a flush
        flush = True
        for i in range(4):
            if suits[i] != suits[i + 1]:
                flush = False
                break
            
    # Finding out how many of each card is in the users hand
        counts = [0] * 14
        for value in ranks:
            counts[value] = counts[value] + 1
        
        
    # Displaying text for getting a straight
        if straight:
            returns = bet * 2
            ResultText.setText('You Have a Straight! You win $' + str(returns))
            total = total + returns
            
        # Displaying text for getting a straight flush
            if straight and flush:
                returns = bet * 3.5
                ResultText.setText('You Have a Straight Flush! You win $' + str(returns))
                total = total + returns
                
            # Displaying text for getting a straight royal flush
                if straight and flush and (ranks == [1, 10, 11, 12, 13]):
                    returns = bet * 100
                    ResultText.setText('You Have a Royal Flush! You win $' + str(returns))
                    total = total + returns
                    
    # Displaying text for getting a flush
        elif flush:
            returns = bet * 2
            ResultText.setText('You Have a Flush! You win $' + str(returns))
            total = total + returns
            
    # Displaying text for getting Four of a Kind
        elif 4 in counts:
            returns = bet * 2.5
            ResultText.setText('You Have Four of a Kind! You win $' + str(returns))
            total = total + returns
                
    # Displaying text for getting a Full House
        elif (3 in counts) and (2 in counts):
            returns = bet * 2.25
            ResultText.setText('You Have a Full House! You win $' + str(returns))
            total = total + returns
                
    # Displaying text for getting Three of a Kind
        elif 3 in counts:
            returns = bet * 1.75
            ResultText.setText('You Have Three of a Kind! You win $' + str(returns))
            total = total + returns
                        
    # Displaying text for getting Tow Pairs
        elif counts.count(2) == 2:
            returns = bet * 1.25
            ResultText.setText('You Have Two Pairs! You win $' + str(returns))
            total = total + returns
            
    # Displaying text for getting a Pair
        elif 2 in counts:
            returns = bet * .75
            ResultText.setText('You Have a Pair! You win $' + str(returns))
            total = total + returns
            
    # Displaying text for getting High Card
        else:
            returns = bet * 0
            ResultText.setText('You Have High Card! You win $' + str(returns))
            total = total + returns
            
    # Resetting variables
        totaltext.setText('$' + str(total))
        bettext.setText(' ')
        begintext.setText('Click to play again')
        c += 1
        if ChipIdrawn == True:
            ChipI.undraw()
        
            
    # Not allowing the user to play again if they don't have $100
        if total <= 99:
            break
    
    
    ResultText.setText("After " + str(c) + " hands you ran out of money. The casino wins again.")
    begintext.setText('You have been kicked out of the Casino.')

    
    time.sleep(3)
    win.close()
    
main()