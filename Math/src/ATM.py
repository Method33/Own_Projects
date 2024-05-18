class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print("Your current balance is:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Successfully deposited", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Successfully withdrew", amount)
        else:
            print("Insufficient funds in the account")

def ATM():
    account = BankAccount(500)  # Example initial balance

    while True:
        print("1. Check balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Exit")
        choice = int(input("Choose an option: "))

        if choice == 1:
            account.check_balance()
        elif choice == 2:
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == 3:
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == 4:
            print("Thank you for using our services!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    ATM()
