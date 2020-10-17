import random as r
import sys
import string


class SimpleBankingSystem:
    def __init__(self):
        # self.db = [('4000000856777642', '5351'), ('4000003869633784', '4642')]
        self.db = []
        self.balance = 0

# Generates a control sum that satisfies the Luhn algorithm
    def generate_control_sum(self, card_number_str, is_validate=False):
        if is_validate:
            card_number_str = card_number_str[:-1]

        int_map = map(int, list(card_number_str))
        int_list = list(int_map)

        for idx, num in enumerate(int_list):
            # Assuming the indices are 1-based, we're to double the value of odd indices
            # but since I can't find a way to tweak enumerate() on short notice, 
            # compensate for zero-based index by doubling the value of even indices
            if idx % 2 == 0:
                int_list[idx] = num * 2

        for idx, num in enumerate(int_list):
            if num > 9:
                int_list[idx] = num - 9

        return sum(int_list)

    # Generates a checksum that satisfies the Luhn algorithm
    def generate_check_sum(self, ctrl_sum):
        if ctrl_sum % 10 != 0:
            last_digit_str = str(ctrl_sum)[-1]
            checksum = 10 - int(last_digit_str)
        else:
            checksum = 0
            
        return checksum

    def create_account(self):
        issuer_id_num = "400000"
        r.seed()

        account_id = ""
        for i in range(9):
            account_id = account_id + str(r.randint(0, 9))

        ctrl_sum = self.generate_control_sum(issuer_id_num+account_id)
        checksum = self.generate_check_sum(ctrl_sum)
        card_details = issuer_id_num+account_id + str(checksum)

        pin = ""
        for i in range(4):
            pin = pin + str(r.randint(0, 9))
        self.db.append((card_details, pin))

        print("Your card has been created",
              "Your card number:", card_details, sep="\n")
        print("Your card PIN:", pin, sep="\n")

    def login(self):
        card_number = input("Enter your card number:\n")
        pin_code = input("Enter your PIN:\n")

        if (card_number, pin_code) in self.db:
            print("You have successfully logged in!")
        else:
            print("Wrong card number or PIN!")

        while True:
            print("1. Balance", "2. Log out", "0. Exit", sep="\n")
            user_input = int(input())
            if user_input == 0:
                print("Bye!")
                sys.exit()
                # return
            elif user_input == 1:
                print(f"Balance: {self.balance}")
            elif user_input == 2:
                print("You have successfully logged out!")
                break

    def run(self):
        while True:
            print("1. Create an account",
                  "2. Log into account", "0. Exit", sep="\n")
            user_input = int(input())
            if user_input == 0:
                print("Bye!")
                break
            elif user_input == 1:
                self.create_account()
            elif user_input == 2:
                self.login()


simple_banking = SimpleBankingSystem()
simple_banking.run()
