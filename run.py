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
    start_row, end_row = row, row + 1
    start_col, end_col = col, col + 1

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

    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            if target_board[r][c] != '.':
                return False

    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            target_board[r][c] = 'O'
    return True


def create_board():
    global board, position_of_ships

    board = [["." for _ in range(board_size)] for _ in range(board_size)]
    num_ships_placed = 0

    while num_ships_placed != ship_count:
        rand_row = random.randint(0, board_size - 1)
        rand_col = random.randint(0, board_size - 1)
        direction = random.choice(["left", "right", "up", "down"])
        ship_size = random.randint(2, 6)

        if place_ships_on_board(board, rand_row, rand_col, direction, ship_size):
            num_ships_placed += 1


def create_ai_board():
    global ai_board, ai_ship_segments

    ai_board = [['.' for _ in range(board_size)] for _ in range(board_size)]
    num_ships_placed = 0

    while num_ships_placed < ship_count:
        rand_row = random.randint(0, board_size - 1)
        rand_col = random.randint(0, board_size - 1)
        direction = random.choice([
            Directions.LEFT.value, Directions.RIGHT.value,
            Directions.UP.value, Directions.DOWN.value])
        ship_size = random.randint(2, 6)

        if place_ships_on_board(ai_board, rand_row, rand_col, direction, ship_size):
            num_ships_placed += 1
            ai_ship_segments += ship_size


def print_board(player_board, ai_board, reveal_ships=False):
    print("\nPlayer's Board:")
    for row in range(len(player_board)):
        print(f"{alphabet[row]}) ", end="")
        print(" ".join(player_board[row]))
    print("\nAI's Board:")
    for row in range(len(ai_board)):
        print(f"{alphabet[row]}) ", end="")
        for col in range(len(ai_board[row])):
            cell = ai_board[row][col]
            print('.' if cell == 'O' and not reveal_ships else cell, end=" ")
        print("")
    print("   " + " ".join(str(i) for i in range(board_size)))

def get_revealed_board(board):
    """
    Returns a new board with all ships ('O'), hits ('X'), and misses ('#') revealed,
    while keeping empty water cells ('.') as is.
    """
    revealed_board = [['.' for _ in range(board_size)] for _ in range(board_size)]
    for row in range(board_size):
        for col in range(board_size):
            cell = board[row][col]
            if cell in ['O', 'X', '#']: 
                revealed_board[row][col] = cell
            else:  
                revealed_board[row][col] = '.'
    return revealed_board


def fire_shot(player_turn=True):
    global ships_sunk, player_shots_left, ai_shots_left, ai_ship_segments

    row, col = (-1, -1)
    if player_turn:
        print("Player's turn...")
        row, col = valid_shot_placement(ai_board)
        player_shots_left -= 1
    else:
        print("AI's turn...")
        time.sleep(1)
        row, col = ai_generate_move()
        ai_shots_left -= 1

    print("\n----------------------------")

    target_board = ai_board if player_turn else board
    cell = target_board[row][col]
    if cell == ".":
        print("Miss! No ship was hit.")
        target_board[row][col] = "#"
    elif cell == "O":
        print("Hit!", end=" ")
        target_board[row][col] = "X"
        if player_turn:
            ai_ship_segments -= 1
            print(" A ship was hit!")
            if validate_ships_sunken(row, col, ai_board):
                print(" A ship was sunk!")
                ships_sunk += 1


def valid_shot_placement(target_board):
    is_valid = False
    while not is_valid:
        placement = input("Enter row (A-J) and column (0-9) such as B7: ").upper()
        if len(placement) == 2 and placement[0] in alphabet[:board_size] and placement[1].isdigit():
            row = alphabet.find(placement[0])
            col = int(placement[1])
            if 0 <= col < board_size and target_board[row][col] not in ["#", "X"]:
                return row, col
            else:
                print("You have already shot here, pick somewhere else.")
        else:
            print("Invalid coordinates. Please try again.")


def validate_ships_sunken(row, col, target_board):

    return target_board[row][col] == "X"


def check_game_over():
    global game_over, ai_ship_segments

    if ai_ship_segments <= 0:
        print("All AI ships have been sunk! You win!")
        game_over = True
    elif player_shots_left <= 0:
        print("You've run out of shots! Game over!")
        game_over = True
    elif ai_shots_left <= 0:
        print("AI has run out of shots! You win!")
        game_over = True


def ai_generate_move():
    while True:
        row = random.randint(0, board_size - 1)
        col = random.randint(0, board_size - 1)
        if board[row][col] not in ["#", "X"]:
            return row, col


def main():
    global game_over

    reveal_ships = False  # Change to True to reveal AI ships for debugging

    create_ai_board()
    create_board()

    while not game_over:
        print_board(board, ai_board, reveal_ships)
        print(f"Player Shots left: {player_shots_left}")
        print(f"AI Ship segments remaining: {ai_ship_segments}")

        fire_shot(player_turn=True)
        check_game_over()
        if game_over:
            break

        fire_shot(player_turn=False)
        check_game_over()
        if game_over:
            break

    print("Game Over!")


if __name__ == '__main__':
    main()
