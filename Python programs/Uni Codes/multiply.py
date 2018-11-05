#Nana Abekah
#October 5, 2018
#Multiply Assignment
#Comp 1001

a = int(input("Enter first value to multiply: "));
b = int(input("Enter second value to multiply: "));
product = 0;
while(b >= 1):
    if(b%2 == 0):
        print("%7s %7s" %(a,b),"(ignore)");
    else:
        print("%7s %7s" %(a,b),"(keep)");
        product = product+a;
    a = (a*2);
    b = (b // 2);

print("Product: ", product);
