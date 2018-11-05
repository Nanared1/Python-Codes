#Nana Abekah
#October 15, 2018
#Dice Game Assignment
#Comp 1001

import math
from random import randint

def diceRoll():
    return(randint(1, 6));

def main():
    d1 = diceRoll();
    d2 = diceRoll();
    add = d1+d2;
    if((add is 2) or (add is 3) or (add is 12)):
        print("Your rolled ", d1, " + ", d2, " = ", add);
        print("You lose...");
    elif((add is 7) or (add is 11)):
        print("Your rolled ", d1, " + ", d2, " = ", add, "\nYou win!");
    else:
        point = True;
        keep = add;
        print("Your rolled ", d1, " + ", d2, " = ", add, "\nPoint value = ", add);
        while(point):
            d1 = diceRoll();
            d2 = diceRoll();
            add = d1+d2;
            if(keep is add):
                print("Your rolled ", d1, " + ", d2, " = ", add, "\nYou win!");
                point = False;
            elif(add is 7):
                print("Your rolled ", d1, " + ", d2, " = ", add, "\nYou Lose...");
                point = False;
            else:
                print("Your rolled ", d1, " + ", d2, " = ", add);

if __name__ == '__main__':
    main();
