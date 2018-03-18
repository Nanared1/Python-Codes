#TicTac Board
#Mr Veera
#03 Oct 2017

tt_board=[]
for row_count in range(3):
    row=[]
    for col_count in range(3):
        row.append('[ ]')
    tt_board.append(row)

print(tt_board)
space  = 9;
def display_board():
    for row_count in range(len(tt_board)):
        for col_count in range(len(tt_board[row_count])):
            print(tt_board[row_count][col_count],end='')
        print()
  
display_board();

def check_availability(row_num, column_num):
    if tt_board[row_num][column_num]=='[ ]':
        return(True);
    else:
        return(False);
    
def check_winner():


while(space >= 1):
    row_number=int(input('Enter row number (0,1,2): '))
    column_number = int(input('Enter column number (0,1,2): '))
    if(check_availability(row_number, column_number)):
        if(space%2 == 0):
            tt_board[row_number][column_number]='[x]';
        else:
            tt_board[row_number][column_number]='[O]';
        space-=1;
        display_board();
    else:
        print("The space is taken.");





