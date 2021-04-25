class Category:
    def __init__(self, name):
        self.name =  name
        self.list = []

    def deposit(self, amount, description="Nil "):
        self.list.append({"amount": amount, "description": description})
        print("Funds have been deposited into your " + self.name +  " Budget")

    def withdraw(self, amount, description="Nil "):
        if self.check_funds(amount) == True:
            self.list.append({"amount": -amount, "description": description})
        else:
            print("You do no have sufficient funds in your " + self.name +  " Budget")
            
    def get_balance(self):
        balance = 0
        for i in self.list:
            balance += i["amount"]
        return balance

        # return balance
    def check_funds(self, amount):
        if amount >= self.get_balance():
            return False
        else:
            return True
    def transfer(self, category, amount):
        self.withdraw(amount, "Transfer to "+ category.name)
        category.deposit(amount, "Transfer from "+ self.name)
        print("Funds have been transferred into your " + self.name +  " Budget")

    def display(self):      #displays activities is formatted style
        print("\n\nTransaction summary \n\n")
        print(self.name.center(35 + 9, '='))

        for i in self.list:
            amt = float(i["amount"])
            print(i["description"].ljust(35, '-') + str(amt).rjust(9))
        print("Total Balance remaining is %.2f" %self.get_balance())
        print("\t")
    def displayCurrentBalance(self):
        print("Your Current balance in your "+ self.name + " Budget is %.2f" %self.get_balance())


food = Category("Food")
clothing = Category("Clothing")
entertainment = Category("Entertainment")

food.deposit(1000, "Initial Deposit")
food.withdraw(20, "pepper")
food.displayCurrentBalance()
food.transfer(clothing, 50)

clothing.withdraw(25.55)
clothing.withdraw(100)

entertainment.deposit(5000, "party")
entertainment.withdraw(1000, "Dj")
entertainment.transfer(food, 3000)

entertainment.display()
food.display()
clothing.display()



