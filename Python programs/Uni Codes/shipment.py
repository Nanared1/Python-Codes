#Nana Abekah
#October 5, 2018
#Shipment Assignment
#Comp 1001

p_shipped = int(input("How many packages are to be shipped?: "));
s_total = 0.0;

for x in range(1,p_shipped+1):
    weight = float(input("Enter Weight for package "+str(x)+": "));
    ##It is assummed that a num > 0 will be entered
    if(weight <= 2):
        s_total = s_total+(1.50 * weight);
    elif((weight > 2) and (weight <= 6)):
        s_total = s_total+(2.50 * weight);
    elif((weight > 6) and (weight <= 10)):
        s_total = s_total+(3.25 * weight);
    else:
        s_total = s_total+(4.0 * weight);

debCred = input(("How are you paying? (D)ebit or (C)redit? "));
t_total = (s_total*0.15)+s_total;

print("Your subtotal is: $%.2f" % s_total);

if(debCred == "C"):
    c_Pay = (s_total*0.02);
    s_total = t_total+c_Pay;
    print("Your total is: $%.2f" % t_total);
else:
    ##Paying Cash or Debit
    print("Your total is: $%.2f" % t_total);
