#Nana Abekah
#November 02, 2018
#Counter Assignment
#Comp 1001

import random


def pathString(slots, nBalls):
    path = [];
    for x in range(nBalls):
        p="";
        for x in range(slots-1):
            rNum = random.randint(0,10);
            LR = "R" if rNum%2 is 0 else "L";
            p += LR;
        path.append(p);
    return(path);

def sNumber(path):
    r = 0;
    for x in path:
        if(x == "R"):
            r+=1;
    return(r);


def main():
    nBalls = int(input("Enter number of Balls: "));
    nSlots = int(input("Enter number of slots: "));
    sNum = [];
    pString = pathString(nSlots, nBalls);
    for x in range(nBalls):
        sNum.append(sNumber(pString[x]));
        print("Ball ", x, "path: ", pString[x], "in slot ", sNumber(pString[x]));
main();
