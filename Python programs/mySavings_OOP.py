##Nana Abekah
##April 4th, 2018

class piggyBank:
    def __init__(self):
        self.total = 0;
    def addPenny(self, money):
        self.total += money
    def addNickel(self, money):
        self.total += money
    def addDime(self, money):
        self.total += money
    def addQuarter(self, money):
        self.total += money;
    def showTotal(self):
        return(self.total);
    def removeMoney(self, amount):
        self.total -= amount;
    def __repr__(self):
        return(self.total);


print('1.    Show total in bank');
print('2.    Add Penny');
print('3.    Add Nickel');
print('4.    Add Dime');
print('5.    Add Quarter');
print('6.    Take money out');
print('Enter 0 to quit');

userInput = int(input('Enter Choice: '));
mySavings = piggyBank();

while(userInput is not 0):
    if(userInput is 1):
        print('Total money in bank is: $', mySavings.showTotal());
        userInput = int(input('Enter Choice: '));
    if(userInput is 2):
        penny = int(input('Penny: '))
        mySavings.addPenny(penny*0.01);
        userInput = int(input('Enter Choice: '));
    if(userInput is 3):
        nickel = int(input('Nickel: '))
        mySavings.addNickel(nickel*0.05);
        userInput = int(input('Enter Choice: '));
    if(userInput is 4):
        dime = int(input('Dime: '))
        mySavings.addDime(dime*0.1);
        userInput = int(input('Enter Choice: '));
    if(userInput is 5):
        quarter = int(input('Quarter: '))
        mySavings.addQuarter(quarter*0.25);
        userInput = int(input('Enter Choice: '));
    if(userInput is 6):
        remove = int(input("Remove: "));
        mySavings.removeMoney(remove);
        userInput = int(input('Enter Choice: '));
