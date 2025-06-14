from datetime import datetime

class BankAccount:

    def __init__(self,account_holder,balance=0):
        self.account_holder=account_holder
        self.balance=balance

    def deposit(self,balance): 
        self.balance+=balance
        print("Successfully Deposited!💵")
        with open("transaction.txt","a") as f:
            f.write(f"[{datetime.now()}] Deposited {balance}$\n")
            

    def withdraw(self,balance):
        withdrawed_balance=balance
        if(withdrawed_balance<=self.balance):
            self.balance-=balance
            with open("transaction.txt","a") as f:
                f.write(f"[{datetime.now()}] Withdrawed {balance}$\n")
            print("Successfully Withdrawn!📩")
        else:
            print("Insufficient balance")

    def checkbalance(self):
        print(f"Your current balance is {self.balance}$")

    @staticmethod
    def showtransaction():
        with open("transaction.txt","r") as f:
            print(f.read())

name=input("Please enter your name: ")
b1=BankAccount(name,balance=0)

while True:
    print(f"\nWelcome {name} to ABC Bank! What would you like to do?😊\n1.Deposit\n2.Withdraw\n3.Check Balance \n4.View transactions")
    choice=input("\nEnter your choice(type 'exit' to close): ").lower()
    match(choice):

        case "1":
            money=int(input("Enter the amount you would like to deposit: "))
            b1.deposit(money)
        
        case "2":
            money=int(input("Enter the amount you would like to withdraw: "))
            b1.withdraw(money)

        case "3":
            b1.checkbalance()

        case "4":
            b1.showtransaction()

        case "exit":
            break

        case _:
            print("Invalid choice! Please pick again.")
    
    