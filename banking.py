# A banking program to create account deposit withdraw and check balance
user = {}
state = 1 # 1 means running 0 means exit
name = input("To create an account please write your name: ")
bankBalance = 0
user["name"] = name
user["balance"] = bankBalance

def deposit(amount):
    global bankBalance
    bankBalance += amount
    response = f"A deposit of {amount} was made your account balance is {bankBalance}"
    return response

def accountBalance():
    return f"Your account balance is {bankBalance}"

def withdraw (amount):
    global bankBalance
    if(bankBalance > amount):
        bankBalance -= amount
        return f"{amount} withdrawn your new bank balance is {bankBalance}"
    else:
        return "Cannnot withdraw your balance is low"

while (state == 1):
    action = int(input("Press 1 for your account balance \nPress 2 to deposit \nPress 3 to withdraw: "))
    if(action == 1):
        print(accountBalance())
    elif(action == 2):
        amount = int(input("How much would you like to deposit: "))
        print(deposit(amount))
    elif(action == 3):
        amount = int(input("How much would you like to withdraw: "))
        print(withdraw(amount))
    action = int(input("Press 1 to exit, Press 2 to continue: "))

    if(action == 1):
        state = 0 # Exits
        print("GoodBye !")