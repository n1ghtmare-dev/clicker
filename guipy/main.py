from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt
from ui_main import Ui_MainWindow
from database import Database
import asyncio
import sys

db = Database('database.db')

class MinerWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MinerWindow, self).__init__()
        self.setupUi(self)


        # Объявляем переменные с нормальными названиями
        self.click_btn = self.pushButton
        self.clicks_counter = self.label_2
        self.rang_bar = self.progressBar

        # Объявляем события
        self.click_btn.clicked.connect(self.click)

    # Обновляем переменные
    async def data_update(self):
        self.one_click = await db.get_click()
        print(self.one_click)

    def click(self):
        click = int(self.clicks_counter.text())+self.one_click
        self.clicks_counter.setText(str(click))


app = QApplication(sys.argv)

window = MinerWindow()
asyncio.run(window.data_update())
window.show()

app.exec()