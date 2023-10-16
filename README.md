![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Battleship Game

## Introduction

This is a Python implementation of the classic Battleship game for a player to play against an AI opponent. In this game, you'll place your ships on a game board and take turns with the AI to make shots and sink each other's ships. The game provides a user-friendly interface for both players and displays both player and AI boards.

## Table of Contents

- [Features](#features)
- [How to Play](#how-to-play)
- [Game Rules](#game-rules)

## Features

- Player vs. AI gameplay.
- Separate game boards for the player and AI.
- Reveal ship locations on the player's board.
- Independent shot counts for the player and AI.
- User-friendly interface with clear instructions.


## How to Play
- When the console is ran, you are given intructions on how to play.
- X's indicate hits 
- O's indicate where your ship location is 
-  '.' indicate free slots on the board 
- '#' indicare missed shots
- The game ends after 50 shots by either the computer or the player. If all shots are used then the player and Ai Draw

## Data model
- I used the board as my data model and attributed it the board class that generates the ai and the player board

## Testing

### Manual testing
- Through manual testing I made sure the game worked, through using invalid inputs, incorrect co-ords.
- I also passed it through a PEP8 Linter to test the validity of the code
- I did most of the testing through the console

## Bugs 
- The code has 
