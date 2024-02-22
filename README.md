
# Battleship Game

## Introduction

This is a Python implementation of the classic Battleship game for a player to play against an AI opponent. In this game, you'll place your ships on a game board and take turns with the AI to make shots and sink each other's ships. The game provides a user-friendly interface for both players and displays both player and AI boards.

# Built with
This game was built with python3


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

## Game Rules
- The player has 50 shots to try and sink the ai ships. If he misses the ships or all his ships are sunk he loses.

  
## Data models
- I used the board as my data model and attributed it the board class that generates the ai and the player board

## Testing

### Manual testing
- Through manual testing I made sure the game worked, through using invalid inputs, incorrect co-ords.
- I did most of the testing through the console
- using manual testing, i tested the fire shot function, and ship hit function and the gameover function, through manual testing when a shot is fired and missed it is represented by a '#' and when it is hit it is represented by a 'X'.
- insuring that the project runs and can be hosted on Heroku, and are actually able to finish a game

## Bugs 
- Through testing several bugs, were found, through the mistyping of variable names.
- The incorrect syntax of code
- when a part or ship segment is hit you will see the "A ship is sunk" the code registers all segments or targets as individual ships.

## Future development
- Implement a more sophisticated algorithm for the computer's guesses.
- Add a graphical user interface (GUI) for a more interactive experience.
- Allow for more customization of ships and game rules.

## Acknowledgements
- Using this video as inspiration by [Knowledge Mavens](https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=1514s) is how i started my project.