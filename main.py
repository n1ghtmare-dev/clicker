from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt
from ui_main import Ui_MainWindow
import sys


class MinerWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MinerWindow, self).__init__()
        self.setupUi(self)
        # Объявляем переменные с нормальными названиями
        self.click_btn = self.pushButton
        self.clicks_counter = self.label_2

        # Объявляем события
        self.click_btn.clicked.connect(self.click)

    def click(self):
        one_click = 1
        self.clicks_counter.setText(str(int(self.clicks_counter.text())+one_click))


app = QApplication(sys.argv)

window = MinerWindow()
window.show()

app.exec()