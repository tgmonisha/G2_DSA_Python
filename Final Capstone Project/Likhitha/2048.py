                                              #PYTHON CODE IMPLEMENTATION ON 2048 GAME
#code:
#importing random package
import random
#function to initialize game
def initialize_board():
    board = [[0] * 4 for _ in range(4)]
    add_new_tile(board)
    add_new_tile(board)
    return board
def add_new_tile(board):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = random.choice([2, 4])
def transpose(matrix):
    #function to get the transpose of matrix means interchanging rows and columns
    return [list(row) for row in zip(*matrix)]
def merge(row):
    new_row = [0] * 4
    index = 0
    for tile in row:
        if tile != 0:
            if new_row[index] == 0:
                new_row[index] = tile
            elif new_row[index] == tile:
                new_row[index] *= 2
                index += 1
            else:
                index += 1
                new_row[index] = tile
    return new_row
def move_left(board):
    #merge the cells
    return [merge(row) for row in board]
def move_right(board):
    #to move right we reverse the matrix
    reversed_board = [row[::-1] for row in board]
    merged_board = [merge(row) for row in reversed_board]
    return [row[::-1] for row in merged_board]
def move_up(board):
    #to move up we take transpose the matrix
    transposed_board = transpose(board)
    moved_board = [merge(column) for column in transposed_board]
    return transpose(moved_board)
def move_down(board):
    for j in range(4):
        col = [board[i][j] for i in range(4) if board[i][j] != 0]
        for i in range(len(col) - 1, 0, -1):
            if col[i] == col[i - 1]:
                col[i] *= 2
                col[i - 1] = 0
        col = [tile for tile in col if tile != 0]
        col = [0] * (4 - len(col)) + col
        for i in range(4):
            board[i][j] = col[i]
    return board
def print_board(board):
    for row in board:
        print(" ".join(str(tile) if tile != 0 else '.' for tile in row))
    print()
def play_game():
    board = initialize_board()
    while True:
        print_board(board)
        move = input("Enter move (U/L/D/R): ").upper()
        if move == 'U':
            #call the move up function
            board = move_up(board)
        elif move == 'L':
            #to move left
            board = move_left(board)
        elif move == 'D':
            #to move down
            board = move_down(board)
        elif move == 'R':
            #to move right
            board = move_right(board)
        elif move == 'Q':
            #to break
            break
        else:
            print("Invalid move. Use U/L/D/R/Q.")
        add_new_tile(board)
        if is_game_over(board):
            print_board(board)
            print("Game over!")
            break
def is_game_over(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return False  
            if j < 3 and board[i][j] == board[i][j + 1]:
                return False  
            if i < 3 and board[i][j] == board[i + 1][j]:
                return False
    return True
play_game()



