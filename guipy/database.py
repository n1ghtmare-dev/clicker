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

<<<<<<< HEAD
<<<<<<< HEAD
    async def edit_click(self, value):
        sql = "UPDATE user SET click = ?"
        await self.execute(
            sql=sql,
            parameters=(value),
            commit=True
            )

    async def get_click(self):
        sql = "SELECT * FROM user"
        res = await self.execute(sql=sql, fetchall=True)
        return res[0][0]
=======
    def edit_level(self, level):
        with self.connection:
            try:
                lock.acquire(True)
                sql = "UPDATE user SET level = ?"
                self.cursor.execute(sql, (level,))
            finally:
                lock.release()

    def edit_user(self, one_click=None, clicks_counter=None, level=None):
        var = []
        if one_click:
            var.append(f"one_click = '{one_click}'")
        if clicks_counter:
            var.append(f"clicks_counter = '{clicks_counter}'")
        if level:
            var.append(f"level = '{level}'")
        with self.connection:
            try:
                lock.acquire(True)
                sql = f"UPDATE user SET {','.join(var)}"
                self.cursor.execute(sql)
            finally:
                lock.release()

=======
>>>>>>> parent of 028a1b2 (added assets, ranks system, new GUI)
    def save_user_data(self, one_click, clicks_counter):
        with self.connection:
            try:
                lock.acquire(True)
                sql = "UPDATE user SET one_click = ?, clicks_counter = ?"
                self.cursor.execute(sql, (one_click, clicks_counter,))
            finally:
                lock.release()
>>>>>>> 028a1b2 (added assets, ranks system, new GUI)
