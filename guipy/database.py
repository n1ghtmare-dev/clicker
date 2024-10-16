<<<<<<< HEAD
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

    def edit_level(self, level):
        with self.connection:
            try:
                lock.acquire(True)
                sql = "UPDATE user SET level = ?"
                self.cursor.execute(sql, (level,))
            finally:
                lock.release()

    def edit_user(self, one_click=None, clicks_counter=None, level=None, skill=None):
        var = []
        if one_click:
            var.append(f"one_click = '{one_click}'")
        if clicks_counter:
            var.append(f"clicks_counter = '{clicks_counter}'")
        if level:
            var.append(f"level = '{level}'")
        if skill:
            var.append(f"skill = '{skill}'")
        with self.connection:
            try:
                lock.acquire(True)
                sql = f"UPDATE user SET {','.join(var)}"
                self.cursor.execute(sql)
            finally:
                lock.release()
=======
import aiosqlite

class Database:
    def __init__(self, file_name):
        self.file_name = file_name

    # Метод, обрабатывающий запросы
    async def execute(self, sql: str, parameters: tuple=None, fetchone=None, fetchall=False, commit=False):
        async with aiosqlite.connect(self.file_name) as db:
            if not parameters:
                parameters = ()
            data = None
            cursor = await db.cursor()
            await cursor.execute(sql, parameters) # Отправляем запрос

            if commit:
                await db.commit()
            if fetchone:
                data = await cursor.fetchone()
            if fetchall:
                data = await cursor.fetchall()

            return data
>>>>>>> main

    def save_user_data(self, one_click, clicks_counter):
        with self.connection:
            try:
                lock.acquire(True)
                sql = "UPDATE user SET one_click = ?, clicks_counter = ?"
                self.cursor.execute(sql, (one_click, clicks_counter,))
            finally:
                lock.release()
<<<<<<< HEAD

    def get_tasks(self):
        with self.connection:
            try:
                lock.acquire(True)
                sql = "SELECT * FROM tasks"
                res = self.cursor.execute(sql).fetchall()
                return res
            finally:
                lock.release()

    def get_task_info(self, task_id):
        with self.connection:
            try:
                lock.acquire(True)
                sql = "SELECT * FROM tasks WHERE id = ?"
                res = self.cursor.execute(sql, (task_id,)).fetchone()
                return res
            finally:
                lock.release()

    def plus_use_task(self, task_id, use):
        with self.connection:
            try:
                lock.acquire(True)
                sql = "UPDATE tasks SET done = ? WHERE id = ?"
                self.cursor.execute(sql, (use, task_id,))
            finally:
                lock.release()

    def get_good_info(self, good_id):
        with self.connection:
            try:
                lock.acquire(True)
                sql = "SELECT * FROM click_shop WHERE id = ?"
                res = self.cursor.execute(sql, (good_id,)).fetchone()
                return res
            finally:
                lock.release()

    def edit_good_use(self, good_id, use):
        with self.connection:
            try:
                lock.acquire(True)
                sql = "UPDATE click_shop SET use = ? WHERE id = ?"
                self.cursor.execute(sql, (use, good_id,))
            finally:
                lock.release()

=======
>>>>>>> 028a1b2 (added assets, ranks system, new GUI)
>>>>>>> main
