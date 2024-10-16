<<<<<<< HEAD
from PySide6.QtWidgets import (QApplication, QMainWindow, QFrame, QPushButton, QLabel, QSpacerItem, QMessageBox,
                               QHBoxLayout, QVBoxLayout, QWidget, QGraphicsDropShadowEffect)
from PySide6.QtCore import QThreadPool, QSize, QRect, Qt, QPropertyAnimation
from PySide6.QtGui import QPixmap, QFont, QCursor, QPainter
from PySide6 import QtQuick
from ui_main import Ui_MainWindow
from database import Database
from functions import *
from styles import *
from error import Ui_Error
from icecream import ic
import time
=======
from PySide6.QtWidgets import QApplication, QMainWindow
<<<<<<< HEAD
from PySide6.QtCore import Qt
=======
from PySide6.QtCore import QThreadPool
from ui_main import Ui_MainWindow
from database import Database
import asyncio
>>>>>>> main
import sys

db = Database('database.db')

<<<<<<< HEAD

class MinerWindow(QMainWindow, Ui_MainWindow):

=======
class MinerWindow(QMainWindow, Ui_MainWindow):
>>>>>>> main
    def __init__(self):
        super(MinerWindow, self).__init__()
        self.setupUi(self)

<<<<<<< HEAD
        # Объявляем переменные
        self.error = ErrorWindow()
        self.error.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.task_use_info_label = None
        self.last_click = 0
        self.one_click = 1
        self.boost_active = True
        self.task_active = False
        self.menu_bar_frames = {self.island_page_2: self.frame_10,
                                self.shop_page: self.frame_9,
                                self.backpack_page: self.frame_11}
        # MSG
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Warning)
        self.msg.setWindowTitle("Сообщение")

        # Потоки
        self.auto_save_thread = QThreadPool()
        self.anim = QThreadPool()
        self.task_execution = QThreadPool()
        self.rank_bar_inprogress_anim = QThreadPool()
        self.auto_click_thread = QThreadPool()
        self.boost_clicks_thread = QThreadPool()
=======
        # Объявляем переменные с нормальными названиями
        self.click_btn = self.pushButton
        self.clicks_counter = self.label_2
        self.rang_bar = self.progressBar
        self.rating = self.label_6
        self.goal = self.label_4

        # Объявляем переменные, которые обновятся
        self.one_click = 1

        self.data_update()

        # Потоки
        self.auto_save_thread = QThreadPool()
>>>>>>> main
        self.auto_save_thread.start(self.auto_save)

        # Объявляем события
        self.click_btn.clicked.connect(self.click)
<<<<<<< HEAD
        self.level_upgrade_btn.clicked.connect(self.level_upgrade)
        self.menu_btn.clicked.connect(lambda: open_menu(self))
        self.close_island_btn.clicked.connect(self.close_menu)
        self.open_shop_btn.clicked.connect(lambda: open_shop(self))
        self.open_backpack_btn.clicked.connect(lambda: open_backpack(self))
        self.open_island_btn.clicked.connect(lambda: open_island(self))

        # SHOP BTNS CONNECT
        self.btn_one_click_buy_1.clicked.connect(lambda: self.click_buy(1))
        self.btn_one_click_buy_2.clicked.connect(lambda: self.click_buy(2))
        self.btn_one_click_buy_3.clicked.connect(lambda: self.click_buy(3))
        self.btn_one_boost_buy_1.clicked.connect(lambda: self.boost_buy(1))
        self.btn_one_boost_buy_2.clicked.connect(lambda: self.boost_buy(2))

        # Эффекты
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        self.centralwidget.setGraphicsEffect(shadow)

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

        self.main_page_data_update()

    # Анимация
    def animation_rank_up(self) -> None:
        user_info = db.get_user_info()
        level_info = db.get_level_info(user_info[2])
        sprites = ":images/sprites/sprites/blue_1/b{}.png"
        count = 13
        for i in range(1, count+1):
            self.rank_img.setPixmap(QPixmap(sprites.format(i)))
            time.sleep(0.07)
        self.rank_img.setPixmap(QPixmap(f":/images/ranks/Shield/{level_info[3]}"))
        # print(self.rank_img.setPixmap(QPixmap(u":images/sprites/sprites/blue_1.png")))
        # self.rank_img.setScaledContents(False)

    def activate_btn(self) -> None:
        s_widget = self.stackedWidget_2.currentWidget()
        for page in list(self.menu_bar_frames):
            btn = self.menu_bar_frames[page].children()[1]
            frame_img = self.menu_bar_frames[page].children()[2]
            if page == s_widget:
                btn.setStyleSheet("color: rgb(85, 255, 127);\n")
                frame_img.setVisible(True)
            else:
                frame_img.setVisible(False)
                btn.setStyleSheet("color: rgb(255, 255, 255);\n")

    def click_buy(self, btn_id) -> int:
        if self.boost_active:
            self.error.label_2.setText("Действует буст, покупки запрещены!")
            self.error.show()

            return 0
        good = db.get_good_info(btn_id)
        self.one_click += good[1]
        if int(self.clicks_counter.text()) >= good[2]:
            new_balance = int(self.clicks_counter.text()) - good[2]
            self.clicks_counter.setText(str(new_balance))
            db.edit_user(one_click=self.one_click, clicks_counter=new_balance)
            db.edit_good_use(use=good[4]+1, good_id=btn_id)
            self.island_page_top_update()
        else:
            self.error.label_2.setText("Недостаточно монет!")
            self.error.show()


    def boost_buy(self, boost: int) -> None:
        if boost == 1:
            price = 1750
            if int(self.clicks_counter.text()) >= price:
                if self.auto_click_thread.activeThreadCount() == 0:
                    new_balance = int(self.clicks_counter.text()) - price
                    self.clicks_counter.setText(str(new_balance))
                    db.edit_user(clicks_counter=new_balance)
                    self.auto_click_thread.start(self.auto_click_start)
                    self.island_page_top_update()
                else:
                    self.error.label_2.setText("У вас уже действует авто-клик!")
                    self.error.show()
            else:
                self.error.label_2.setText("Недостаточно монет!")
                self.error.show()
        elif boost == 2:
            price = 9590
            if int(self.clicks_counter.text()) >= price:
                if self.boost_clicks_thread.activeThreadCount() == 0:
                    new_balance = int(self.clicks_counter.text()) - price
                    self.clicks_counter.setText(str(new_balance))
                    db.edit_user(clicks_counter=new_balance)
                    self.boost_clicks_thread.start(self.boost_clicks_start)
                    self.island_page_top_update()
                else:
                    self.error.label_2.setText("У вас уже действует буст!")
                    self.error.show()
            else:
                self.error.label_2.setText("Недостаточно монет!")
                self.error.show()

    def boost_clicks_start(self):
        self.boost_active = True
        self.one_click *= 2
        time.sleep(30)
        self.one_click //= 2
        db.edit_user(one_click=self.one_click)
        self.boost_active = False


    def auto_click_start(self):
        for i in range(15):
            print('start')
            new = int(self.clicks_counter.text())+self.one_click
            self.clicks_counter.setText(str(new))
            db.edit_user(clicks_counter=new)
            time.sleep(1)

    def close_menu(self) -> None:
        self.stackedWidget.setCurrentWidget(self.main_page)
        self.tasks_check()

    # Удаление фреймов
    def tasks_check(self) -> None:
        i = 0
        while True:
            i += 1
            if hasattr(self, "island_tasks_frame_" + str(i)):
                self.verticalLayout_7.removeWidget(getattr(self, "island_tasks_frame_" + str(i), 0))
            else:
                break

    # Обновляем переменные
    def main_page_data_update(self) -> None:
=======
        self.pushButton_3.clicked.connect(self.close)


    # Обновляем переменные
    def data_update(self):
>>>>>>> main
        user_info = db.get_user_info()

        self.one_click = user_info[0]
        self.clicks_counter.setText(str(user_info[1]))

        # Level
        level_info = db.get_level_info(user_info[2])
<<<<<<< HEAD
        self.level_number.setText(f"Уровень {user_info[2]}")
        self.goal.setText(str(level_info[2]))
        self.rating.setText(self.clicks_counter.text())
        self.rank_bar.setRange(0, level_info[2])
        self.rank_bar.setValue(user_info[1])
        self.rank_img.setPixmap(QPixmap(u":/images/ranks/Shield/{}".format(level_info[3])))

    def island_page_data_update(self) -> None:
        tasks = db.get_tasks()
        user_info = db.get_user_info()
        self.island_task_bar.setValue(0)
        self.island_page_top_update()

        # Обновляем переменные тасков
        for i in tasks:
            if user_info[2] >= i[4]:
                if hasattr(self, f"island_tasks_task_{i[0]}_uses_label"):
                    getattr(self, f"island_tasks_task_{i[0]}_uses_label", 0).setText(f"{i[6]}/{i[5]}")
            else:
                break

    def island_page_top_update(self):
        user_info = db.get_user_info()
        level_info = db.get_level_info(user_info[2])
        self.island_money_counter.setText(self.clicks_counter.text())
        self.island_skill_counter.setText(str(user_info[3]))
        self.island_level_title.setText(level_info[1])

    # Вывод задания в отдельный поток
    def start_task(self, tid: int) -> int:
        if self.task_active:
            return 0
        self.task_execution.start(lambda: self.task_exec(tid))

    def task_exec(self, tid: int) -> None:
        self.task_active = True
        task_info = db.get_task_info(tid)
        user_info = db.get_user_info()
        max_val = task_info[3] * 60
        self.island_task_bar.setRange(0, max_val)
        for i in range(max_val):
            self.island_task_bar.setValue(i + 1)
            time.sleep(0.01)
        self.island_task_bar.setValue(0)
        db.edit_user(skill=user_info[3]+task_info[2])
        db.plus_use_task(use=task_info[6]+1, task_id=tid)
        self.island_page_data_update()
        self.task_active = False

    def click(self) -> None:
        size = QSize(290, 290) if self.click_btn.iconSize() == QSize(300, 300) else QSize(300, 300)
        self.click_btn.setIconSize(size)
        self.last_click = time.time()
        click = int(self.clicks_counter.text()) + self.one_click
        self.clicks_counter.setText(str(click))
        self.update_rang()
        # Анимация прогрессбара
        if self.rank_bar_inprogress_anim.activeThreadCount() == 0:
            self.rank_bar_inprogress_anim.start(self.progress_bar_anim)

    def progress_bar_anim(self) -> None:
        while True:
            self.rank_bar.setStyleSheet(rank_progress_bar_styles_onclick)
            time.sleep(0.05)
            self.rank_bar.setStyleSheet(rank_progress_bar_styles)
            time.sleep(1)
            if time.time() - self.last_click > 3:
                break

    def level_upgrade(self) -> None:
        user_info = db.get_user_info()
        level_info = db.get_level_info(user_info[2])
        if int(self.clicks_counter.text()) >= level_info[2]:
            self.anim.start(self.animation_rank_up)
            db.edit_user(clicks_counter=int(self.clicks_counter.text()) - level_info[2], level=int(user_info[2]) + 1)
            self.level_upgrade_btn.setStyleSheet(self.level_upgrade_btn.styleSheet().replace(
                "background-color: rgba(5, 211, 234, 200);\n", "background-color: rgba(255, 255, 255, 100);\n"))
            self.main_page_data_update()

    def auto_save(self) -> None:
=======
        self.goal.setText(str(level_info[2]))
        self.rating.setText(self.clicks_counter.text())
        self.rang_bar.setValue(round((int(self.clicks_counter.text()) / int(self.goal.text()) * 100)))

    def click(self):
        click = int(self.clicks_counter.text())+self.one_click
        self.clicks_counter.setText(str(click))
<<<<<<< HEAD
=======
        self.update_rang()

    def auto_save(self):
>>>>>>> main
        print("Auto save ON | 10s")
        while True:
            # print("log | Обновление данных")
            db.save_user_data(self.one_click, self.clicks_counter.text())
<<<<<<< HEAD
            time.sleep(5)

    def update_rang(self) -> None:
        cc = self.clicks_counter.text()
        self.rating.setText(cc)
        # Изменяем прогрессбар
        self.rank_bar.setValue(int(cc)+self.one_click)

        if int(self.clicks_counter.text()) >= int(self.goal.text()):
            self.level_upgrade_btn.setStyleSheet(self.level_upgrade_btn.styleSheet().replace(
                "background-color: rgba(255, 255, 255, 100);\n", "background-color: rgba(5, 211, 234, 200);\n"))

class ErrorWindow(QWidget, Ui_Error):
    def __init__(self):
        super(ErrorWindow, self).__init__()
        self.setupUi(self)

        self.label_2.setStyleSheet(u"color: #fff;")
        self.pushButton.clicked.connect(self.close)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MinerWindow()
    window.show()

    sys.exit(app.exec())
=======
            time.sleep(10)

    def update_rang(self):
        cc = self.clicks_counter.text()
        self.rating.setText(cc)
        # Изменяем прогрессбар
        new_percent = round((int(cc) / int(self.goal.text()) * 100))
        if new_percent - self.rang_bar.value() >= 1:
            self.rang_bar.setValue(new_percent)

        if int(self.clicks_counter.text()) >= int(self.goal.text()):
            # Загорается кнопка и можно улучшить уровень
            pass
>>>>>>> 028a1b2 (added assets, ranks system, new GUI)


app = QApplication(sys.argv)

window = MinerWindow()
asyncio.run(window.data_update())
window.show()

app.exec()
>>>>>>> main
