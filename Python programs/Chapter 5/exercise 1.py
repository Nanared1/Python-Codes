#Nana Abekah
#Exercise 1(printing)
#Feb, 07 2018
#ICS4U0-A
#Mr. Veera

_copies = int(input("Enter the number of copies to be printed: "));
if _copies >= 0 and _copies <= 99:
    print("Price Per Copy is: ${}".format(0.30));
elif _copies >= 100 and _copies <= 499:
    print("Price Per Copy is: ${}".format(0.28));
elif _copies >= 500 and _copies <= 749:
    print("Price Per Copy is: ${}".format(0.27));
elif _copies >= 750 and _copies <= 1000:
    print("Price Per Copy is: ${}".format(0.26));
else:
    print("Price Per Copy is: ${}".format(0.25));
    
