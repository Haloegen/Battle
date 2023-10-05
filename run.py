# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
import time

board = [[]]

board_size = 10

ship_count = 8

shots_left = 50

game_over = False 

ships_sunk = 0

position_of_ships = [[]]

alphabet = "ABCDEFGHJKLMNOPQRSTUVWXYZ"


def board_and_ship_location(start_row, end_row, start_col, end_col):
    """
    Will check to see if the location of the ship is valid
    Returns true of false
    """
    global board
    global position_of_ships

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


def place_ships_on_board(row, col, direction, length):
    """
    Will try and place a ship will return true or false if ship location is
    invalid
    """
    global board_size

    start_row, end_row, start_col, end_col = row, row+1, col, col+1
    if direction == "left":
        if col - length < 0:
            return False
        start_col = col - length + 1
    
    elif direction == "right":
        if col + length >= board_size:
            return False
        end_col = col + length
    
    elif direction == "up":
        if row - length < 0:
            return False
        start_row = row - length + 1
    
    elif direction == "down":
        if row + length >= board_size:
            return False
            end_row = row + length

    return board_and_ship_location(start_row, end_row, start_col, end_col)


def create_board():
    """
    Will create the board and place down ships in valid locations
    Ships will be of different sizes
    """
    global board
    global board_size
    global ship_count
    global position_of_ships

    random.seed(time.time())

    rows, cols = (board_size, board_size)

    board = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(".")
        board.append(row)
        
    num_ships_placed = 0
    
    position_of_ships = []

    while num_ships_placed != ship_count:
        random_row = random.randint(0, rows - 1)
        random_col = random.randint(0, cols - 1)
        direction = random.choice(["left", "right", "up", "down"])
        ship_size = random.randint(2, 6)
        if place_ships_on_board(random_row, random_col, direction, ship_size):
            num_ships_placed += 1


def print_board():
    """
    Will print the grid depending on size
    """
    global board
    global alphabet

    debug_mode = True

    alphabet = alphabet[0: len(board)+1]

    for row in range(len(board)):
        print(alphabet[row], end=") ")
        for col in range(len(board[row])):
            if board[row][col] == "O":
                if debug_mode:
                    print("O", end=" ")
                else:
                    print(".", end=" ")
            else:
                print(board[row][col], end=" ")
        print("")

    print("  ", end=" ")
    for i in range(len(board[0])):
        print(str(i), end=" ")
    print("")


def valid_shot_placement():
    """
    Will validate if the location of the shot is valid.
    Will return row and column
    """
    global alphabet
    global board

    Error = print("Error: Please enter only one row and column such as b7")

    is_valid = False
    row = -1
    col = -1
    while is_valid is False:
        placement = input("Enter row (A-J) and column (0-9) such as b7: ")
        placement = placement.upper()
        if len(placement) <= 0 or len(placement) > 2:
            print("Error: Please enter only one row and column such as b7")
            continue
        row = placement[0]
        col = placement[1]
        if not row.isalpha() or not col.isnumeric():
            print(Error)
            continue
        row = alphabet.find(row)
        if not (-1 < row < board_size):
            print("Error: please enter letter (A-J) for row and (0-9) for col")
            continue
        col = int(col)
        if not (-1 < col < board_size):
            print("Error: Please enter letter (A-J) for row and (0-9) for col")
            continue
        if board[row][col] == "#" or board[row][col] == "X":
            print("You have already shot here, pick somewhere else")
            continue
        if board[row][col] == "." or board[row][col] == "O":
            is_valid = True

    return row, col


def validate_ships_sunken(row, col):
    """
    If all parts of the ship have been hit the ship will be sunk
    """
    global position_of_ships
    global board

    for position in position_of_ships:
        start_row = position[0]
        end_row = position[1]
        start_col = position[2]
        end_col = position[3]
        if start_row <= row <= end_row and start_col <= col <= end_col:
            # ship found, needs to validate if its been sunk
            for r in range(start_row, end_row):
                for c in range(start_col, end_col):
                    if board[r][c] != "X":
                        return False
        return True


def fire_shot():
    """
    """

    global board
    global ships_sunk
    global shots_left

    row, col = valid_shot_placement()

    pass


def check_game_over():
    """
    """
    global ships_sunk
    global ship_count
    global shots_left
    global game_over

    pass


def main():
    """
    """
    global game_over

    pass


if __name__ == '__main__':
    """
    """
    main()