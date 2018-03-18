num_integers = int(input("What is the count: ")); ## receive number of inputs from the boss
total = []; ##store inputs from the boss!
boss_num = 0; ##Receive input from boss to store in list
final = 0; ## accumulate all the numbers from the boss.
while(num_integers > 0): ## Loop for number of inputs from boss
    boss_num = int(input("What does the boss say: "));## Receive inputs from boss
    if(boss_num == 0):## check to see if the boss said "zero"
        total.pop();##if the boss said "zero", remove the last element in the list.
    else:
        total.append(boss_num);##if the boss did not say "zero", add the number to the list.
    num_integers-=1; ##decrement counter for the while loop.

##Add up all the integers in the list
for x in range(len(total)):
    final += total[x];

print("The total is:", final); ##Print out final number. 
