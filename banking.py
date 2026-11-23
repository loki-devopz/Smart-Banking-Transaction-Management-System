
"""
Banking Module
Handles account creation, deposits, withdrawals,
balance checking, and transaction history.
"""

from exceptions import (
    InsufficientBalanceError,
    InvalidAmountError,
    AccountNotFoundError
)


# Store account information
accounts = {}


def create_account(account_number, customer_name, balance=0):
    """Create a new bank account."""

    if account_number in accounts:
        print("Account already exists!")
        return

    accounts[account_number] = {
        "name": customer_name,
        "balance": balance,
        "transactions": []
    }

    print("Account created successfully!")


def get_account(account_number):
    """Find and return an account."""

    if account_number not in accounts:
        raise AccountNotFoundError(
            "Account does not exist!"
        )

    return accounts[account_number]


def deposit_money(account_number, amount):
    """Deposit money into a bank account."""

    account = get_account(account_number)

    if amount <= 0:
        raise InvalidAmountError(
            "Deposit amount must be greater than zero."
        )

    account["balance"] += amount

    account["transactions"].append(
        f"Deposited: Rs. {amount:.2f}"
    )

    print("Money deposited successfully!")


def withdraw_money(account_number, amount):
    """Withdraw money from a bank account."""

    account = get_account(account_number)

    if amount <= 0:
        raise InvalidAmountError(
            "Withdrawal amount must be greater than zero."
        )

    if amount > account["balance"]:
        raise InsufficientBalanceError(
            "Insufficient account balance!"
        )

    account["balance"] -= amount

    account["transactions"].append(
        f"Withdrawn: Rs. {amount:.2f}"
    )

    print("Withdrawal successful!")


def check_balance(account_number):
    """Display the current account balance."""

    account = get_account(account_number)

    print("\nCustomer Name:", account["name"])

    print(
        f"Available Balance: Rs. "
        f"{account['balance']:.2f}"
    )


def show_transactions(account_number):
    """Display account transaction history."""

    account = get_account(account_number)

    print("\n===== TRANSACTION HISTORY =====")

    if not account["transactions"]:
        print("No transactions available.")
        return

    for transaction in account["transactions"]:
        print(transaction)
