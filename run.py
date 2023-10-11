# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
import time

board = [[]]

ai_board = []

board_size = 10

ship_count = 8

player_shots_left = 50

ai_shots_left = 50

game_over = False

ships_sunk = 0

position_of_ships = [[]]

alphabet = "ABCDEFGHJKLMNOPQRSTUVWXYZ"


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


def place_ships_on_board(row, col, direction, length):
    """
    Will try and place a ship will return true or false if ship location is
    invalid
    """

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
        if place_ships_on_board(random_row, random_col, direction, ship_size):
            num_ships_placed += 1


def create_ai_board():
    """
    Create a separate board for the AI.
    """
    global ai_board

    ai_board = [['.' for _ in range(board_size)] for _ in range(board_size)]


def print_board(player_board, ai_board, reveal_ships=False):
    """
    Print the player's board with ship locations and the AI's board
    with hits and misses.
    """
    global alphabet

    alphabet = alphabet[0: len(player_board) + 1]

    print("Player's Board:")
    for row in range(len(player_board)):
        print(alphabet[row], end=") ")
        for col in range(len(player_board[row])):
            if player_board[row][col] == "O" and not reveal_ships:
                print(".", end=" ")
            else:
                print(player_board[row][col], end=" ")
        print("")

    print("\nAI's Board:")
    for row in range(len(ai_board)):
        print(alphabet[row], end=") ")
        for col in range(len(ai_board[row])):
            print(ai_board[row][col], end=" ")
        print("")

    print("\n  ", end=" ")
    for i in range(len(player_board[0])):
        print(str(i), end=" ")
    print("")


def fire_shot(player_turn=True):
    """
    Perform a shot, either by the player or AI.
    """
    global ships_sunk
    global player_shots_left
    global ai_shots_left

    if player_turn:
        row, col = valid_shot_placement()
        target_board = ai_board
    else:
        print("AI's turn...")
        time.sleep(1)
        row, col = ai_generate_move()
        target_board = board

    print("\n----------------------------")

    if target_board[row][col] == ".":
        print("Miss!, no ship was hurt")
        target_board[row][col] = "#"
    elif target_board[row][col] == "O":
        print("Hit!", end=" ")
        target_board[row][col] = "X"
        if validate_ships_sunken(row, col):
            print("A ship was sunk")
            ships_sunk += 1
        else:
            print("A ship was hit!")

    player_shots_left -= 1
    
    ai_shots_left -= 1


def valid_shot_placement():
    """
    Will validate if the location of the shot is valid.
    Will return row and column
    """
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
            print(("Error: Please enter only one row and column such as b7"))
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
        row = random.choice(alphabet)
        col = random.randint(0, board_size - 1)
        row_index = alphabet.find(row)
        if (row_index != -1 and
            board[row_index][col] != "#" and
                board[row_index][col] != "X"):
            return row_index, col


def main():
    """
    Main game loop for Player vs AI.
    """
    global game_over

    create_ai_board()  # Create the AI's board
    create_board()  # Create the player's board

    while not game_over:
        print_board(board, ai_board, reveal_ships=True)
        print(f"Player Shots left: {player_shots_left}")
        print(f"AI Shots left: {ai_shots_left}")
        # Player's turn
        fire_shot(player_turn=True)
        if ships_sunk == ship_count or player_shots_left == 0:
            game_over = True
            break

        # AI's turn
        fire_shot(player_turn=False)
        if ships_sunk == ship_count or ai_shots_left == 0:
            game_over = True

    print("Game Over!")


if __name__ == '__main__':
    main()
