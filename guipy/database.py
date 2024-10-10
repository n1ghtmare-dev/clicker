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
