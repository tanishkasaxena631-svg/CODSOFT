# Task 2: Simple Tic-Tac-Toe Game for CODSOFT
import random

# Step 1: Create empty board
board = [' ' for _ in range(9)] # 9 empty spaces

def print_board():
    # Step 2: Show the board nicely
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_win(player):
    # Step 3: Check if player won - 3 in a row
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8], # rows
        [0,3,6], [1,4,7], [2,5,8], # columns
        [0,4,8], [2,4,6] # diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def check_tie():
    # Step 4: Check if board is full
    return ' ' not in board

def player_move():
    # Step 5: Human player = X
    while True:
        try:
            move = int(input("Enter your move 1-9: ")) - 1
            if move >= 0 and move <= 8 and board[move] == ' ':
                board[move] = 'X'
                break
            else:
                print("Invalid! Pick empty spot 1-9.")
        except:
            print("Enter a number 1-9.")

def computer_move():
    # Step 6: Computer = O, picks random empty spot
    empty_spots = [i for i in range(9) if board[i] == ' ']
    move = random.choice(empty_spots)
    board[move] = 'O'
    print(f"Computer chose spot {move + 1}")

# Step 7: Main game loop
print("=== CODSOFT Tic-Tac-Toe ===")
print("You are X, Computer is O")
print("Board positions:")
print(" 1 | 2 | 3 ")
print("---|---|---")
print(" 4 | 5 | 6 ")
print("---|---|---")
print(" 7 | 8 | 9 ")

while True:
    print_board()

    # Player turn
    player_move()
    if check_win('X'):
        print_board()
        print("You WIN! 🎉")
        break
    if check_tie():
        print_board()
        print("It's a TIE!")
        break

    # Computer turn
    computer_move()
    if check_win('O'):
        print_board()
        print("Computer WINS! 💻")
        break
    if check_tie():
        print_board()
        print("It's a TIE!")
        break

input("\nPress Enter to exit...")