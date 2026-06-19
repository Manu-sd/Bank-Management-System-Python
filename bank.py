from random import randint

class Bank:

    def __init__(self):
        self.account = randint(100000, 999999)
        self.full_name = input("Enter Your Name: ")
        self.phone_no = input("Enter Your Phone Number: ")
        self.balance = 0

    def show_info(self):
        print("\n-------------------------")
        print(f"Account Number : {self.account}")
        print(f"Full Name      : {self.full_name}")
        print(f"Phone Number   : {self.phone_no}")
        print(f"Balance        : ₹{self.balance}")
        print("-------------------------")

    def show_balance(self):
        print(f"Current Balance: ₹{self.balance}")

    def deposit(self):
        amount = float(input("Enter amount to deposit: ₹"))

        if amount <= 0:
            print("Invalid deposit amount!")
            return

        self.balance += amount
        print(f"₹{amount} deposited successfully.")
        self.show_balance()

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: ₹"))

        if amount <= 0:
            print("Invalid withdrawal amount!")
            return

        if amount > self.balance:
            print("Insufficient balance!")
            return

        self.balance -= amount
        print(f"₹{amount} withdrawn successfully.")
        self.show_balance()


# ---------------- MAIN PROGRAM ---------------- #

banks = []

while True:

    print("\n====== BANK MANAGEMENT SYSTEM ======")
    print("1. Create Account")
    print("2. Show All Accounts")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Check Balance")
    print("6. Search Account")
    print("7. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    # Create Account
    if choice == 1:

        account = Bank()
        banks.append(account)

        print("\nAccount Created Successfully!")
        print("Your Account Number is:", account.account)

    # Show All Accounts
    elif choice == 2:

        if not banks:
            print("No accounts found.")
        else:
            for account in banks:
                account.show_info()

    # Deposit
    elif choice == 3:

        if not banks:
            print("No accounts available.")
            continue

        acc_no = int(input("Enter Account Number: "))

        for account in banks:
            if account.account == acc_no:
                account.deposit()
                break
        else:
            print("Account not found!")

    # Withdraw
    elif choice == 4:

        if not banks:
            print("No accounts available.")
            continue

        acc_no = int(input("Enter Account Number: "))

        for account in banks:
            if account.account == acc_no:
                account.withdraw()
                break
        else:
            print("Account not found!")

    # Check Balance
    elif choice == 5:

        if not banks:
            print("No accounts available.")
            continue

        acc_no = int(input("Enter Account Number: "))

        for account in banks:
            if account.account == acc_no:
                account.show_balance()
                break
        else:
            print("Account not found!")

    # Search Account
    elif choice == 6:

        if not banks:
            print("No accounts available.")
            continue

        acc_no = int(input("Enter Account Number: "))

        for account in banks:
            if account.account == acc_no:
                account.show_info()
                break
        else:
            print("Account not found!")

    # Exit
    elif choice == 7:
        print("Thank you for using Bank Management System!")
        break

    else:
        print("Invalid choice! Please try again.")