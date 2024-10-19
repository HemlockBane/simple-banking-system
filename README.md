# Simple Banking System

This is a command-line based Simple Banking System implemented in Python. It allows users to create accounts, log in, check balances, add income, transfer money, and close accounts. The system also uses Luhn's algorithm to validate card numbers.

## Features

- **Create an account**: Generates a unique card number and PIN.
- **Log in**: Allows users to log into their account using their card number and PIN.
- **Check balance**: View the current balance of the account.
- **Add income**: Add a specified amount of income to the account.
- **Transfer money**: Transfer money to another account, with Luhn's algorithm validation for the card number.
- **Close account**: Delete an account and all its associated data.
- **Logout and exit**: Log out or exit the program.

## Database

The application uses a SQLite database to store account information.

- **Database File**: `card.s3db`
- **Table**: `card`
- **Columns**:
  - `id`: Integer, Primary Key
  - `card_number`: String
  - `pin`: String
  - `balance`: Integer (Default 0)

## Luhn's Algorithm

The system uses **Luhn's Algorithm** for generating valid card numbers. It also validates card numbers entered during the transfer process to ensure they are correct.

## Installation

1. Clone the repository.
2. Install dependencies (if necessary):
   ```bash
   pip install sqlalchemy
   ```

## Run the application
```bash
python simple_banking.py
```

## Usage
When you run the program, you will be presented with a menu:

1) Create an account: This generates a card number and PIN for you and stores it in the database.
2) Log into account: Log into your account using the card number and PIN.
0) Exit: Close the application.

Once logged in, you can:
1) Balance: Check your account balance.
2) Add income: Add a specified amount of money to your account.
3) Do transfer: Transfer money to another account, with card number validation.
4) Close account: Delete your account.
5) Log out: Log out of your account.
0) Exit: Close the application.
