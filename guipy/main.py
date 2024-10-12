from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QThreadPool
from PySide6.QtGui import QPixmap
from ui_main import Ui_MainWindow
from asyncio import create_task
from database import Database
from threading import Thread
import asyncio
from icecream import ic
import time
import sys
import sqlite3

db = Database('database.db')

class MinerWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MinerWindow, self).__init__()
        self.setupUi(self)

        # Объявляем переменные, которые обновятся
        self.one_click = 1

        self.data_update()

        # Потоки
        self.auto_save_thread = QThreadPool()
        self.auto_save_thread.start(self.auto_save)

        # Объявляем события
        self.click_btn.clicked.connect(self.click)
        self.level_upgrade_btn.clicked.connect(self.level_upgrade)



    # Обновляем переменные
    def data_update(self):
        user_info = db.get_user_info()

        self.one_click = user_info[0]
        self.clicks_counter.setText(str(user_info[1]))

        # Level
        level_info = db.get_level_info(user_info[2])
        self.goal.setText(str(level_info[2]))
        self.rating.setText(self.clicks_counter.text())
        self.rank_bar.setValue(round((int(self.clicks_counter.text()) / int(self.goal.text()) * 100)))
        self.rank_img.setPixmap(QPixmap(u":/images/ranks/Shield/{}".format(level_info[3])))

    def click(self):
        click = int(self.clicks_counter.text())+self.one_click
        self.clicks_counter.setText(str(click))
        self.update_rang()

    def level_upgrade(self):
        user_info = db.get_user_info()
        level_info = db.get_level_info(user_info[2])
        if int(self.clicks_counter.text()) >= level_info[2]:
            db.edit_user(clicks_counter=int(self.clicks_counter.text())-level_info[2], level=int(user_info[2])+1)
            self.data_update()


    def auto_save(self):
        print("Auto save ON | 10s")
        while True:
            # print("log | Обновление данных")
            db.save_user_data(self.one_click, self.clicks_counter.text())
            time.sleep(10)

    def update_rang(self):
        cc = self.clicks_counter.text()
        self.rating.setText(cc)
        # Изменяем прогрессбар
        new_percent = round((int(cc) / int(self.goal.text()) * 100))
        if new_percent - self.rank_bar.value() >= 1:
            self.rank_bar.setValue(new_percent)

        if int(self.clicks_counter.text()) >= int(self.goal.text()):
            # Загорается кнопка и можно улучшить уровень
            pass



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MinerWindow()
    window.show()

    sys.exit(app.exec())
