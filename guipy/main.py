from PySide6.QtWidgets import (QApplication, QMainWindow, QGraphicsBlurEffect, QFrame, QPushButton, QLabel, QSpacerItem,
                               QHBoxLayout, QVBoxLayout, QSizePolicy)
from PySide6.QtCore import QThreadPool, QSize, QRect, Qt
from PySide6.QtGui import QPixmap, QFont, QCursor
from ui_main import Ui_MainWindow
from database import Database
from functions import *
from icecream import ic
import time
import sys

db = Database('database.db')


class MinerWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MinerWindow, self).__init__()
        self.setupUi(self)

        # Объявляем переменные
        self.task_use_info_label = None
        self.one_click = 1
        self.main_page_data_update()

        # Потоки
        self.auto_save_thread = QThreadPool()
        self.auto_save_thread.start(self.auto_save)

        # Объявляем события
        self.click_btn.clicked.connect(self.click)
        self.level_upgrade_btn.clicked.connect(self.level_upgrade)
        self.menu_btn.clicked.connect(self.open_menu)
        self.close_island_btn.clicked.connect(self.close_menu)

        # Эффекты
        self.blur_effect = QGraphicsBlurEffect()
        self.blur_effect.setBlurRadius(5)

        # Открываем главный виджет
        self.stackedWidget.setCurrentWidget(self.main_page)

        # Шрифты
        # PLUMP BOLD
        self.font_plump = QFont()
        self.font_plump.setFamilies([u"Plump"])
        self.font_plump.setBold(True)
        # Data Trash
        self.font_dt = QFont()
        self.font_dt.setFamilies([u"Data Trash"])
        self.font_dt.setPointSize(8)
        # Intro Black BOLD
        self.font_intro_bold = QFont()
        self.font_intro_bold.setFamilies([u"Intro Black"])
        self.font_intro_bold.setPointSize(8)
        self.font_intro_bold.setBold(True)

    # Открытие панели меню
    def open_menu(self) -> None:
        self.stackedWidget.setCurrentWidget(self.island_page)
        # Обновляем переменные
        self.island_page_data_update()

    def close_menu(self) -> None:
        self.stackedWidget.setCurrentWidget(self.main_page)
        # Удаление фреймов
        i = 0
        while True:
            i += 1
            if hasattr(self, "island_tasks_frame_" + str(i)):
                self.verticalLayout_7.removeWidget(getattr(self, "island_tasks_frame_" + str(i), 0))
            else:
                break

    # Обновляем переменные
    def main_page_data_update(self) -> None:
        user_info = db.get_user_info()

        self.one_click = user_info[0]
        self.clicks_counter.setText(str(user_info[1]))

        # Level
        level_info = db.get_level_info(user_info[2])
        self.goal.setText(str(level_info[2]))
        self.rating.setText(self.clicks_counter.text())
        self.rank_bar.setValue(round((int(self.clicks_counter.text()) / int(self.goal.text()) * 100)))
        self.rank_img.setPixmap(QPixmap(u":/images/ranks/Shield/{}".format(level_info[3])))

    def island_page_data_update(self) -> None:
        user_info = db.get_user_info()
        level_info = db.get_level_info(user_info[2])
        self.island_money_counter.setText(str(user_info[1]))
        self.island_skill_counter.setText(str(user_info[3]))
        self.island_level_title.setText(level_info[1])
        self.island_task_bar.setValue(0)

        # Выводим задачки
        island_area_task_update(self)

        # Недоработанное
        # self.label_8.setGraphicsEffect(self.blur_effect)

    def start_task(self, tid) -> None:
        task_info = db.get_task_info(tid)
        print(tid)
        # sec * 60
        max_val = task_info[3] * 60
        self.island_task_bar.setRange(0, max_val)
        for i in range(max_val):
            self.island_task_bar.setValue(i+1)
            time.sleep(0.01)
        self.island_task_bar.setValue(0)

        # print(f"Выполнение задания {task_info[0]}")

    def click(self) -> None:
        click = int(self.clicks_counter.text()) + self.one_click
        self.clicks_counter.setText(str(click))
        self.update_rang()

    def level_upgrade(self) -> None:
        user_info = db.get_user_info()
        level_info = db.get_level_info(user_info[2])
        if int(self.clicks_counter.text()) >= level_info[2]:
            db.edit_user(clicks_counter=int(self.clicks_counter.text()) - level_info[2], level=int(user_info[2]) + 1)
            self.main_page_data_update()

    def auto_save(self) -> None:
        print("Auto save ON | 10s")
        while True:
            # print("log | Обновление данных")
            db.save_user_data(self.one_click, self.clicks_counter.text())
            time.sleep(10)

    def update_rang(self) -> None:
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
