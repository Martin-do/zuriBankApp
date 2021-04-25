import time, datetime, random, sys
import database
import validation
from getpass import getpass

def main():

    print("Welcome to My Bank!!!")

    haveaccount()

def haveaccount():

    response = int(input("Do you have an account with us? \n 1. Yes      2. No \n===    "))

    if response == 1:

        login()

    elif response == 2:

        register()


def register():
    first_name = input("What is your first name: ")
    last_name = input("What is your last name: ")
    email = input("Enter your email address: ")
    password1 = getpass("Enter a new password: ")
    password2 = getpss("Enter a new password again:")
    if password1 == password2:

        account_number = generateaccount()
    
        user_details = [account_number, first_name, last_name, email, password1, 0]
    
        database.create(account_number, user_details)
    
        if database.does_account_number_exist(account_number) == True:
            print("****Account Successfully register!!!****")
            print("This is your account number %d" %account_number) 
            print("******Login to your account******")
            login()
    
        else:
    
            print("Please try again")
            register()
    else:
        print("Password does not match")
    


def login():
    print("====== Login Page ======")
    account_number_from_user = input("What is your account number? \n")
    password = getpass("What is your password \n")

    if validation.is_account_number_valid(account_number_from_user) == True:

        user = database.authenticated_user(account_number_from_user, password)
    
        if user:
    
            print("!!! Welcome %s %s, what would you like to do !!!" %(user[1], user[2]))
    
            banking_operation(user)
    

    print('** Invalid account or password **')
    
    login()



def generateaccount():
    return random.randrange(1111111111, 9999999999)



def banking_operation(user):
    print("What would you like to do?")
    operation = int(input("1. Cash Deposit     2. Cash Withdrawal     3. Complain\n4. Transfer     5. Logout     6. Update your details     7. Check Balance     8. Exit\n==== "))
    if operation == 1:
        deposit(user)
    
    elif operation == 2:
        withdraw(user)
        
    elif operation == 3:
        complain()
        
    elif operation == 4:
        transfer(user)
        
    elif operation == 5:
        logout(user)

    elif operation == 6:
        update(user)

    elif operation == 7:
        print("Your balance is %s" %check_balance(user))
        print("="*30)
        banking_operation(user)

    elif operation == 8:
        print("Thank you for banking with us, Good Bye")
        sys.exit()
        
    else:
        print("You have entered an incorrect input, please try again")
        banking_operation(user)



def deposit(user):

    amount = int(input("Enter the amount you want to deposit: "))

    try:

        user[5] = int(user[5]) + amount

        database.update(user[0], "deposit", user[5])

        print("====== Cash Deposit successful ======")
        print("="*30)

        banking_operation(user)

    except ValueError:

        print("** Invalid Input **")

        deposit(user)



def withdraw(user):

    amount = int(input("Enter the amount you want to withdraw: "))

    try:
        if int(check_balance(user)) >= amount:
            user[5] = int(user[5]) - amount
        else:
            print("You do not have sufficient Funds")

        database.update(user[0], "withdraw", user[5])

        print("====== Cash Withdraw successful ======")
        print("="*30)

        banking_operation(user)

    except ValueError:

        print("** Invalid Input **")

        withdraw(user)

def complain():

    complain = input("What is your complain: ")

def transfer(user):
    #check if enough funds
    destination = int(input("Enter the account number you want to transfer to: "))

    amount = int(input("Enter the amount you want to transfer: "))
    if int(check_balance(user)) >= amount:
        user[5] = int(user[5]) - amount
    else:
        print("You do not have sufficient Funds")

    if database.does_account_number_exist(destination) == True:

        try:
            database.update(user[0], "withdraw", user[5])
            database.update(destination, "transfer", amount)

            print("====== Transfer successful ======")
            print("="*30)

            banking_operation(user)

        except ValueError:

            print("** Invalid Input **")

            withdraw(user)

    else:

        print("** Sorry, account not found **")

        banking_operation(user)


def update(user):
    update_data = int(input("What information would you like to update?\n 1. First name     2. Last name     3. Email     4. Password\n=== "))
    
    if update_data == 1:
        new_first_name = input("Enter your First name: ")
        database.update(user[0], "firstname", new_first_name)
        print("Information Updated Successfully")
        print("="*30)
        banking_operation(user)
    
    elif update_data == 2:
        new_last_name = input("Enter your last name: ")
        database.update(user[0], "lastname", new_last_name)
        print("Information Updated Successfully")
        print("="*30)
        banking_operation(user)
    
    elif update_data == 3:
        new_email = input("Enter your email: ")
        database.update(user[0], "email", new_email)
        print("Information Updated Successfully")
        print("="*30)
        banking_operation(user)
    
    elif update_data == 4:
        new_password1 = getpass("Enter a new password: ")
        new_password2 = getpass("Enter a new password again:")
        if new_password1 == new_password2:
            database.update(user[0], "password", new_password1)
            print("Information Updated Successfully")
            print("="*30)
            banking_operation(user)
        else:
            print("Password does not match")
            banking_operation(user)
    else:
        print("** Invalid Input **")
        print("="*30)
        banking_operation(user)


def check_balance(user):
    return user[5]
    
def logout(user):
    print("** Logout successful **")
    login(user)



main()