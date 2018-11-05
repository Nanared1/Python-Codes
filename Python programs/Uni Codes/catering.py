#Nana Abekah
#September 19, 2018
#Catering Assignment
#Comp 1001

costMeal = float(input("Please enter the cost per adult meal: "));
numAdults = float(input("Please enter the number of adults: "));
numKids = float(input("Please enter the number of children: "));
tip = float(input("Please enter the gratuity percentage: "));
deposit = float(input("Please enter the deposit amount: "));

tax = 0.15;
t_mealCost = (costMeal*numAdults)+(.5*costMeal*numKids);
t_tip = (t_mealCost*(tip/100));
t_tax = (t_mealCost*tax);
t_cost = (t_mealCost + t_tip + t_tax);
final_cost = (t_cost - deposit);

print("\nDone Right Catering Service\n");
print("%-14s"%"Meal Cost: ","$ %.2f"% t_mealCost);
print("%-14s"%"Gratuity: ","$ %.2f"% t_tip);
print("%-14s"%"Tax: ","$ %.2f"% t_tax);
print("%-14s"%"Total Cost: ","$ %.2f"% t_cost);
print("%-14s"%"Deposit: ","$ %.2f"% deposit);
print("%-14s"%"Amount Owing: ","$ %.2f"% final_cost);
