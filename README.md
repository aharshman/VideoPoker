# One Player Poker Game

This is a graphical, single-player poker game implemented using Python. The player starts with five cards and has the ability to place bets, swap cards, and win based on the final hand. The game provides a user-friendly interface to bet, swap cards, and see the outcome of each hand.

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Getting Started](#getting-started)
- [Dependencies](#dependencies)
- [How to Play](#how-to-play)
- [Folder Structure](#folder-structure)
- [Credits](#credits)

## Description
The game is a single-player poker game where the player begins with a total of $2000 in chips. The player can:
1. Place a bet.
2. Swap selected cards.
3. Hold cards to determine the final hand.
4. Win or lose based on the resulting hand.

The player can continue playing as long as they have at least $100 to bet.

## Features
- Graphical user interface (GUI) with a card display.
- Bet chips in different denominations.
- Swap or hold cards to form the best possible hand.
- Display hand results and update player balance.

## Getting Started
1. Clone this repository to your local machine.
2. Make sure all dependencies are installed.
3. Run the `app.py` file to start the game.

### Running the Game
'''bash
python app.py

## Dependencies
1. Python 3.x
2. graphics.py: A graphics library for Python. Make sure to have it in your project directory.
3. Additional custom classes (Button, CButton, VCard, Deck) should also be in the project directory.

## How to Play
1. Start the Game: Run app.py to start the game. The main window will open, displaying the cards and buttons for betting, holding, and swapping.
2. Placing a Bet: Click on one of the chip buttons to bet an amount. The available chips are $100, $200, $500, and $1000.
3. Hold or Bet: After placing a bet, you can click on the Hold button to stop betting or continue to add more.
4. Swap Cards: Click on the cards you wish to swap, and then press the Swap button to get new cards.
5. Winning or Losing: The game will calculate the hand result and update your total amount. You can continue playing until your total falls below $100.
6. Ending the Game: If your total reaches $0, you will be kicked out of the casino, and the game will end.

## Folder Structure
One_Player_Poker_Game/
│
├── app.py
├── graphics.py
├── button.py
├── CircleButton.py
├── VCard.py
├── DeckClass.py
└── images/
    ├── back.gif
    ├── yback.gif
    ├── Chips.gif
    └── (Other card images)

## Credits
1. Author: Alexander Harshman
2. Date: 12/10/2021
