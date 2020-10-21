

# Main goals - Add options for
# ...........
# Deposit money into account
# Transfer money to another account
# Close an account


# Update after login options:
# - Option 1: Balance
# - Option 2: Add income
# - Option 3: Do transfer
# - Option 4: Close account
# - Option 5: Log out
# - Option 0: Exit


# 2 Add income:
# - Prompts user to "Enter income:"
# - Accepts income
# - Saves income to account
# -  Prints "Income was added!"


# 4 Close account:
# - Closes account
# - Prints "The account has been closed!"

# 3 Do transfer
# - Prints "Transfer"
# - Prompts user to "Enter card number:"
# - Accepts account number
# - Verifies account number:
# -- If account number is invalid (i.e doesn't pass Luhn's algorithm), it prints "Probably you made a mistake in the card number. Please try again!"
# -- If account number doesn't exist in the db, it prints "Such a card does not exist."
# -- If account number is the same as the currently logged in account, it prints "You can't transfer money to the same account!"
# -- If the account number passes all the tests above, it prompts the user with "Enter how much money you want to transfer:"
# ---- Accepts input
# ---- If the money the user has is less than the transfer amount, it prints "Not enough money!"
# ---- If the money the user has is equal or greater than the transfer amount,
# ------ Transfers money, deduct sfrom user's account
# ------ Prints "Success!"


# Using Luhn algorithm o check the validity of a card number
# card_number_str = "4000008449433403"
# ctrl_sum = generate_control_sum(card_number_str[:-1])
# result = ctrl_sum + int(card_number_str[-1])

# if result % 10 == 0:
#     #     print("valid")
# generate_check_sum(1111)

# generate_check_sum(ctrl_sum)


# Generate control sum
# .........................
# Remove checksum (the last digit if to check for validity)
# Multiply odd digit indices by 2 (index should start at 1)
# Subtract 9 from numbers over 9
# Add all numbers and return


# Check for valid card number
# ...............................
# Find result of (control sum + checksum)
# find result modulo 10
# - If result is 0, card number is valid
# - If result is not 0, card number is not valid


# Generate check sum
# ...................
# Accept an integer
# If number is not divisible by 10, get the last digit
# Subtract it from 10
# Output the number as string


# Useful stuff/stuff to check out later
# ...................
# db = [('4000000856777642', '5351'), ('4000003869633784', '4642')]
# string.digits
