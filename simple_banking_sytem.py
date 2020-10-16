import random as r
import sys
import string


class SimpleBankingSystem:
    def __init__(self):
        self.db = [('4000000856777642', '5351'), ('4000003869633784', '4642')]
        self.balance = 0

    def create_account(self):
        iin = "400000"
        r.seed()

        account_id = ""
        for i in range(9):
            account_id = account_id + str(r.randint(0, 9))
        checksum = str(r.randint(0, 9))
        card_details = iin+account_id + checksum

        pin_code = ""
        for i in range(4):
            pin_code = pin_code + str(r.randint(0, 9))
        self.db.append((card_details, pin_code))
        print("Your card has been created",
              "Your card number:", card_details, sep="\n")
        print("Your card PIN:", pin_code, sep="\n")

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