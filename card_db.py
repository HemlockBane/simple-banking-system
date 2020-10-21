import sqlite3 as sq3


class Db:

    def __init__(self):
        self.table_name = "card"
        self.db_name = "card.s3db"
        self.connection = self.init_db()

    def init_db(self):
        create_table_query = f'''create table if not exists {self.table_name} (
                            id INTEGER PRIMARY KEY AUTOINCREMENT, 
                            number TEXT, pin TEXT, 
                            balance INTEGER DEFAULT 0
                        );'''

        db_connection = sq3.connect(self.db_name)
        db_cursor = db_connection.cursor()
        db_cursor.execute(create_table_query)

        return db_connection

    def get_all_card_details(self):
        select_all_query = f'''select * from {self.table_name};'''
        db_cursor = self.connection.cursor()
        db_cursor.execute(select_all_query)
        rows = db_cursor.fetchall()
        print(rows)

    def save_card_details(self, card_num, pin):
        insert_value_query = f''' insert into {self.table_name} (number, pin)
                            values (?,?);'''
        db_cursor = self.connection.cursor()
        db_cursor.execute(insert_value_query, [card_num, pin])
        self.connection.commit()
        return int(db_cursor.lastrowid)

    def get_card_details(self, card_num, pin):
        select_user_query = f'''select id from {self.table_name}
                               where number = ? and pin = ?;'''
        db_cursor = self.connection.cursor()
        db_cursor.execute(select_user_query, [card_num, pin])
        rows = db_cursor.fetchall()
        return rows

    def check_if_card_exists(self, card_num):
        select_user_query = f'''select id from {self.table_name}
                                      where number = ?;'''
        db_cursor = self.connection.cursor()
        db_cursor.execute(select_user_query, [card_num])
        rows = db_cursor.fetchall()
        return rows

    def get_account_balance(self, card_id):
        select_user_balance_query = f'''select balance from {self.table_name}
                                       where id = ?;'''
        db_cursor = self.connection.cursor()
        db_cursor.execute(select_user_balance_query, [card_id])
        rows = db_cursor.fetchall()
        return rows[0] if len(rows) != 0 else ()

    def delete_card_details(self, card_id):
        delete_card_query = f'''delete from {self.table_name}
                               where id = ?'''
        db_cursor = self.connection.cursor()
        db_cursor.execute(delete_card_query, [card_id])
        self.connection.commit()

    def increase_account_balance(self, amount, card_id):
        update_value_query = f'''update {self.table_name}
                                set balance = balance + ?
                                where id = ?'''
        db_cursor = self.connection.cursor()
        db_cursor.execute(update_value_query, [amount, card_id])
        self.connection.commit()

    def decrease_account_balance(self, amount, card_id):
        update_value_query = f'''update {self.table_name}
                                set balance = balance - ?
                                where id = ?'''
        db_cursor = self.connection.cursor()
        db_cursor.execute(update_value_query, [amount, card_id])
        self.connection.commit()

    def close(self):
        self.connection.close()