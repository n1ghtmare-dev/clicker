from PySide6.QtWidgets import QApplication, QMainWindow
<<<<<<< HEAD
from PySide6.QtCore import Qt
=======
from PySide6.QtCore import QThreadPool
<<<<<<< HEAD
from PySide6.QtGui import QPixmap
>>>>>>> 028a1b2 (added assets, ranks system, new GUI)
=======
>>>>>>> parent of 028a1b2 (added assets, ranks system, new GUI)
from ui_main import Ui_MainWindow
from database import Database
import asyncio
import sys

db = Database('database.db')

class MinerWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MinerWindow, self).__init__()
        self.setupUi(self)

<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> parent of 028a1b2 (added assets, ranks system, new GUI)
        # Объявляем переменные с нормальными названиями
        self.click_btn = self.pushButton
        self.clicks_counter = self.label_2
        self.rang_bar = self.progressBar
<<<<<<< HEAD

        # Объявляем события
        self.click_btn.clicked.connect(self.click)

    # Обновляем переменные
    async def data_update(self):
        self.one_click = await db.get_click()
        print(self.one_click)
=======
=======
        self.rating = self.label_6
        self.goal = self.label_4

>>>>>>> parent of 028a1b2 (added assets, ranks system, new GUI)
        # Объявляем переменные, которые обновятся
        self.one_click = 1

        self.data_update()

        # Потоки
        self.auto_save_thread = QThreadPool()
        self.auto_save_thread.start(self.auto_save)

        # Объявляем события
        self.click_btn.clicked.connect(self.click)
        self.pushButton_3.clicked.connect(self.close)


    # Обновляем переменные
    def data_update(self):
        user_info = db.get_user_info()

        self.one_click = user_info[0]
        self.clicks_counter.setText(str(user_info[1]))

        # Level
        level_info = db.get_level_info(user_info[2])
        self.goal.setText(str(level_info[2]))
        self.rating.setText(self.clicks_counter.text())
<<<<<<< HEAD
        self.rank_bar.setValue(round((int(self.clicks_counter.text()) / int(self.goal.text()) * 100)))
        self.rank_img.setPixmap(QPixmap(u":/images/ranks/Shield/{}".format(level_info[3])))
>>>>>>> 028a1b2 (added assets, ranks system, new GUI)
=======
        self.rang_bar.setValue(round((int(self.clicks_counter.text()) / int(self.goal.text()) * 100)))
>>>>>>> parent of 028a1b2 (added assets, ranks system, new GUI)

    def click(self):
        click = int(self.clicks_counter.text())+self.one_click
        self.clicks_counter.setText(str(click))
<<<<<<< HEAD
=======
        self.update_rang()

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