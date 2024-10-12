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

    def save_user_data(self, one_click, clicks_counter):
        with self.connection:
            try:
                lock.acquire(True)
                sql = "UPDATE user SET one_click = ?, clicks_counter = ?"
                self.cursor.execute(sql, (one_click, clicks_counter,))
            finally:
                lock.release()
>>>>>>> 028a1b2 (added assets, ranks system, new GUI)
