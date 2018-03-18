import math
from random import randint

##First display the board
##Randomize the the prizes.

##Board dsipaly

pp_board = [];

for row_count in range(5):
    row = [];
    for col_count in range(5):
        row.append('[         ]');
    pp_board.append(row);
##print(pp_board);

def display_board():
    for row_count in range(len(pp_board)):
        for col_count in range(len(pp_board[row_count])):
            print(pp_board[row_count][col_count], end = '');
        print();
        
display_board();
