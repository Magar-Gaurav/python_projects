from accounts import SavingsAccount, CurrentAccount
from exceptions import InvalidChoiceError

def fetch_transactions():
    try:
        with open("transaction_history.txt", "r") as file:
            data = file.read()
            if not data.strip():
                print("\nNo transaction history found.")
            else:
                print("\n===== Transaction History =====")
                print(data)
    except FileNotFoundError:
        print("Transaction history file not found.")
    except Exception as e:
        print(f"Error: {e}")

def clear_transactions():
    try:
        with open("transaction_history.txt", "w") as file:
            pass
        print("\nAll transaction history has been cleared successfully.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("=" * 40)
    print(" Welcome to Banking System ")
    print("=" * 40)

    try:
        name = input("Enter Account Holder Name: ").strip().title()
        account_type = input("Enter Account Type (s = Savings, c = Current): ").strip().lower()
        balance = int(input("Enter Initial Balance: "))

        if account_type == "s":
            account = SavingsAccount(name, balance)
        elif account_type == "c":
            account = CurrentAccount(name, balance)
        else:
            raise InvalidChoiceError("Invalid account type.")
    except Exception as e:
        print(f"Error: {e}")
        return

    while True:
        print("\n========== MENU ==========")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. View Transaction History")
        print("5. Clear Transaction History")
        print("6. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                amount = int(input("Enter deposit amount: "))
                account.deposit(amount)
            elif choice == "2":
                amount = int(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            elif choice == "3":
                account.show_balance()
            elif choice == "4":
                fetch_transactions()
            elif choice == "5":
                confirm = input("Are you sure you want to clear all transaction history? (y/n): ").strip().lower()
                if confirm == "y":
                    clear_transactions()
                else:
                    print("Operation cancelled.")
            elif choice == "6":
                print("Thank you for using Banking System.")
                break
            else:
                raise InvalidChoiceError("Please enter a valid menu choice.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
