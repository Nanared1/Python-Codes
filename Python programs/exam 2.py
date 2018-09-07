##Nana Abekah
##June 14th, 2018
##Exam 2 - Railway 
##ICS 4UO
##Mr. Veera


## First read the lines from the file
user_in = [];
with open('input.dat.txt', 'r') as file:
    for line in file:
        user_in.append(line);

## Get the max weight, num_cars, and weight of cars
max_weight = int(user_in[0]);
num_cars = int(user_in[1]); 
car_weights = [];


loop = True;

for x in range(2,len(user_in)):
    car_weights.append(int(user_in[x])) 

#first check if the first 4 cars can be on the track

begin = 0;
f = sum([int(x) for x in car_weights[:4]]); ## sum up the first 4 weights   
if(f > max_weight):
    begin = 0;
else:
    begin = 4;
    del car_weights[:1]; ## delete the first element in the car weight list if it within the max weight
    while(loop):
        f = sum([int(x) for x in car_weights[:4]]); ## sum up the the first 4 weights
        if(f < max_weight):
            begin+=1;
        else:
            loop = False;
        del car_weights[:1];
            

print(begin);

