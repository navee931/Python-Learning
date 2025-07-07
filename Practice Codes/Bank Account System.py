# Create class BankAccount with attributes like name, balance, and methods: deposit(), withdraw(), display_balance().

name = input("Enter your name: ")
initial_balance = float(input("Enter initial Balance: "))
print(f"\n{name}'s Balance = {initial_balance} Rs")

class Banking:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"\n₹{amount} credit to your account")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"\n₹{amount} debited from your account")
        else:
            print("Insufficient Balance")
    
    def display(self):
        print(f"{self.name}'s Balance = {self.balance: .2f} Rs")

Acc = Banking(name, initial_balance)

while True:

    print("\nChoose an operation")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display Balance")
    print("4. Exit")
    
    choice = input("\nEnter your Choice: ")
    
    if choice == "1":
        amount = float(input("\nEnter the amount: "))
        Acc.deposit(amount)
        Acc.display()

    elif choice == "2":
        amount = float(input("\nEnter the amount: "))
        Acc.withdraw(amount)
        Acc.display()

    elif choice == "3":
        print()
        Acc.display()

    elif choice == "4":
        print("\nThank You")
        break

    else:
        print("\nInvalid Choice, Try again")   
