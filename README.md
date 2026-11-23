# Smart Banking & Transaction Management System

A simple command-line banking application written in Python. It allows users to create accounts, deposit and withdraw money, check balances, and view transaction history during a running session.

## Features

- Create a bank account
- Deposit money
- Withdraw money
- Check account balance
- View transaction history
- Handle invalid menu choices and numeric input
- Report account, balance, and amount errors

## Requirements

- Python 3
- No external packages required

## Project Structure

```text
SmartBanking/
|-- main.py       # Interactive command-line menu
|-- banking.py    # Account and transaction operations
|-- exceptions.py # Custom banking exceptions
|-- README.md
```

## Getting Started

1. Open a terminal in the project directory.
2. Run the application:

```bash
python main.py
```

3. Choose an operation from the menu.

## Menu Options

| Option | Action |
|---|---|
| 1 | Create Account |
| 2 | Deposit Money |
| 3 | Withdraw Money |
| 4 | Check Balance |
| 5 | View Transaction History |
| 6 | Exit |

## Example Usage

```text
Enter account number: 1001
Enter customer name: Alex
Account created successfully!

Enter account number: 1001
Enter deposit amount: 5000
Money deposited successfully!

Enter account number: 1001
Enter withdrawal amount: 1250
Withdrawal successful!
```

## Transaction Records

The application stores account details and transaction messages in memory for the duration of the program. Deposits and withdrawals are recorded in the format:

```text
Deposited: Rs. 5000.00
Withdrawn: Rs. 1250.00
```

## Error Handling

The application provides clear messages for the following situations:

- Account number does not exist
- Withdrawal amount exceeds the available balance
- Deposit or withdrawal amount is zero or negative
- Menu choice or entered number is invalid
- Unexpected application errors

## Data Persistence

Accounts are stored in a Python dictionary while the application is running. Data is cleared when the program exits. Database or file storage is not included in this version.
