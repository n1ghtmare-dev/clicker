# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(900, 600)
        MainWindow.setMinimumSize(QSize(900, 600))
        MainWindow.setMaximumSize(QSize(900, 600))
        MainWindow.setBaseSize(QSize(900, 600))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.142, y1:0, x2:0.857955, y2:1, stop:0 rgba(35, 14, 54, 255), stop:1 rgba(102, 40, 156, 255));")
        MainWindow.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: #fff;")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(200, 500))
        self.frame_2.setMaximumSize(QSize(16777215, 500))
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setEnabled(True)
        self.label_5.setGeometry(QRect(0, 20, 301, 451))
        self.label_5.setPixmap(QPixmap("images/Group 5.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.frame_2)

        self.mainframe = QFrame(self.centralwidget)
        self.mainframe.setObjectName(u"mainframe")
        self.mainframe.setMinimumSize(QSize(300, 0))
        self.mainframe.setMaximumSize(QSize(400, 550))
        self.verticalLayout_3 = QVBoxLayout(self.mainframe)
        self.verticalLayout_3.setSpacing(100)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.counts = QFrame(self.mainframe)
        self.counts.setObjectName(u"counts")
        self.counts.setMaximumSize(QSize(16777215, 200))
        font = QFont()
        font.setFamilies([u"a_Concepto"])
        self.counts.setFont(font)
        self.verticalLayout = QVBoxLayout(self.counts)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 1)
        self.label = QLabel(self.counts)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"a_Concepto"])
        font1.setPointSize(42)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.counts)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setTextFormat(Qt.TextFormat.AutoText)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(False)

        self.verticalLayout.addWidget(self.label_2)


        self.verticalLayout_3.addWidget(self.counts)

        self.pushButton = QPushButton(self.mainframe)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        self.pushButton.setMinimumSize(QSize(0, 220))
        self.pushButton.setMaximumSize(QSize(99999, 220))
        font2 = QFont()
        font2.setPointSize(30)
        self.pushButton.setFont(font2)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(u"border: 0;")
        icon = QIcon()
        icon.addFile("images/Huobi BTC (HBTC) 01.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(300, 300))
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setAutoDefault(False)

        self.verticalLayout_3.addWidget(self.pushButton, 0, Qt.AlignmentFlag.AlignVCenter)

        self.pushButton_2 = QPushButton(self.mainframe)
        self.pushButton_2.setObjectName(u"pushButton_2")
        font3 = QFont()
        font3.setFamilies([u"a_Concepto"])
        font3.setPointSize(22)
        self.pushButton_2.setFont(font3)
        self.pushButton_2.setStyleSheet(u"border: none;")

        self.verticalLayout_3.addWidget(self.pushButton_2)


        self.horizontalLayout_2.addWidget(self.mainframe, 0, Qt.AlignmentFlag.AlignVCenter)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(200, 0))
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.rang = QFrame(self.frame)
        self.rang.setObjectName(u"rang")
        self.rang.setMaximumSize(QSize(16777215, 200))
        self.verticalLayout_2 = QVBoxLayout(self.rang)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.rang)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.line = QFrame(self.rang)
        self.line.setObjectName(u"line")
        font4 = QFont()
        font4.setPointSize(30)
        font4.setBold(True)
        self.line.setFont(font4)
        self.line.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.line.setStyleSheet(u"")
        self.line.setFrameShadow(QFrame.Shadow.Plain)
        self.line.setLineWidth(10)
        self.line.setMidLineWidth(5)
        self.line.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_2.addWidget(self.line)

        self.label_4 = QLabel(self.rang)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_4)


        self.verticalLayout_4.addWidget(self.rang)

        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(200, 200))
        self.widget.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout_4.addWidget(self.widget)


        self.horizontalLayout_2.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pushButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Crypto Miner", None))
        self.label_5.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"COUNT", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0410\u0413\u0410\u0417\u0418\u041d", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"RANG", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"253/1000", None))
    # retranslateUi

