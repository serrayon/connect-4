import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7

def creat_board():
    board = np.zeros((6,7))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece 

# first step to pass board and col as arguments here
def is_valid_location(board, col):
    return board[5][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r 
   # command in numpy to change the orientation of the board
   #  flips it on the x axis so the numbers will fall all the way down
def print_board(board):
    print(np.flip(board, 0))
    
board = creat_board()
print_board(board)
game_over = False
turn = 0 

while not game_over:
    # Ask for player 1 input
    if turn == 0:
        col = int(input("Player 1 make your selection (0-6): "))
        
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)
        
       
          
    # Ask for player 2 input 
    else:
        col = int(input("Player 2 make your selection (0-6): "))
        
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)
            
    print_board(board)
    
    # this alternates between player one and two  
    turn +=1
    turn = turn % 2
    