#Nana Abekah
#September 19, 2018
#Polygon Assignment
#Comp 1001

from math import *

n = int(input("Enter the number of sides: "));
s = float(input("Enter the lenght of each side: "));
a_numerator = n*pow(s,2);
a_denom = 4*(tan(pi/n));
a = a_numerator/a_denom
print("The area of a ", n, "-sided polygon with a side length ", s," is %.2f" % a);

