# Tic-Tac-Toe Game

## Overview

This is a simple implementation of the classic Tic-Tac-Toe game in Python. The game supports two players - one human player (Player 1) and one computer player (Player 2). Player 1 plays with 'X' symbol, while Player 2 (computer) plays with 'O' symbol.

## How to Play

1. Run the Python script.
2. You will be prompted to choose 'X' or 'O' as your symbol for Player 1.
3. The computer will automatically be assigned the opposite symbol.
4. The game board will be displayed, and you can make your moves by entering the position number (1 to 9) where you want to place your symbol.

## Code Structure

The code is organized into several functions:

- `printBoard(board)`: Displays the current state of the Tic-Tac-Toe board.
- `checkPosition(position)`: Checks if the chosen position is valid for Player 1 and updates the board.
- `drawOnBoard(player, position)`: Draws the symbol for Player 1 on the board.
- `playing1()`: Handles the moves for Player 1.
- `drawOnBoardB(bot, pos)`: Draws the symbol for Player 2 (computer) on the board.
- `checkpos(pos)`: Checks if the chosen position is valid for Player 2 (computer) and updates the board.
- `botMove()`: Handles the moves for Player 2 (computer).
- `checkWhoWin(z)`: Checks and prints the winner.
- `checkForTheWinner()`: Checks for a winner after each move.
- `calculateHeuristic(board)`: Calculates the heuristic value based on the current board state.

## Playing the Game

The game consists of a loop where both players take turns until a winner is determined. Player 1 and Player 2 make their moves alternately, and the game stops when a player wins or the board is full.

Feel free to run the script and enjoy a game of Tic-Tac-Toe!
