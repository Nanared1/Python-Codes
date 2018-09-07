##Nana Abekah
##May 25th, 2018
##File Reading Test 2
##ICS 4UO
##Mr. Veera

user_in = [];
order = ['', ''];
ord_score = [0,0];
with open('input.dat.txt', 'r') as file:
    for line in file:
        user_in.append(line);
keep = [];
for element in user_in:
    keep.append(element.split(' '));
lines = str(keep[0][0]);    
lines = int(lines[:len(lines)-1]);

for x in range(1,lines+1):
    temp = keep[x][1:100];
    temp = [int(x) for x in temp];
    add = (temp[0]*2)+ temp[2] +(temp[1]*3);
    print(add);
    if(ord_score[0] < add):
        ord_score[0] = x;
    elif(ord_score[1] < add):
        ord_score[1]  = x;

with open('output.txt', 'w') as file:
    for x in ord_score:
        file.write(str(x));

    
