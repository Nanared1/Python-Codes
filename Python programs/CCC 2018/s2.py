n = int(input());
sf = [];
final = [];
row = 0;
column = 0;
sum_row = 0;
sum_column = 0;
for x in range(n):
    sf.append([int(i) for i in input().split()]);
small = sf[0][0];

print(3);





##for x in range(n):
##    for i in range(n):
##        if(small >= sf[x][i]):
##            small = sf[x][i];
##            row = x;
##            column = i;
##
##sum_row = sum(sf[row]);
##sum_column = [sum(x) for x in zip(*sf)][column];
##
##if(sum_row > sum_column):
##    if(column > 1):
##        for x in range(n,0,-1):
##            final.append([item[(column-x)] for item in sf]);
##    else:
##        for x in range(0,n):
##            final.append([item[(column-x)] for item in sf]);
##else:
##    if(row > 1):
##        for x in range(n,0,-1):
##            final.append([item[(row-x)] for item in sf])
##    else:
##        for x in range(0,n):
##            final.append([item[(row-x)] for item in sf]);
##for x in range(n):
##    final[x].sort();
##print(final);
##row is horizontal
