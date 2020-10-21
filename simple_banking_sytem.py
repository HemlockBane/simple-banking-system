import random as r
import sys
import string
import sqlite3 as sq3


class Db:

    def __init__(self):
        self.connection = self.init_db()

    def init_db(self):
        create_table_query = '''create table if not exists test (
                            id INTEGER PRIMARY KEY AUTOINCREMENT, 
                            number TEXT, pin TEXT, 
                            balance INTEGER DEFAULT 0
                        );'''

        db_connection = sq3.connect("test.s3db")
        db_cursor = db_connection.cursor()
        db_cursor.execute(create_table_query)

        return db_connection

    def save_card_details(self, card_num, pin):
        insert_value_query = ''' insert into test (number, pin)
                            values (?,?);'''
        db_cursor = self.connection.cursor()
        db_cursor.execute(insert_value_query, [card_num, pin])
        self.connection.commit()
        return int(db_cursor.lastrowid)

    def get_card_details(self, card_num, pin):
        select_user_query = '''select id from test
                               where number = ? and pin = ?;'''
        db_cursor = self.connection.cursor()
        db_cursor.execute(select_user_query, [card_num, pin])
        rows = db_cursor.fetchall()
        return rows

    def get_account_balance(self, card_id):
        select_user_balance_query = '''select balance from test
                                       where id = ?;'''
        db_cursor = self.connection.cursor()
        db_cursor.execute(select_user_balance_query, [card_id])
        rows = db_cursor.fetchall()
        return rows[0] if len(rows) != 0 else ()

    def close(self):
        self.connection.close()


class SimpleBankingSystem:
    def __init__(self):
        self.card_id = 0
        self.db_v2 = Db()

    def generate_control_sum(self, card_number_str, is_validate=False):
        if is_validate:
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

        ctrl_sum = self.generate_control_sum(issuer_id_num + account_id)
        checksum = self.generate_check_sum(ctrl_sum)
        card_num = issuer_id_num + account_id + str(checksum)

        pin = ""
        for i in range(4):
            pin = pin + str(r.randint(0, 9))
        # self.db.append((card_num, pin))
        card_id = self.db_v2.save_card_details(card_num, pin)
        # print("card db id", card_id)

        print("Your card has been created",
              "Your card number:", card_num, sep="\n")
        print("Your card PIN:", pin, sep="\n")

    def login(self):
        card_number = input("Enter your card number:\n")
        pin_code = input("Enter your PIN:\n")
        rows = self.db_v2.get_card_details(card_number, pin_code)

        if len(rows) != 0:
            self.card_id = rows[0][0]
            # print(self.card_id)
            print("You have successfully logged in!")
        else:
            print("Wrong card number or PIN!")

        while True:
            print("1. Balance", "2. Log out", "0. Exit", sep="\n")
            user_input = int(input())
            if user_input == 0:
                self.db_v2.close()
                print("Bye!")
                sys.exit()

            elif user_input == 1:
                result = self.db_v2.get_account_balance(self.card_id)
                print(f"Balance: {result[0]}")
            elif user_input == 2:
                print("You have successfully logged out!")
                break

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
