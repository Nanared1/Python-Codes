#Nana Abekah
#October 15, 2018
#Day of week  Assignment
#Comp 1001

from math import *

y = int(input("Enter the 4-digit year: "));
m = int(input("Enter the month as an integer: "));
d = int(input("Enter the day as an integer: "));

y1 = y;

if((m is 1) or (m is 2)):
    y = y-2;

def getDayName(d):
    if(d is 0):
        return("Sunday");
    elif(d is 1):
        return("Monday");
    elif(d is 2):
        return("Tuesday");
    elif(d is 3):
        return("Wednesday");
    elif(d is 4):
        return("Thursday");
    elif(d is 5):
        return("Friday");
    elif(d is 6):
        return("Saturday");

def getMonthName(m):
    if(m is 1):
        return("January");
    elif(m is 2):
        return("February");
    elif(m is 3):
        return("March");
    elif(m is 4):
        return("April");
    elif(m is 5):
        return("May");
    elif(m is 6):
        return("June");
    elif(m is 7):
        return("July");
    elif(m is 8):
        return("August");
    elif(m is 9):
        return("September");
    elif(m is 10):
        return("October");
    elif(m is 11):
        return("November");
    elif(m is 12):
        return("December");

def getDayNum(y,m,d):
    p = int(str(y)[2:4]);
    q = int(str(y)[0:2]);
    r = ((m+9) % 12)+1;
    s = ((13*r)-1)/5;
    t = p/4;
    u = q/4;
    v = floor(d + p + s + t + u + (5*q));
    w = (v%7);
    return((w));

def main():
    num = getDayNum(y,m,d);
    print(getMonthName(m), " ", d, " , ", y1, " is a ", getDayName(num*1));
main();
