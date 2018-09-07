##Nana Abekah
##June 14th, 2018
##Exam 1 - Euclid 
##ICS 4UO
##Mr. Veera

x = int(input("Enter a positive integer: "));
y = int(input("Enter another positive integer: "));
def gcd(x,y):
    if(y == 0):
        return(x);
    else:
        return(gcd(y,(x%y)));
print(gcd(x,y))
