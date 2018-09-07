#Nana Abekah
#Factorial


def factorial(num):
    
    if(num == 1):
        expo = 1;
    else:
        expo = num*factorial(num - 1);

    return(expo)


number = int(input("Input a number to find factorial: "));
print("The factorial of", number, 'is', factorial(number));
    
