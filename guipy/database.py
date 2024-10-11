import sqlite3
from threading import Lock

lock = Lock()

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file, check_same_thread=False, timeout=1)
        self.cursor = self.connection.cursor()

    def edit_click(self, value):
        with self.connection:
            try:
                lock.acquire(True)
                sql = "UPDATE user SET one_click = ?"
                self.cursor.execute(sql, (value,))
            finally:
                lock.release()

    def get_user_info(self):
        with self.connection:
            try:
                lock.acquire(True)
                sql = "SELECT * FROM user"
                res = self.cursor.execute(sql).fetchone()
                return res
            finally:
                lock.release()

    def get_level_info(self, number):
        with self.connection:
            try:
                lock.acquire(True)
                sql = "SELECT * FROM levels WHERE number = ?"
                res = self.cursor.execute(sql, (number,)).fetchone()
                return res
            finally:
                lock.release()

    def save_user_data(self, one_click, clicks_counter):
        with self.connection:
            try:
                lock.acquire(True)
                sql = "UPDATE user SET one_click = ?, clicks_counter = ?"
                self.cursor.execute(sql, (one_click, clicks_counter,))
            finally:
                lock.release()
