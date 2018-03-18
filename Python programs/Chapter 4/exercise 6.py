#Nana Abekah
#Exercise 6(change)
#Feb, 08 2018
#Mr. Veera
#ISC4U0-A

change = int(input("Enter the change in cents: "));
Quarters = change//25;
print("Quarters: ", Quarters);
Dimes = (change - (Quarters*25)) // 10;
print("Dimes: ", Dimes);
Nickles = (change - (Quarters*25) - (Dimes*10)) // 5;
print("Nickles: ", Nickles);
Pennies = (change - (Quarters*25) - (Dimes*10) - (Nickles*5));
print("Pennies: ", Pennies);
