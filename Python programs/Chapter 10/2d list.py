#Nana Abekah
#March 5, 2018
#2D assignment
table = [int(x) for x in input().split()]; ## Receive input from user for dimensions of the sweeper
num_row = table[0]; ## get number of rows
num_col = table[1]; ## get number of cols
del table[:]; ## reset the table. 
for x in range(num_row): ## get '-' and '*' as a string and split it
    col = list(str(input()));  ## receives inputs and splits it
    table.append(col); ## append the cols to a final table;
index_ast = []; ## Stores index of the asterisk
def get_index_ast(): ## function to recieve index of each asterisk in the sequence
    for row_count in range(num_row):
        for col_count in range(num_col):
            if(table[row_count][col_count] is '*'):
                row_col = [row_count,col_count] ## store the 'x' and 'y' of the asterisk into a variable
                index_ast.append(row_col); ## append the 'x' and 'y' into a 2d list
get_index_ast(); ## call the function to get the asterisk.
def around(row, col): ## this function recieves '-' locations and return the number of '*' around the '-'
    add = [];  
    ad = 0;
    ## Go through all the index's and set perimeters
    for x in range(len(index_ast)):
        ## If '-' is within range, add one to it
        if((index_ast[x][0]-1) <= row and ((index_ast[x][0])+1) >= row):
            if((index_ast[x][1]-1) <= col and ((index_ast[x][1])+1) >= col):
                add.append(1);
            else:
                add.append(-1);
        else:
            add.append(-1);
    ## 
    for x in range(len(add)):
        if(add[x]>0):
            ad+=add[x];
    if(ad > 0):
        return(ad);
    else:
        return(0);
def output():
    for row_count in range(num_row):
        for col_count in range(num_col):
            if(table[row_count][col_count] is '*'):
                print('*', end = '');
            else:
                print(around(row_count, col_count), end = '');
        print();
output();
