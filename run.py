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


def grid_and_ship_location(start_row, end_row, start_col, end_col):
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

    pass

    return valid_grid_and_location(0, 0, 0, 0)


def create_board():
    """
    Will create the board and place down ships in valid locations
    Ships will be of different sizes
    """
    global board
    global board_size
    global ship_count
    global position_of_ships

    pass

    try_placing_ships_on_board(0, 0, 0, 0)


def print_board():
    """
    Will print the grid depending on size
    """
    global alphabet
    global board

    pass


def valid_shot_placement():
    """
    Will validate if the location of the shot is valid.
    Will return row and column
    """
    global alphabet
    global board

    pass

    return 0, 0


def ships_sunken(row, col):
    """
    """
    global position_of_ships
    global board

    pass


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