
"""
Smart Banking Application
Main Program
"""

from banking import (
    create_account,
    deposit_money,
    withdraw_money,
    check_balance,
    show_transactions
)

from exceptions import (
    InsufficientBalanceError,
    InvalidAmountError,
    AccountNotFoundError
)


def display_menu():
    """Display banking application menu."""

    print("\n" + "=" * 45)
    print("       SMART BANKING SYSTEM")
    print("=" * 45)

    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Transaction History")
    print("6. Exit")


while True:

    display_menu()

    try:

        choice = int(input("\nEnter your choice: "))

        if choice == 1:

            account_number = input(
                "Enter account number: "
            ).strip()

            customer_name = input(
                "Enter customer name: "
            ).strip()

            create_account(
                account_number,
                customer_name
            )

        elif choice == 2:

            account_number = input(
                "Enter account number: "
            ).strip()

            amount = float(
                input("Enter deposit amount: ")
            )

            deposit_money(account_number, amount)

        elif choice == 3:

            account_number = input(
                "Enter account number: "
            ).strip()

            amount = float(
                input("Enter withdrawal amount: ")
            )

            withdraw_money(account_number, amount)

        elif choice == 4:

            account_number = input(
                "Enter account number: "
            ).strip()

            check_balance(account_number)

        elif choice == 5:

            account_number = input(
                "Enter account number: "
            ).strip()

            show_transactions(account_number)

        elif choice == 6:

            print("Thank you for using Smart Banking!")
            break

        else:

            print("Invalid menu choice!")

    # Handle invalid numeric inputs
    except ValueError:
        print("Error: Please enter a valid number.")

    # Handle insufficient balance
    except InsufficientBalanceError as error:
        print("Transaction Error:", error)

    # Handle invalid deposit or withdrawal
    except InvalidAmountError as error:
        print("Amount Error:", error)

    # Handle missing account
    except AccountNotFoundError as error:
        print("Account Error:", error)

    # Handle unexpected type errors
    except TypeError as error:
        print("Type Error:", error)

    # Handle other unexpected errors
    except Exception as error:
        print("Unexpected Error:", error)

    # Always execute this block
    finally:
        print("\nBanking operation completed.")
