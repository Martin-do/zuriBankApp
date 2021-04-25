import 
def banking_operation(user):
	print("Welcome user, what would you like to do")
	operation = int(input("1. Cash Deposit	2. Cash Withdrawal	3. Complain	4. Transfer	5. Logout	6. Update your details"))
	if operation == 1:
		deposit()
	elif operation == 2:
		withdraw()
	elif operation == 3:
		complain()
	elif operation == 4:
		transfer()
	elif operation == 5:
		logout()
	elif operation == 6:
		#database.update()
		pass
	else:
		print("You have entered an incorrect input, please try again")
		banking_operation()

def deposit():
	amount = int(input("How much would you like to deposit: "))
	user[3] += amount
	#database.update(type, value)
	print("cash deposited successfully")
	print(user)
	
def withdraw():
	amount_withdraw = int(input("Enter amount you want to withdraw: "))
	user[3] -= amount_withdraw
	print("withdraw succesful")
	print(user)
	#database.update(type, value)
	
def complain():
	pass
def transfer():
	pass
def logout():
	pass
	
	
def update(type, value):
	if type == 

user = ["","","", 4]
banking_operation(user)