##Nana Abekah
##May 25th, 2018
##File Reading Test 1
##ICS 4UO
##Mr. Veera

## My idea is to make a string to record all the words in the file
## this will make it easier to split the words into letters
## also, I will make all the words lower case to make things easier.


sx = '';
s = 0;
t = 0;

with open('sX.txt', 'r') as file:
    for line in file:
        sx += line.lower();
        
sx = list(sx); ## This will split all the elements of the strings into individual elements
## this loop accumulates the  number of 's' and 't'

for i in sx:
    if(i == 's'):
        s+=1;
    elif(i == 't'):
        t+=1;
## Compare the numbers and output the answer.
if(t > s):
    print('English');
elif(t < s):
    print('French');
else:
    print('French');
