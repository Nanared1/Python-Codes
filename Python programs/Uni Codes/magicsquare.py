#Nana Abekah
#September 20, 2018
#Catering Assignment
#Comp 1001

a = int(input("Please Enter A: "));
b = int(input("Please Enter B: "));
c = int(input("Please Enter C: "));
d = int(input("Please Enter D: "));
w = int(input("Please Enter W: "));
x = int(input("Please Enter X: "));
y = int(input("Please Enter Y: "));
z = int(input("Please Enter Z: "));

print("\nThe Magic Square is:\n");

print("%10d %10d %10d %10d" %   ((a-w),(c+w+y),(b+x-y),(d-x)));
print("%10d %10d %10d %10d" %   ((d+w-z),(b),(c),(a-w+z)));
print("%10d %10d %10d %10d" %   ((c-x+z),(a),(d),(b+x-z)));
print("%10d %10d %10d %10d" %   ((b+x),(d-w-y),(a-x+y),(c+w)));
