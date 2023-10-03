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

    pass


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


def ships_sunken():
    """
    """
    global position_of_ships
    global board

    pass


