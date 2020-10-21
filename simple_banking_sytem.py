from card_db import Db
import random as r
import sys



class SimpleBankingSystem:
    def __init__(self):
        self.card_id = 0
        self.card_number = ""
        self.db_v2 = Db()

    def generate_control_sum(self, card_number_str, should_validate=False):
        '''Generate control sum using Luhn algorithm'''
        if should_validate:
            card_number_str = card_number_str[:-1]

        int_map = map(int, list(card_number_str))
        int_list = list(int_map)

        for idx, num in enumerate(int_list):
            if idx % 2 == 0:  # Compensate for zero-based index by using even numbers
                int_list[idx] = num * 2

        for idx, num in enumerate(int_list):
            if num > 9:
                int_list[idx] = num - 9

        return sum(int_list)

    def generate_check_sum(self, ctrl_sum: int):
        '''Generate a checksum to complete the control sum using Luhn algorithm'''
        if ctrl_sum % 10 != 0:
            last_digit_str = str(ctrl_sum)[-1]
            checksum = 10 - int(last_digit_str)
        else:
            checksum = 0

        return checksum

    def validate_card_number(self, card_num):
        ctrl_sum = self.generate_control_sum(card_num, should_validate=True)
        result = ctrl_sum + int(card_num[-1])

        if result % 10 == 0:
            return True
        else:
            return False

    def create_account(self):
        issuer_id_num = "400000"
        r.seed()

        account_id = ""
        for i in range(9):
            account_id = account_id + str(r.randint(0, 9))

        ctrl_sum = self.generate_control_sum(issuer_id_num + account_id)
        checksum = self.generate_check_sum(ctrl_sum)
        card_num = issuer_id_num + account_id + str(checksum)

        pin = ""
        for i in range(4):
            pin = pin + str(r.randint(0, 9))

        self.db_v2.save_card_details(card_num, pin)

        print("Your card has been created",
              "Your card number:", card_num, sep="\n")
        print("Your card PIN:", pin, sep="\n")

    def login(self):
        card_number = input("Enter your card number:\n")
        pin_code = input("Enter your PIN:\n")
        rows = self.db_v2.get_card_details(card_number, pin_code)

        if len(rows) == 0:
            print("Wrong card number or PIN!")
        else:
            self.card_id = rows[0][0]
            self.card_number = card_number
            print("You have successfully logged in!")
            # self.db_v2.get_all_card_details()

            while True:
                print("1. Balance", "2. Add income", "3. Do transfer",
                      "4. Close account", "5. Log out", "0. Exit", sep="\n")
                user_input = int(input())
                if user_input == 0:
                    self.db_v2.close()
                    print("Bye!")
                    sys.exit()

                elif user_input == 1:
                    result = self.db_v2.get_account_balance(self.card_id)
                    print(f"Balance: {result[0]}")

                elif user_input == 2:
                    amount = int(input("Enter income:\n"))
                    self.add_income(amount)
                    print('Income was added!')

                elif user_input == 3:
                    self.transfer_money()

                elif user_input == 4:
                    self.close_account()
                    print("The account has been closed!")
                    break

                elif user_input == 5:
                    print("You have successfully logged out!")
                    break

    def add_income(self, amount):
        self.db_v2.increase_account_balance(amount, self.card_id)

    def transfer_money(self):
        print("Transfer")
        card_num = input("Enter card number:\n")

        is_valid = self.validate_card_number(card_num)
        if not is_valid:
            print("Probably you made a mistake in the card number. Please try again!")
            return

        if card_num == self.card_number:
            print("You can't transfer money to the same account!")
            return

        rows = self.db_v2.check_if_card_exists(card_num)
        if len(rows) == 0:
            print("Such a card does not exist.")
            return

        transfer_amount = int(
            input("Enter how much money you want to transfer:\n"))
        res = self.db_v2.get_account_balance(self.card_id)
        acct_balance = res[0]

        if acct_balance < transfer_amount:
            print("Not enough money!")
            return

        self.db_v2.decrease_account_balance(transfer_amount, self.card_id)

        dest_card_id = rows[0][0]
        self.db_v2.increase_account_balance(transfer_amount, dest_card_id)
        print("Success!")

    def close_account(self):
        self.db_v2.delete_card_details(self.card_id)

    def run(self):
        while True:
            print("1. Create an account",
                  "2. Log into account", "0. Exit", sep="\n")
            user_input = int(input())
            if user_input == 0:
                self.db_v2.close()
                print("Bye!")
                break
            elif user_input == 1:
                self.create_account()
            elif user_input == 2:
                self.login()


simple_banking = SimpleBankingSystem()
simple_banking.run()
