def getDollarAmount(pennies, nickles, dimes, quarters):
    pennies*=0.01;
    nickles*=0.05;
    dimes*=0.1;
    quarters*=0.25;
    return(pennies + nickles + dimes + quarters);

print("Enter your total coins: \n");
quarts = int(input("Quarters: "));
dimes = int(input("Dimes: "));
nicks = int(input("Nickles: "));
pens = int(input("Pennies: "));

print("Total: $", getDollarAmount(pens, nicks, dimes, quarts));




