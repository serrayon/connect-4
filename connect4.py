import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7

def creat_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece 

# first step to pass board and col as arguments here
def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r 
   # command in numpy to change the orientation of the board
   #  flips it on the x axis so the numbers will fall all the way down
def print_board(board):
    print(np.flip(board, 0))
    
    #manually check all the winning moves
    #and verify to see if there is a wining combo
def winning_move(board, piece):
    #check horizontal locations for win
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
            
    #vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True  
            
    # check positively sloped diagonals 
    
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
    
    # check negatively sloped diagonals      
    for c in range(COLUMN_COUNT-3):
        for r in range(3,ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True
    
    
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
            
            if winning_move(board, 1):
                print("Player 1 Winss!!! Congrats!!!")
                game_over = True
        
       
          
    # Ask for player 2 input 
    else:
        col = int(input("Player 2 make your selection (0-6): "))
        
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)
            
            if winning_move(board, 2):
                print("Player 2 Winss!!! Congrats!!!")
                game_over = True
                break
            
    print_board(board)
    
    # this alternates between player one and two  
    turn +=1
    turn = turn % 2
    