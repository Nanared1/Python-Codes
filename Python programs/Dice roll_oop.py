## Nana Abekah
## Dice Roll Game - ch 8#4
## Mr. Veera
## ICS 4UO
import math
from random import randint

risk = 0;
highlow = 1;
random = 0;
class dice:
    def __init__(self):
        self.points = 1000;
    def roll(self):
        if(random >= 2 and random <= 6 and highlow is 0):
            self.points += risk*2;
        elif(random >= 8 and random <= 12 and highlow is 1):
            self.points += risk*2;
        else:
            self.points -= risk;
    def showPoints(self):
        return(self.points);
    def __repr(self):
        print("");

DRplayer = dice();
print("You have ", DRplayer.showPoints(), " points.");
while(True):
    risk = int(input("How many points do you want to risk? (-1 to quit): "));
    if(risk is -1):
        break;
    highlow = int(input("Make a code (0 for low, 1 for high): "));
    random = randint(2, 12);
    DRplayer.roll();
    print("You have rolled: ", random,".");
    print("You know have ", DRplayer.showPoints(), " points.")
