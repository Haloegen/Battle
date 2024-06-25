# Battleship Game




## Table of Contents
1. [Introduction](#introduction)
2. [Core Features](#core-features)
3. [How to Play](#how-to-play)
4. [Game Rules](#game-rules)
5. [User Stories](#user-stories)
6. [Testing](#testing)
   - [Manual Testing](#manual-testing)
   - [User Story Testing](#user-story-testing)
7. [Bugs](#bugs)
8. [Future Development](#future-development)
9. [Acknowledgements](#acknowledgements)
10. [Deployment to Heroku](#deployment-to-heroku)


## Introduction 
This is a Python implementation of the classic Battleship game where the player competes against an AI opponent. Both players' ships are hidden from each other. The board is generated randomly, and players take turns shooting at the board to sink each other's ships. The game displays the boards and registers hits and misses for user-friendly functionality.

## Objective
The user should be able to play the game vs the AI, finding out the location of the ships with hits and misses, the ships should be grouped together, allowing problem solving for findind the direction and coordinates of other ships, while providing feedback when putting errors into the console.

## Data models
- I used the board as my data model and attributed it the board class that generates the ai and the player board, this allows the user to see where the ai has hit and where the player has also hit/miss.

# Built with
This game was built with python3

## Core Features
- Human vs. AI gameplay
- Classic Battleship rules
- Separate game boards for the player and AI
- Independent shot count for the player and AI
- AI with basic strategic capabilities
- User interface with clear instructions

## How to Play
- Upon running the console application, instructions on how to play are provided.
- 'X' indicates hits.
- 'O' indicates ship locations.
- '.' indicates free slots on the board.
- '#' indicates missed shots.
- The game ends after 50 shots by either the player or the AI. If all shots are used, the game results in a draw.

## Game Rules
- The player has 50 shots to sink the AI ships. If the player misses or all their ships are sunk, they lose.
- When a shot hits/misses the terminal provides feedback E.G ship hit/ shot miss.

## User Stories
1. As a player, I want to input my moves via a command-line interface to interact with the game.
2. As a player, I want error messages for incorrect coordinates.
3. As a player, I want the AI to automatically take its turn after mine to progress the game.
4. As a player, I want to see the current game board state after each turn to strategize.
5. As a player, I want to be notified when the game ends to know the outcome.
6. As a player, I don't want to input the same coordinates multiple times to avoid wasting turns.
7. As a player, I want the game to notify me when I win by destroying all AI ships.

## Testing
### Manual Testing
1. **Input Validation**:
   - Enter invalid coordinates (e.g., out of board range) and verify that the error message is displayed.
   - Status: Pass
2. **AI Move Execution**:
   - Make a move and observe if the AI immediately takes its turn.
   - Status: Pass
3. **Board State Update**:
   - Check if the board is updated correctly with 'X' for hits and '#' for misses after each move.
   - Status: Pass
4. **End Game Conditions**:
   - Play until all shots are used or all ships are sunk and verify that the game ends with the correct message.
   - Status: Pass
5. **Prevent Duplicate Moves**:
   - Attempt to fire at the same coordinates multiple times and check for error message.
   - Status: Pass
6. **Win Notification**:
   - Successfully sink all AI ships and ensure the game displays a winning message.
   - Status: Pass

### User Story Testing
1. **Command-line input for moves**:
   - Test: Enter coordinates (e.g., A1) in the terminal.
   - Status: Pass
2. **Error messages for incorrect coordinates**:
   - Test: Enter wrong coordinates to see if error message appears.
   - Status: Pass
3. **AI automatic turn**:
   - Test: Make a move and check if AI responds. Verify on player's board.
   - Status: Pass
4. **Current state of the game board**:
   - Test: Ensure hits and misses are recorded.
   - Status: Pass
5. **End game notification**:
   - Test: Finish the game by destroying ships or running out of shots.
   - Status: Pass
6. **Avoiding duplicate coordinates**:
   - Test: Enter the same coordinates multiple times and check for error.
   - Status: Pass
7. **Winning notification**:
   - Test: Destroy all AI ships and check for win message.
   - Status: Pass

## Bugs
- Fixed issues with mistyped variable names and incorrect syntax.
- individual ship segments show up as Ship hit in the terminal, and then sunk. 
-when coding all my code passes the pep8 linter, bar two lines as seen in the screen shot below
- ![pep8linter](https://res.cloudinary.com/dtajxn9oi/image/upload/v1719315138/Screenshot_64_vb4a1x.png)

## Future Development
- Implement a more sophisticated algorithm for AI guesses.
- Add a graphical user interface (GUI) for a more interactive experience.
- Allow customization of ships and game rules.

## Acknowledgements
- Inspired by the video from [Knowledge Mavens](https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=1514s).

## Deployment to Heroku

### Prerequisites
- Ensure you have a Heroku account. If not, sign up at [Heroku](https://signup.heroku.com/).
- Install the Heroku CLI from [here](https://devcenter.heroku.com/articles/heroku-cli).

### Steps

1. **Fork the Repository**:
   - Navigate to the GitHub repository for the Battleship game.
   - Click on the "Fork" button at the top-right corner of the page to create a copy of the repository under your GitHub account.

2. **Clone the Repository**:
   - Open a terminal or command prompt.
   - Clone your forked repository using the command:
     ```bash
     git clone https://github.com/Haloegen/Battle
     ```
   - Navigate to the cloned directory:
     ```bash
     cd BATTLE
     ```

3. **Create a Heroku App**:
   - Login to Heroku:
     ```bash
     heroku login
     ```
   - Create a new Heroku app:
     ```bash
     heroku create your-app-name
     ```

4. **Deploy to Heroku**:
   - Ensure you have a `Procfile` that specifies the command to run your application. For a simple Python script, it might look like this:
     ```
    web: node index.js
     ```
   - Add and commit these files if they are not already present:
     ```bash
     git add .
     git commit -m "Added Procfile"

ON the Heroku website click the new app button, select region,
select build packs, 
heroku/python
heroku/node.js
and then connect the github repository to the heroku app in the deploy tab, and then deploy from main branch.


By following these steps, you can fork the Battleship game repository, deploy it to Heroku, and run the game in a cloud environment.
