
# Bank Management System

accounts = {}

def create_account():
    name = input("Enter account holder name: ")
    account_number = input("Enter account number: ")
    balance = float(input("Enter opening balance: "))

    accounts[account_number] = {
        "name": name,
        "balance": balance
    }

    print("Account created successfully!")

def view_accounts():
    if len(accounts)== 0:
        print("No accounts found.")
    else:
        for account_number, details in accounts.items():
            print("\nAccount Number:", account_number)
            print("Account Holder:", details["name"])
            print("Balance: ₹", details["balance"])

while True:
    print("\n===== BANK MANAGEMENT SYSTEM =====")
    print("1. Create Account")
    print("2. View All Accounts")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_account()

    elif choice == "2":
        view_accounts()

    elif choice == "3":
        print("Thank you for using our Bank System!")
        break

    else:
        print("Invalid choice. Please try again.")
