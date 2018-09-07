##Nana Abekah
##April 9th, 2018
##Objects and Classes Test 1
##ICS 4UO
##Mr. Veera

class widget: ##Widget class to store information for different objects.
    def __init__(self, quantity):
        self.quantity = quantity;
    def show_stock(self):
        return(self.quantity);
    def remove_stock(self, amount):
        self.quantity -= amount;
    def add_stock(self, amount):
        self.quantity += amount;
    def __repr__(self):
        print("Good luck");

##display the choices.
def showChoices():
    print("1. Show current inventory");
    print("2. Add to the current inventory.");
    print("3. Decrease the current inventory.");
    print("Enter 0 to Quit.");

showChoices();
userInput = int(input('Enter your choice:'));
walmart = widget(100); ##widget object called 'walmart' has initial stock amount of 100

##Ask for user choice
while(userInput is not 0):
    if(userInput is 1):
        print('Current amount in inventory is: ', walmart.show_stock());##show amount in stock
        userInput = int(input('Enter your choice: '));
    if(userInput is 2):
        walmart.add_stock(int(input('Add stocks: '))); ##add to stock
        userInput = int(input('Enter your choice: '));
    if(userInput is 3):
        walmart.remove_stock(int(input('Remove stocks: '))); ##remove from stock
        userInput = int(input('Enter your choice: '));
