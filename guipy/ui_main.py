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
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import images_rc

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
        MainWindow.setStyleSheet(u"background-image: url(:/images/winterbg.png)")
        MainWindow.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: #fff;")
        self.verticalLayout_6 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.stackedWidget.setStyleSheet(u"background: rgba(0,0,0,0);")
        self.main_page = QWidget()
        self.main_page.setObjectName(u"main_page")
        self.horizontalLayout = QHBoxLayout(self.main_page)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(self.main_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(200, 500))
        self.frame_2.setMaximumSize(QSize(16777215, 600))
        self.frame_2.setStyleSheet(u"background: none;")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 100))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.skin_btn = QPushButton(self.frame_4)
        self.skin_btn.setObjectName(u"skin_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.skin_btn.sizePolicy().hasHeightForWidth())
        self.skin_btn.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"a_Concepto"])
        font.setPointSize(12)
        self.skin_btn.setFont(font)
        self.skin_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.skin_btn.setStyleSheet(u"border: none;\n"
"background: none;\n"
"background-color: rgba(255, 255, 255, 100);\n"
"border-radius: 8px;\n"
"padding: 10px 25px;\n"
"")

        self.horizontalLayout_4.addWidget(self.skin_btn, 0, Qt.AlignmentFlag.AlignVCenter)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addWidget(self.frame_4, 0, Qt.AlignmentFlag.AlignVCenter)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setEnabled(True)
        self.label_5.setMaximumSize(QSize(250, 350))
        self.label_5.setStyleSheet(u"background: none;")
        self.label_5.setPixmap(QPixmap(u":/images/humster.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_5)

        self.verticalSpacer = QSpacerItem(20, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame_2)

        self.mainframe = QFrame(self.main_page)
        self.mainframe.setObjectName(u"mainframe")
        self.mainframe.setMinimumSize(QSize(300, 0))
        self.mainframe.setMaximumSize(QSize(400, 550))
        self.mainframe.setStyleSheet(u"background: none;")
        self.verticalLayout_3 = QVBoxLayout(self.mainframe)
        self.verticalLayout_3.setSpacing(100)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.counts = QFrame(self.mainframe)
        self.counts.setObjectName(u"counts")
        self.counts.setMaximumSize(QSize(16777215, 200))
        font1 = QFont()
        font1.setFamilies([u"a_Concepto"])
        self.counts.setFont(font1)
        self.verticalLayout = QVBoxLayout(self.counts)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 1)
        self.label = QLabel(self.counts)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"a_Concepto"])
        font2.setPointSize(42)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"background: none;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.clicks_counter = QLabel(self.counts)
        self.clicks_counter.setObjectName(u"clicks_counter")
        self.clicks_counter.setFont(font2)
        self.clicks_counter.setStyleSheet(u"\n"
"background: none;")
        self.clicks_counter.setTextFormat(Qt.TextFormat.AutoText)
        self.clicks_counter.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.clicks_counter.setWordWrap(False)

        self.verticalLayout.addWidget(self.clicks_counter)


        self.verticalLayout_3.addWidget(self.counts)

        self.click_btn = QPushButton(self.mainframe)
        self.click_btn.setObjectName(u"click_btn")
        self.click_btn.setEnabled(True)
        self.click_btn.setMinimumSize(QSize(0, 220))
        self.click_btn.setMaximumSize(QSize(99999, 220))
        font3 = QFont()
        font3.setPointSize(30)
        self.click_btn.setFont(font3)
        self.click_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.click_btn.setAutoFillBackground(False)
        self.click_btn.setStyleSheet(u"border: 0;\n"
"background: none;")
        icon = QIcon()
        icon.addFile(u":/images/click-huobi.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.click_btn.setIcon(icon)
        self.click_btn.setIconSize(QSize(300, 300))
        self.click_btn.setCheckable(False)
        self.click_btn.setAutoRepeat(False)
        self.click_btn.setAutoExclusive(False)
        self.click_btn.setAutoDefault(False)

        self.verticalLayout_3.addWidget(self.click_btn)

        self.menu_btn = QPushButton(self.mainframe)
        self.menu_btn.setObjectName(u"menu_btn")
        font4 = QFont()
        font4.setFamilies([u"a_Concepto"])
        font4.setPointSize(22)
        self.menu_btn.setFont(font4)
        self.menu_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.menu_btn.setStyleSheet(u"border: none;\n"
"background: none;\n"
"background-color: rgb(59, 59, 59);\n"
"border-radius: 8px;\n"
"padding: 10px 20px;")

        self.verticalLayout_3.addWidget(self.menu_btn, 0, Qt.AlignmentFlag.AlignVCenter)


        self.horizontalLayout.addWidget(self.mainframe)

        self.frame = QFrame(self.main_page)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(200, 300))
        self.frame.setStyleSheet(u"background: none;")
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.rang = QFrame(self.frame)
        self.rang.setObjectName(u"rang")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.rang.sizePolicy().hasHeightForWidth())
        self.rang.setSizePolicy(sizePolicy1)
        self.rang.setMaximumSize(QSize(16777215, 400))
        self.verticalLayout_2 = QVBoxLayout(self.rang)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_3 = QFrame(self.rang)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 100))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.rank_img = QLabel(self.frame_3)
        self.rank_img.setObjectName(u"rank_img")
        self.rank_img.setMinimumSize(QSize(150, 150))
        self.rank_img.setMaximumSize(QSize(150, 150))
        self.rank_img.setPixmap(QPixmap(u":/images/ranks/Shield/Wood/shield-wood-1.png"))
        self.rank_img.setScaledContents(True)
        self.rank_img.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.rank_img)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.label_3 = QLabel(self.rang)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 80))
        self.label_3.setFont(font4)
        self.label_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_3.setStyleSheet(u"text-shadow: -1px 2px 6px rgba(0, 0, 0, 0.5);")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.rank_bar = QProgressBar(self.rang)
        self.rank_bar.setObjectName(u"rank_bar")
        self.rank_bar.setMinimumSize(QSize(200, 30))
        self.rank_bar.setMaximumSize(QSize(300, 16777215))
        font5 = QFont()
        font5.setStyleStrategy(QFont.PreferAntialias)
        self.rank_bar.setFont(font5)
        self.rank_bar.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.rank_bar.setAutoFillBackground(False)
        self.rank_bar.setStyleSheet(u"QProgressBar{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	border-radius: 15px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(2, 97, 123, 255), stop:1 rgba(4, 177, 225, 255))\n"
"}")
        self.rank_bar.setValue(22)
        self.rank_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.rank_bar.setTextVisible(False)
        self.rank_bar.setFormat(u"%p%")

        self.verticalLayout_2.addWidget(self.rank_bar)

        self.rating = QLabel(self.rang)
        self.rating.setObjectName(u"rating")
        font6 = QFont()
        font6.setFamilies([u"a_Concepto"])
        font6.setPointSize(18)
        self.rating.setFont(font6)
        self.rating.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.rating)

        self.goal = QLabel(self.rang)
        self.goal.setObjectName(u"goal")
        self.goal.setFont(font6)
        self.goal.setStyleSheet(u"text-shadow: -1px 2px 6px rgba(0, 0, 0, 0.5);")
        self.goal.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.goal)

        self.level_upgrade_btn = QPushButton(self.rang)
        self.level_upgrade_btn.setObjectName(u"level_upgrade_btn")
        font7 = QFont()
        font7.setFamilies([u"a_Concepto"])
        font7.setPointSize(14)
        self.level_upgrade_btn.setFont(font7)
        self.level_upgrade_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.level_upgrade_btn.setStyleSheet(u"border: none;\n"
"background-color: rgba(255, 255, 255, 100);\n"
"border-radius: 8px;\n"
"padding: 10px 20px;")

        self.verticalLayout_2.addWidget(self.level_upgrade_btn)


        self.verticalLayout_4.addWidget(self.rang, 0, Qt.AlignmentFlag.AlignVCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 200, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)


        self.horizontalLayout.addWidget(self.frame)

        self.stackedWidget.addWidget(self.main_page)
        self.island_page = QWidget()
        self.island_page.setObjectName(u"island_page")
        self.frame_14 = QFrame(self.island_page)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setEnabled(True)
        self.frame_14.setGeometry(QRect(400, 150, 161, 191))
        self.frame_14.setStyleSheet(u"background: #403C43;\n"
"border-radius: 5px;")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_14)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.pushButton_6 = QPushButton(self.frame_14)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_6.setStyleSheet(u"color: #fff;")

        self.verticalLayout_7.addWidget(self.pushButton_6)

        self.frame_18 = QFrame(self.frame_14)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setEnabled(True)
        self.frame_18.setMinimumSize(QSize(0, 30))
        self.frame_18.setMaximumSize(QSize(16777215, 20))
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_12)

        self.label_21 = QLabel(self.frame_18)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(0, 0))
        self.label_21.setMaximumSize(QSize(150, 16777215))
        font8 = QFont()
        font8.setFamilies([u"Data Trash"])
        font8.setPointSize(8)
        self.label_21.setFont(font8)
        self.label_21.setStyleSheet(u"color: white;\n"
"background: none;")

        self.horizontalLayout_11.addWidget(self.label_21)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_13)


        self.verticalLayout_7.addWidget(self.frame_18)

        self.label_22 = QLabel(self.frame_14)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setEnabled(True)
        font9 = QFont()
        font9.setFamilies([u"Intro Black"])
        font9.setPointSize(8)
        font9.setBold(True)
        self.label_22.setFont(font9)
        self.label_22.setStyleSheet(u"color: white;\n"
"background: none;")
        self.label_22.setScaledContents(False)
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_22)

        self.frame_19 = QFrame(self.frame_14)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setEnabled(True)
        self.frame_19.setMinimumSize(QSize(0, 63))
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_8 = QLabel(self.frame_19)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(50, 50))
        self.label_8.setMaximumSize(QSize(50, 50))
        self.label_8.setPixmap(QPixmap(u":/images/gems/Gemstone_Icon_Kit/1.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_8.setWordWrap(False)

        self.horizontalLayout_14.addWidget(self.label_8)


        self.verticalLayout_7.addWidget(self.frame_19, 0, Qt.AlignmentFlag.AlignVCenter)

        self.frame_20 = QFrame(self.frame_14)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setStyleSheet(u"padding: 0;\n"
"margin: 0;")
        self.frame_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_16)

        self.label_14 = QLabel(self.frame_20)
        self.label_14.setObjectName(u"label_14")
        font10 = QFont()
        font10.setFamilies([u"Intro Black"])
        self.label_14.setFont(font10)
        self.label_14.setStyleSheet(u"color: #fff;")

        self.horizontalLayout_15.addWidget(self.label_14)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_17)


        self.verticalLayout_7.addWidget(self.frame_20)

        self.frame_5 = QFrame(self.island_page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(230, 60, 650, 80))
        self.frame_5.setMinimumSize(QSize(650, 80))
        self.frame_5.setMaximumSize(QSize(650, 80))
        self.frame_5.setStyleSheet(u"background: #403C43;\n"
"border-radius: 5px;")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.progressBar = QProgressBar(self.frame_5)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy2)
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	background: none;\n"
"	background-color: #686868;\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	background-color: #2AED7B;\n"
"	border-radius: 4px;\n"
"}")
        self.progressBar.setValue(28)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_8.addWidget(self.progressBar)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.label_2 = QLabel(self.frame_7)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font10)
        self.label_2.setStyleSheet(u"color: #fff;")

        self.horizontalLayout_6.addWidget(self.label_2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)


        self.verticalLayout_8.addWidget(self.frame_7)

        self.frame_6 = QFrame(self.island_page)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(0, 0, 221, 581))
        self.frame_6.setMinimumSize(QSize(221, 581))
        self.frame_6.setStyleSheet(u"background: #403C43;\n"
"border-radius: 5px;")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_10 = QFrame(self.frame_6)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pushButton = QPushButton(self.frame_10)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(False)
        font11 = QFont()
        font11.setFamilies([u"Disket Mono"])
        font11.setPointSize(10)
        font11.setBold(True)
        self.pushButton.setFont(font11)
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background: none;\n"
"border: none;\n"
"color: #2AED7B;")

        self.horizontalLayout_8.addWidget(self.pushButton)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)


        self.verticalLayout_11.addWidget(self.frame_10)

        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pushButton_2 = QPushButton(self.frame_9)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setFont(font11)
        self.pushButton_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"background: none;\n"
"border: none;\n"
"color: white;")

        self.horizontalLayout_9.addWidget(self.pushButton_2)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_8)


        self.verticalLayout_11.addWidget(self.frame_9)

        self.frame_11 = QFrame(self.frame_6)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.pushButton_3 = QPushButton(self.frame_11)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font11)
        self.pushButton_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"background: none;\n"
"border: none;\n"
"color: white;")

        self.horizontalLayout_16.addWidget(self.pushButton_3)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_7)


        self.verticalLayout_11.addWidget(self.frame_11)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_4)

        self.close_island_btn = QPushButton(self.frame_6)
        self.close_island_btn.setObjectName(u"close_island_btn")
        font12 = QFont()
        font12.setFamilies([u"a_FuturicaBlack"])
        font12.setPointSize(12)
        font12.setBold(False)
        self.close_island_btn.setFont(font12)
        self.close_island_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.close_island_btn.setStyleSheet(u"padding: 8px 12px;\n"
"border-radius: 5px;\n"
"background-color: rgb(74, 153, 213);")

        self.verticalLayout_11.addWidget(self.close_island_btn)

        self.frame_8 = QFrame(self.island_page)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(230, 0, 650, 53))
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy3)
        self.frame_8.setMinimumSize(QSize(650, 0))
        self.frame_8.setMaximumSize(QSize(650, 16777215))
        self.frame_8.setStyleSheet(u"background: #403C43;\n"
"border-radius: 5px;")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.money_count_frame = QFrame(self.frame_8)
        self.money_count_frame.setObjectName(u"money_count_frame")
        self.money_count_frame.setEnabled(True)
        self.money_count_frame.setStyleSheet(u"background:none;\n"
"")
        self.horizontalLayout_2 = QHBoxLayout(self.money_count_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_13 = QLabel(self.money_count_frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setEnabled(False)
        font13 = QFont()
        font13.setFamilies([u"Code Pro Bold"])
        font13.setPointSize(10)
        self.label_13.setFont(font13)
        self.label_13.setStyleSheet(u"color: white;\n"
"background: none;")

        self.horizontalLayout_2.addWidget(self.label_13)

        self.label_9 = QLabel(self.money_count_frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font13)
        self.label_9.setStyleSheet(u"color: white;\n"
"background: none;")

        self.horizontalLayout_2.addWidget(self.label_9)


        self.horizontalLayout_5.addWidget(self.money_count_frame)

        self.skill_count_frame = QFrame(self.frame_8)
        self.skill_count_frame.setObjectName(u"skill_count_frame")
        self.skill_count_frame.setStyleSheet(u"background: none;")
        self.horizontalLayout_7 = QHBoxLayout(self.skill_count_frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_10 = QLabel(self.skill_count_frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setEnabled(False)
        self.label_10.setFont(font13)
        self.label_10.setStyleSheet(u"color: white;\n"
"background: none;")

        self.horizontalLayout_7.addWidget(self.label_10)

        self.label_11 = QLabel(self.skill_count_frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font13)
        self.label_11.setStyleSheet(u"color: white;\n"
"background: none;")

        self.horizontalLayout_7.addWidget(self.label_11)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)


        self.horizontalLayout_5.addWidget(self.skill_count_frame)

        self.label_12 = QLabel(self.frame_8)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setEnabled(False)
        self.label_12.setFont(font13)
        self.label_12.setStyleSheet(u"color: white;\n"
"background: none;")

        self.horizontalLayout_5.addWidget(self.label_12)

        self.frame_13 = QFrame(self.island_page)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setEnabled(True)
        self.frame_13.setGeometry(QRect(230, 150, 161, 191))
        self.frame_13.setStyleSheet(u"background: #403C43;\n"
"border-radius: 5px;")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_13)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.pushButton_5 = QPushButton(self.frame_13)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"color: #fff;")

        self.verticalLayout_10.addWidget(self.pushButton_5)

        self.frame_15 = QFrame(self.frame_13)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setEnabled(True)
        self.frame_15.setMinimumSize(QSize(0, 30))
        self.frame_15.setMaximumSize(QSize(16777215, 20))
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_10)

        self.label_19 = QLabel(self.frame_15)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(0, 0))
        self.label_19.setMaximumSize(QSize(150, 16777215))
        self.label_19.setFont(font8)
        self.label_19.setStyleSheet(u"color: white;\n"
"background: none;")

        self.horizontalLayout_10.addWidget(self.label_19)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_11)


        self.verticalLayout_10.addWidget(self.frame_15)

        self.label_20 = QLabel(self.frame_13)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setEnabled(True)
        self.label_20.setFont(font9)
        self.label_20.setStyleSheet(u"color: white;\n"
"background: none;")
        self.label_20.setScaledContents(False)
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_20)

        self.frame_16 = QFrame(self.frame_13)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setEnabled(True)
        self.frame_16.setMinimumSize(QSize(0, 63))
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_6 = QLabel(self.frame_16)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(50, 50))
        self.label_6.setMaximumSize(QSize(50, 50))
        self.label_6.setPixmap(QPixmap(u":/images/gems/Gemstone_Icon_Kit/1.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_6.setWordWrap(False)

        self.horizontalLayout_12.addWidget(self.label_6)


        self.verticalLayout_10.addWidget(self.frame_16, 0, Qt.AlignmentFlag.AlignVCenter)

        self.frame_17 = QFrame(self.frame_13)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"padding: 0;\n"
"margin: 0;")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_14)

        self.label_7 = QLabel(self.frame_17)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font10)
        self.label_7.setStyleSheet(u"color: #fff;")

        self.horizontalLayout_13.addWidget(self.label_7)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_15)


        self.verticalLayout_10.addWidget(self.frame_17)

        self.stackedWidget.addWidget(self.island_page)

        self.verticalLayout_6.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.click_btn.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Crypto Miner", None))
        self.skin_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0438\u043d", None))
        self.label_5.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041c\u041e\u041d\u0415\u0422\u042b", None))
        self.clicks_counter.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.click_btn.setText("")
        self.menu_btn.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0410\u0413\u0410\u0417\u0418\u041d", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0420\u041e\u0412\u0415\u041d\u042c 1", None))
#if QT_CONFIG(accessibility)
        self.rank_bar.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.rating.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.goal.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.level_upgrade_btn.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043b\u0443\u0447\u0448\u0438\u0442\u044c", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u044b\u0432\u0430\u0442\u044c", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u044b\u0447\u043d\u0430\u044f \u0448\u0430\u0445\u0442\u0430", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"7 \u043e\u0447\u043a. \u043d\u0430\u0432\u044b\u043a\u0430 / 3\u0441\u0435\u043a.", None))
        self.label_8.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"0/550", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0434\u0435\u0441\u044c \u0431\u0443\u0434\u0435\u0442 \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0442\u044c\u0441\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0437\u0430\u0434\u0430\u043d\u0438\u0438", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0421\u0422\u0420\u041e\u0412 \u0417\u0410\u0414\u0410\u041d\u0418\u0419", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0410\u0413\u0410\u0417\u0418\u041d", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u041e\u0420\u0422\u0424\u0415\u041b\u042c", None))
        self.close_island_btn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0411\u0420\u0410\u0422\u041d\u041e", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u041c\u041e\u041d\u0415\u0422\u042b", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0410\u0412\u042b\u041a", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0410\u0427\u0418\u041d\u0410\u042e\u0429\u0418\u0419", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u044b\u0432\u0430\u0442\u044c", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u044b\u0447\u043d\u0430\u044f \u0448\u0430\u0445\u0442\u0430", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"7 \u043e\u0447\u043a. \u043d\u0430\u0432\u044b\u043a\u0430 / 3\u0441\u0435\u043a.", None))
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"0/550", None))
    # retranslateUi

