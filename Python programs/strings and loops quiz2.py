#Nana Abekah
#Strings and Loops Quiz
#February 15, 2017
#Mr. Veera
#ICS 4U0


lower_limit = int(input("Enter lower limit of range: "));
upper_limit = int(input("Enter upper limit of range: "));
count = 1;
acc = 0
for x in range(lower_limit, upper_limit+1):
    for i in range(1,x):
        if((x % i) == 0):
            count+=1;
    if(count == 4):
    
