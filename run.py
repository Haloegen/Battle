# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
import time
from enum import Enum


board = [[]]

ai_board = []

board_size = 10

ship_count = 8

player_shots_left = 50

ai_shots_left = 50

game_over = False

ships_sunk = 0

ai_ships_sunk = 0

ai_ship_segments = 0

position_of_ships = [[]]

alphabet = "ABCDEFGHJKLMNOPQRSTUVWXYZ"


class Directions(Enum):
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"


def board_and_ship_location(start_row, end_row, start_col, end_col):
    """
    Will check to see if the location of the ship is valid
    Returns true of false
    """
    place_valid = True
    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            if board[r][c] != ".":
                place_valid = False
                break
    if place_valid:
        position_of_ships.append([start_row, end_row, start_col, end_col])
        for r in range(start_row, end_row):
            for c in range(start_col, end_col):
                board[r][c] = "O"
    return place_valid


def place_ships_on_board(target_board, row, col, direction, length):
    """
    Try to place a ship on the given board; return True if the ship location is valid.
    """
    start_row, end_row, start_col, end_col = row, row + 1, col, col + 1
    if direction == Directions.LEFT.value:
        if col - length < 0:
            return False
        start_col = col - length + 1

    elif direction == Directions.RIGHT.value:
        if col + length >= board_size:
            return False
        end_col = col + length

    elif direction == Directions.UP.value:
        if row - length < 0:
            return False
        start_row = row - length + 1

    elif direction == Directions.DOWN.value:
        if row + length >= board_size:
            return False
        end_row = row + length

    # Check if the ship can be placed
    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            if target_board[r][c] != '.':
                return False

    # Place the ship
    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            target_board[r][c] = 'O'
    return True


def create_board():
    """
    Will create the board and place down ships in valid locations
    Ships will be of different sizes
    """
    global board
    global position_of_ships

    random.seed(time.time())

    rows, cols = (board_size, board_size)

    board = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append(".")
        board.append(row)

    num_ships_placed = 0

    position_of_ships = []

    while num_ships_placed != ship_count:
        random_row = random.randint(0, rows - 1)
        random_col = random.randint(0, cols - 1)
        direction = random.choice(["left", "right", "up", "down"])
        ship_size = random.randint(2, 6)
        if place_ships_on_board(board, random_row, random_col, direction, ship_size):
            num_ships_placed += 1


def create_ai_board():
    global ai_board, ai_ship_segments

    ai_board = [['.' for _ in range(board_size)] for _ in range(board_size)]

    num_ships_placed = 0
    while num_ships_placed < ship_count:
        random_row = random.randint(0, board_size - 1)
        random_col = random.randint(0, board_size - 1)
        direction = random.choice([Directions.LEFT.value, Directions.RIGHT.value, Directions.UP.value, Directions.DOWN.value])
        ship_size = random.randint(2, 6)
        if place_ships_on_board(ai_board, random_row, random_col, direction, ship_size):
            num_ships_placed += 1
            ai_ship_segments += ship_size  # Add the size of the ship to the total segments


def print_board(player_board, ai_board, reveal_ships=False):
    """
    Print the player's board with ships always revealed and the AI's board, 
    optionally revealing the AI's ships.
    """
    global alphabet

    # Print the player's board with ships revealed
    print("\nPlayer's Board:")
    for row in range(len(player_board)):
        print(alphabet[row], end=") ")
        for col in range(len(player_board[row])):
            print(player_board[row][col], end=" ")
        print("")

    # Print the AI's board, conditionally revealing ships
    print("\nAI's Board:")
    for row in range(len(ai_board)):
        print(alphabet[row], end=") ")
        for col in range(len(ai_board[row])):
            cell = ai_board[row][col]
            # Hide AI's ships unless reveal_ships is True
            if cell == 'O' and not reveal_ships:
                print('.', end=" ")
            else:
                print(cell, end=" ")
        print("")

    # Print the column numbers below the boards
    print("   " + ' '.join(str(i) for i in range(board_size)))


def get_revealed_board(board):
    """
    Returns a new board with all ships revealed.
    This is used for displaying the AI board with ships visible.
    """
    revealed_board = [['.' for _ in range(board_size)] for _ in range(board_size)]
    for row in range(board_size):
        for col in range(board_size):
            if board[row][col] == 'O' or board[row][col] == 'X' or board[row][col] == '#':  # Reveal ships and shots
                revealed_board[row][col] = board[row][col]
            else:
                revealed_board[row][col] = '.'  # Keep water hidden
    return revealed_board


def fire_shot(player_turn=True):
    global ships_sunk, player_shots_left, ai_shots_left, ai_ship_segments

    if player_turn:
        print("Player's turn...")
        row, col = valid_shot_placement(ai_board)
        target_board = ai_board
        player_shots_left -= 1
    else:
        print("AI's turn...")
        time.sleep(1)
        row, col = ai_generate_move()
        target_board = board
        ai_shots_left -= 1

    print("\n----------------------------")

    if target_board[row][col] == ".":
        print("Miss! No ship was hit.")
        target_board[row][col] = "#"
    elif target_board[row][col] == "O":
        print("Hit!", end=" ")
        target_board[row][col] = "X"
        if player_turn:  # Only check for sunk ships when the player hits
            ai_ship_segments -= 1  # Decrement the number of ship segments
            if validate_ships_sunken(row, col, target_board):
                print("A ship was sunk! AI ship segments remaining: " + str(ai_ship_segments))
            else:
                print("A ship was hit!")


def valid_shot_placement(target_board):
    is_valid = False
    row = -1
    col = -1
    while not is_valid:
        placement = input("Enter row (A-J) and column (0-9) such as B7: ").upper()
        if len(placement) != 2 or not placement[0].isalpha() or not placement[1].isdigit():
            print("Error: Please enter a valid row and column such as B7.")
            continue

        row_index = alphabet.find(placement[0])
        col_index = int(placement[1])

        if 0 <= row_index < board_size and 0 <= col_index < board_size:
            if target_board[row_index][col_index] in [".", "O"]:
                is_valid = True
                row, col = row_index, col_index
            else:
                print("You have already shot here, pick somewhere else.")
        else:
            print("Invalid coordinates. Please try again.")

    return row, col


def validate_ships_sunken(row, col, target_board):
    for position in position_of_ships:
        start_row, end_row, start_col, end_col = position
        if start_row <= row <= end_row and start_col <= col <= end_col:
            for r in range(start_row, end_row):
                for c in range(start_col, end_col):
                    if target_board[r][c] != "X":
                        return False
            return True
    return False


def check_game_over():
    """
    If all ships have been sunk or we run out of bullets its game over
    """
    global game_over

    if ship_count == ships_sunk:
        print("You win!")
        game_over = True
    elif player_shots_left <= 0:
        print("You lose! You ran out of shots")
        game_over = True
    elif ai_shots_left <= 0:
        print("You win, the computer lost")


def ai_generate_move():
    """
    Generate a random AI move (row, col).
    """
    while True:
        row = random.randint(0, board_size - 1)
        col = random.randint(0, board_size - 1)
        if ai_board[row][col] != "#" and ai_board[row][col] != "X":
            return row, col


def main():
    global game_over, ai_ship_segments

    # This flag controls whether AI ships are visible
    reveal_ships = True  # Change to True to reveal AI ships during debugging or learning

    create_ai_board()  # Initialize and place ships on the AI board
    create_board()  # Initialize and place ships on the player's board

    while not game_over:
        # Directly pass reveal_ships flag to print_board
        print_board(board, ai_board, reveal_ships)

        print(f"Player Shots left: {player_shots_left}")
        print(f"AI Shots left: {ai_shots_left}")

        # Player's turn
        fire_shot(player_turn=True)
        check_game_over()
        
        if ai_ship_segments <= 0:
            print("All AI ship segments have been hit! You win!")
            game_over = True
            break

        # AI's turn
        fire_shot(player_turn=False)
        check_game_over()
        if game_over:
            break

    print("Game Over!")


if __name__ == '__main__':
    main()
