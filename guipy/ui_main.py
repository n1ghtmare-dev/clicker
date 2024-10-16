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
<<<<<<< HEAD
    QMainWindow, QProgressBar, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)
import images_rc
=======
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
>>>>>>> main

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
<<<<<<< HEAD
        MainWindow.setStyleSheet(u"background-image: url(:/images/winterbg.png);")
        MainWindow.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: #fff;\n"
"margin: 0;")
        self.verticalLayout_9 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
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

=======
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
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
>>>>>>> main
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setEnabled(True)
        self.label_5.setMaximumSize(QSize(250, 350))
<<<<<<< HEAD
        self.label_5.setStyleSheet(u"background: none;")
        self.label_5.setPixmap(QPixmap(u":/images/humster.png"))
=======
        self.label_5.setPixmap(QPixmap(u"../images/Group 5.png"))
>>>>>>> main
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_5)

<<<<<<< HEAD
        self.verticalSpacer = QSpacerItem(20, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame_2)

        self.mainframe = QFrame(self.main_page)
        self.mainframe.setObjectName(u"mainframe")
        self.mainframe.setMinimumSize(QSize(322, 0))
        self.mainframe.setMaximumSize(QSize(322, 550))
        self.mainframe.setStyleSheet(u"background: none;")
        self.verticalLayout_3 = QVBoxLayout(self.mainframe)
        self.verticalLayout_3.setSpacing(50)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.counts = QFrame(self.mainframe)
        self.counts.setObjectName(u"counts")
        self.counts.setMaximumSize(QSize(16777215, 200))
        font1 = QFont()
        font1.setFamilies([u"a_Concepto"])
        self.counts.setFont(font1)
=======

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
>>>>>>> main
        self.verticalLayout = QVBoxLayout(self.counts)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 1)
        self.label = QLabel(self.counts)
        self.label.setObjectName(u"label")
<<<<<<< HEAD
        font2 = QFont()
        font2.setFamilies([u"a_Concepto"])
        font2.setPointSize(42)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"background: none;")
=======
        font1 = QFont()
        font1.setFamilies([u"a_Concepto"])
        font1.setPointSize(42)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"text-shadow: -1px 2px 6px rgba(0, 0, 0, 0.5);")
>>>>>>> main
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

<<<<<<< HEAD
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
        self.click_btn.setStyleSheet(u"QPushButton{\n"
"	border: 0;\n"
"	background: none;\n"
"}\n"
"\n"
"QPushButton:pressed icon{\n"
"	color: #fff;\n"
"}")
        self.click_btn.setText(u"")
        icon = QIcon()
        icon.addFile(u":/images/click-huobi.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        icon.addFile(u":/images/click-huobi.png", QSize(), QIcon.Mode.Disabled, QIcon.State.On)
        icon.addFile(u":/images/click-huobi.png", QSize(), QIcon.Mode.Active, QIcon.State.On)
        icon.addFile(u":/images/click-huobi.png", QSize(), QIcon.Mode.Selected, QIcon.State.On)
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
=======
        self.label_2 = QLabel(self.counts)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"text-shadow: -1px 2px 6px rgba(0, 0, 0, 0.5);")
        self.label_2.setTextFormat(Qt.TextFormat.AutoText)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(False)

        self.verticalLayout.addWidget(self.label_2)


        self.verticalLayout_3.addWidget(self.counts, 0, Qt.AlignmentFlag.AlignVCenter)

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
        icon.addFile(u"../images/Huobi BTC (HBTC) 01.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
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
        self.pushButton_2.setStyleSheet(u"border: none;\n"
"text-shadow: -1px 2px 6px rgba(0, 0, 0, 0.5);")

        self.verticalLayout_3.addWidget(self.pushButton_2)


        self.horizontalLayout_2.addWidget(self.mainframe, 0, Qt.AlignmentFlag.AlignVCenter)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(200, 0))
>>>>>>> main
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.rang = QFrame(self.frame)
        self.rang.setObjectName(u"rang")
<<<<<<< HEAD
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
        self.frame_3.setEnabled(True)
        self.frame_3.setMinimumSize(QSize(0, 130))
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.rank_img = QLabel(self.frame_3)
        self.rank_img.setObjectName(u"rank_img")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.rank_img.sizePolicy().hasHeightForWidth())
        self.rank_img.setSizePolicy(sizePolicy2)
        self.rank_img.setMinimumSize(QSize(150, 150))
        self.rank_img.setMaximumSize(QSize(150, 150))
        self.rank_img.setPixmap(QPixmap(u":/images/ranks/Shield/Wood/shield-wood-1.png"))
        self.rank_img.setScaledContents(True)
        self.rank_img.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.rank_img)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.level_number = QLabel(self.rang)
        self.level_number.setObjectName(u"level_number")
        self.level_number.setMaximumSize(QSize(16777215, 80))
        self.level_number.setFont(font4)
        self.level_number.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.level_number.setStyleSheet(u"text-shadow: -1px 2px 6px rgba(0, 0, 0, 0.5);")
        self.level_number.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.level_number)

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
"	border-radius: 10px;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	border-radius: 10px;\n"
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


        self.verticalLayout_4.addWidget(self.rang, 0, Qt.AlignmentFlag.AlignTop)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)


        self.horizontalLayout.addWidget(self.frame)

        self.stackedWidget.addWidget(self.main_page)
        self.island_page = QWidget()
        self.island_page.setObjectName(u"island_page")
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
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.open_island_btn = QPushButton(self.frame_10)
        self.open_island_btn.setObjectName(u"open_island_btn")
        font8 = QFont()
        font8.setFamilies([u"Disket Mono"])
        font8.setPointSize(10)
        font8.setBold(True)
        self.open_island_btn.setFont(font8)
        self.open_island_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.open_island_btn.setMouseTracking(False)
        self.open_island_btn.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.open_island_btn)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)

        self.menu_bar_img1 = QLabel(self.frame_10)
        self.menu_bar_img1.setObjectName(u"menu_bar_img1")
        self.menu_bar_img1.setEnabled(True)
        self.menu_bar_img1.setMinimumSize(QSize(25, 25))
        self.menu_bar_img1.setMaximumSize(QSize(25, 25))
        self.menu_bar_img1.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.menu_bar_img1.setAutoFillBackground(False)
        self.menu_bar_img1.setPixmap(QPixmap(u":/images/gems/Gemstone_Icon_Kit/18.png"))
        self.menu_bar_img1.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.menu_bar_img1)


        self.verticalLayout_11.addWidget(self.frame_10)

        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.open_shop_btn = QPushButton(self.frame_9)
        self.open_shop_btn.setObjectName(u"open_shop_btn")
        self.open_shop_btn.setFont(font8)
        self.open_shop_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.open_shop_btn.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.open_shop_btn)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_8)

        self.menu_bar_img2 = QLabel(self.frame_9)
        self.menu_bar_img2.setObjectName(u"menu_bar_img2")
        self.menu_bar_img2.setMinimumSize(QSize(25, 25))
        self.menu_bar_img2.setMaximumSize(QSize(25, 25))
        self.menu_bar_img2.setPixmap(QPixmap(u":/images/gems/Gemstone_Icon_Kit/21.png"))
        self.menu_bar_img2.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.menu_bar_img2)


        self.verticalLayout_11.addWidget(self.frame_9)

        self.frame_11 = QFrame(self.frame_6)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.open_backpack_btn = QPushButton(self.frame_11)
        self.open_backpack_btn.setObjectName(u"open_backpack_btn")
        self.open_backpack_btn.setFont(font8)
        self.open_backpack_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_16.addWidget(self.open_backpack_btn)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_7)

        self.menu_bar_img3 = QLabel(self.frame_11)
        self.menu_bar_img3.setObjectName(u"menu_bar_img3")
        self.menu_bar_img3.setMinimumSize(QSize(25, 25))
        self.menu_bar_img3.setMaximumSize(QSize(25, 25))
        self.menu_bar_img3.setPixmap(QPixmap(u":/images/gems/Gemstone_Icon_Kit/60.png"))
        self.menu_bar_img3.setScaledContents(True)

        self.horizontalLayout_16.addWidget(self.menu_bar_img3)


        self.verticalLayout_11.addWidget(self.frame_11)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_4)

        self.close_island_btn = QPushButton(self.frame_6)
        self.close_island_btn.setObjectName(u"close_island_btn")
        font9 = QFont()
        font9.setFamilies([u"a_FuturicaBlack"])
        font9.setPointSize(12)
        font9.setBold(False)
        self.close_island_btn.setFont(font9)
        self.close_island_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.close_island_btn.setStyleSheet(u"padding: 8px 12px;\n"
"border-radius: 5px;\n"
"background-color: rgb(74, 153, 213);")

        self.verticalLayout_11.addWidget(self.close_island_btn)

        self.frame_8 = QFrame(self.island_page)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(230, 0, 640, 50))
        sizePolicy2.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy2)
        self.frame_8.setMinimumSize(QSize(640, 0))
        self.frame_8.setMaximumSize(QSize(640, 50))
        self.frame_8.setStyleSheet(u"background: #403C43;\n"
"border-radius: 5px;")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.money_count_frame = QFrame(self.frame_8)
        self.money_count_frame.setObjectName(u"money_count_frame")
        self.money_count_frame.setEnabled(True)
        self.money_count_frame.setStyleSheet(u"background:none;\n"
"")
        self.horizontalLayout_2 = QHBoxLayout(self.money_count_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.label_13 = QLabel(self.money_count_frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setEnabled(False)
        font10 = QFont()
        font10.setFamilies([u"Code Pro Bold"])
        font10.setPointSize(10)
        self.label_13.setFont(font10)
        self.label_13.setStyleSheet(u"color: white;\n"
"background: none;")

        self.horizontalLayout_2.addWidget(self.label_13)

        self.island_money_counter = QLabel(self.money_count_frame)
        self.island_money_counter.setObjectName(u"island_money_counter")
        self.island_money_counter.setFont(font10)
        self.island_money_counter.setStyleSheet(u"color: white;\n"
"background: none;")

        self.horizontalLayout_2.addWidget(self.island_money_counter)


        self.horizontalLayout_5.addWidget(self.money_count_frame)

        self.skill_count_frame = QFrame(self.frame_8)
        self.skill_count_frame.setObjectName(u"skill_count_frame")
        self.skill_count_frame.setStyleSheet(u"background: none;")
        self.horizontalLayout_7 = QHBoxLayout(self.skill_count_frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.label_10 = QLabel(self.skill_count_frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setEnabled(False)
        self.label_10.setFont(font10)
        self.label_10.setStyleSheet(u"color: white;\n"
"background: none;")

        self.horizontalLayout_7.addWidget(self.label_10)

        self.island_skill_counter = QLabel(self.skill_count_frame)
        self.island_skill_counter.setObjectName(u"island_skill_counter")
        self.island_skill_counter.setFont(font10)
        self.island_skill_counter.setStyleSheet(u"color: white;\n"
"background: none;")

        self.horizontalLayout_7.addWidget(self.island_skill_counter)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)


        self.horizontalLayout_5.addWidget(self.skill_count_frame)

        self.island_level_title = QLabel(self.frame_8)
        self.island_level_title.setObjectName(u"island_level_title")
        self.island_level_title.setEnabled(False)
        self.island_level_title.setFont(font10)
        self.island_level_title.setStyleSheet(u"color: white;\n"
"background: none;")

        self.horizontalLayout_5.addWidget(self.island_level_title)

        self.stackedWidget_2 = QStackedWidget(self.island_page)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setGeometry(QRect(222, 50, 660, 531))
        self.stackedWidget_2.setMinimumSize(QSize(660, 0))
        self.stackedWidget_2.setMaximumSize(QSize(660, 16777215))
        self.stackedWidget_2.setLineWidth(0)
        self.island_page_2 = QWidget()
        self.island_page_2.setObjectName(u"island_page_2")
        self.verticalLayout_6 = QVBoxLayout(self.island_page_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, -1, 0, 0)
        self.frame_5 = QFrame(self.island_page_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(650, 70))
        self.frame_5.setMaximumSize(QSize(650, 70))
        self.frame_5.setStyleSheet(u"background: #403C43;\n"
"border-radius: 5px;\n"
"margin-left: 9px;")
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.island_task_bar = QProgressBar(self.frame_5)
        self.island_task_bar.setObjectName(u"island_task_bar")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.island_task_bar.sizePolicy().hasHeightForWidth())
        self.island_task_bar.setSizePolicy(sizePolicy3)
        self.island_task_bar.setStyleSheet(u"QProgressBar{\n"
"	background: none;\n"
"	background-color: #686868;\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	background-color: #2AED7B;\n"
"	border-radius: 4px;\n"
"}")
        self.island_task_bar.setValue(28)
        self.island_task_bar.setTextVisible(False)
        self.island_task_bar.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_8.addWidget(self.island_task_bar)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Sunken)
        self.frame_7.setLineWidth(0)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.label_2 = QLabel(self.frame_7)
        self.label_2.setObjectName(u"label_2")
        font11 = QFont()
        font11.setFamilies([u"Intro Black"])
        font11.setPointSize(8)
        self.label_2.setFont(font11)
        self.label_2.setStyleSheet(u"color: #fff;")

        self.horizontalLayout_6.addWidget(self.label_2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)


        self.verticalLayout_8.addWidget(self.frame_7)


        self.verticalLayout_6.addWidget(self.frame_5)

        self.scrollArea = QScrollArea(self.island_page_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setEnabled(True)
        self.scrollArea.setMinimumSize(QSize(650, 320))
        self.scrollArea.setMaximumSize(QSize(660, 450))
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Shadow.Raised)
        self.scrollArea.setWidgetResizable(True)
        self.island_tasks_area = QWidget()
        self.island_tasks_area.setObjectName(u"island_tasks_area")
        self.island_tasks_area.setGeometry(QRect(0, 0, 660, 446))
        self.verticalLayout_7 = QVBoxLayout(self.island_tasks_area)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.scrollArea.setWidget(self.island_tasks_area)

        self.verticalLayout_6.addWidget(self.scrollArea)

        self.stackedWidget_2.addWidget(self.island_page_2)
        self.backpack_page = QWidget()
        self.backpack_page.setObjectName(u"backpack_page")
        self.stackedWidget_2.addWidget(self.backpack_page)
        self.shop_page = QWidget()
        self.shop_page.setObjectName(u"shop_page")
        self.frame_19 = QFrame(self.shop_page)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setGeometry(QRect(0, 10, 661, 521))
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_19)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_12 = QFrame(self.frame_19)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 45))
        self.frame_12.setMaximumSize(QSize(16777215, 45))
        self.horizontalLayout_23 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_20)

        self.label_30 = QLabel(self.frame_12)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(150, 45))
        self.label_30.setMaximumSize(QSize(150, 45))
        font12 = QFont()
        font12.setFamilies([u"Code Pro Bold"])
        font12.setPointSize(20)
        self.label_30.setFont(font12)
        self.label_30.setStyleSheet(u"background-color: rgb(64, 60, 67);\n"
"border-radius: 5px;")
        self.label_30.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_23.addWidget(self.label_30)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_21)


        self.verticalLayout_14.addWidget(self.frame_12)

        self.buy_ckicks_frame = QFrame(self.frame_19)
        self.buy_ckicks_frame.setObjectName(u"buy_ckicks_frame")
        self.horizontalLayout_24 = QHBoxLayout(self.buy_ckicks_frame)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.one_click_buy_frame = QFrame(self.buy_ckicks_frame)
        self.one_click_buy_frame.setObjectName(u"one_click_buy_frame")
        self.one_click_buy_frame.setMinimumSize(QSize(170, 150))
        self.one_click_buy_frame.setMaximumSize(QSize(170, 150))
        self.one_click_buy_frame.setStyleSheet(u"background-color: rgb(64, 60, 67);\n"
"border-radius:10px;\n"
"")
        self.verticalLayout_10 = QVBoxLayout(self.one_click_buy_frame)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.one_click_buy_frame)
        self.frame_13.setObjectName(u"frame_13")
        self.horizontalLayout_18 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_12)

        self.label_6 = QLabel(self.frame_13)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(70, 30))
        font13 = QFont()
        font13.setFamilies([u"Code Pro Bold"])
        font13.setPointSize(20)
        font13.setBold(True)
        self.label_6.setFont(font13)
        self.label_6.setStyleSheet(u"background-color: rgb(42, 237, 123);\n"
"border-radius: 8px;\n"
"")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_6)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_13)


        self.verticalLayout_10.addWidget(self.frame_13)

        self.btn_one_click_buy_1 = QPushButton(self.one_click_buy_frame)
        self.btn_one_click_buy_1.setObjectName(u"btn_one_click_buy_1")
        self.btn_one_click_buy_1.setFont(font13)
        self.btn_one_click_buy_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_one_click_buy_1.setFlat(False)

        self.verticalLayout_10.addWidget(self.btn_one_click_buy_1)

        self.frame_14 = QFrame(self.one_click_buy_frame)
        self.frame_14.setObjectName(u"frame_14")
        self.horizontalLayout_17 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_7 = QLabel(self.frame_14)
        self.label_7.setObjectName(u"label_7")
        font14 = QFont()
        font14.setPointSize(15)
        font14.setBold(True)
        self.label_7.setFont(font14)
        self.label_7.setStyleSheet(u"color: rgb(42, 237, 123);\n"
"margin: 3px;")

        self.horizontalLayout_17.addWidget(self.label_7)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_11)

        self.label_9 = QLabel(self.frame_14)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font14)

        self.horizontalLayout_17.addWidget(self.label_9)


        self.verticalLayout_10.addWidget(self.frame_14)


        self.horizontalLayout_24.addWidget(self.one_click_buy_frame)

        self.one_click_buy_frame_2 = QFrame(self.buy_ckicks_frame)
        self.one_click_buy_frame_2.setObjectName(u"one_click_buy_frame_2")
        self.one_click_buy_frame_2.setMinimumSize(QSize(170, 150))
        self.one_click_buy_frame_2.setMaximumSize(QSize(170, 150))
        self.one_click_buy_frame_2.setStyleSheet(u"background-color: rgb(64, 60, 67);\n"
"border-radius:10px;")
        self.verticalLayout_12 = QVBoxLayout(self.one_click_buy_frame_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.one_click_buy_frame_2)
        self.frame_15.setObjectName(u"frame_15")
        self.horizontalLayout_19 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_14)

        self.label_22 = QLabel(self.frame_15)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(70, 30))
        self.label_22.setFont(font13)
        self.label_22.setStyleSheet(u"background-color: rgb(42, 237, 123);\n"
"border-radius: 8px;\n"
"")
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_19.addWidget(self.label_22)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_15)


        self.verticalLayout_12.addWidget(self.frame_15)

        self.btn_one_click_buy_2 = QPushButton(self.one_click_buy_frame_2)
        self.btn_one_click_buy_2.setObjectName(u"btn_one_click_buy_2")
        self.btn_one_click_buy_2.setFont(font13)
        self.btn_one_click_buy_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_one_click_buy_2.setFlat(False)

        self.verticalLayout_12.addWidget(self.btn_one_click_buy_2)

        self.frame_16 = QFrame(self.one_click_buy_frame_2)
        self.frame_16.setObjectName(u"frame_16")
        self.horizontalLayout_20 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_23 = QLabel(self.frame_16)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font14)
        self.label_23.setStyleSheet(u"color: rgb(42, 237, 123);\n"
"margin: 3px;")

        self.horizontalLayout_20.addWidget(self.label_23)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_16)

        self.label_25 = QLabel(self.frame_16)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font14)

        self.horizontalLayout_20.addWidget(self.label_25)


        self.verticalLayout_12.addWidget(self.frame_16)


        self.horizontalLayout_24.addWidget(self.one_click_buy_frame_2)

        self.one_click_buy_frame_3 = QFrame(self.buy_ckicks_frame)
        self.one_click_buy_frame_3.setObjectName(u"one_click_buy_frame_3")
        self.one_click_buy_frame_3.setMinimumSize(QSize(170, 150))
        self.one_click_buy_frame_3.setMaximumSize(QSize(170, 150))
        self.one_click_buy_frame_3.setStyleSheet(u"background-color: rgb(64, 60, 67);\n"
"border-radius:10px;")
        self.verticalLayout_13 = QVBoxLayout(self.one_click_buy_frame_3)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.one_click_buy_frame_3)
        self.frame_17.setObjectName(u"frame_17")
        self.horizontalLayout_21 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_17)

        self.label_26 = QLabel(self.frame_17)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(70, 30))
        self.label_26.setFont(font13)
        self.label_26.setStyleSheet(u"background-color: rgb(42, 237, 123);\n"
"border-radius: 8px;\n"
"")
        self.label_26.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_26)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_18)


        self.verticalLayout_13.addWidget(self.frame_17)

        self.btn_one_click_buy_3 = QPushButton(self.one_click_buy_frame_3)
        self.btn_one_click_buy_3.setObjectName(u"btn_one_click_buy_3")
        self.btn_one_click_buy_3.setFont(font13)
        self.btn_one_click_buy_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_one_click_buy_3.setFlat(False)

        self.verticalLayout_13.addWidget(self.btn_one_click_buy_3)

        self.frame_18 = QFrame(self.one_click_buy_frame_3)
        self.frame_18.setObjectName(u"frame_18")
        self.horizontalLayout_22 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_27 = QLabel(self.frame_18)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font14)
        self.label_27.setStyleSheet(u"color: rgb(42, 237, 123);\n"
"margin: 3px;")

        self.horizontalLayout_22.addWidget(self.label_27)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_19)

        self.label_29 = QLabel(self.frame_18)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font14)

        self.horizontalLayout_22.addWidget(self.label_29)


        self.verticalLayout_13.addWidget(self.frame_18)


        self.horizontalLayout_24.addWidget(self.one_click_buy_frame_3)


        self.verticalLayout_14.addWidget(self.buy_ckicks_frame)

        self.frame_24 = QFrame(self.frame_19)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(0, 20))
        self.frame_24.setMaximumSize(QSize(16777215, 45))
        self.horizontalLayout_33 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_33)

        self.label_44 = QLabel(self.frame_24)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMinimumSize(QSize(150, 45))
        self.label_44.setMaximumSize(QSize(150, 45))
        self.label_44.setFont(font12)
        self.label_44.setStyleSheet(u"background-color: rgb(64, 60, 67);\n"
"border-radius: 5px;")
        self.label_44.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_44.setMargin(0)

        self.horizontalLayout_33.addWidget(self.label_44)

        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_34)


        self.verticalLayout_14.addWidget(self.frame_24)

        self.buy_ckicks_frame_2 = QFrame(self.frame_19)
        self.buy_ckicks_frame_2.setObjectName(u"buy_ckicks_frame_2")
        self.horizontalLayout_34 = QHBoxLayout(self.buy_ckicks_frame_2)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.one_click_buy_frame_7 = QFrame(self.buy_ckicks_frame_2)
        self.one_click_buy_frame_7.setObjectName(u"one_click_buy_frame_7")
        self.one_click_buy_frame_7.setMinimumSize(QSize(170, 150))
        self.one_click_buy_frame_7.setMaximumSize(QSize(170, 150))
        self.one_click_buy_frame_7.setStyleSheet(u"background-color: rgb(64, 60, 67);\n"
"border-radius:10px;\n"
"")
        self.verticalLayout_19 = QVBoxLayout(self.one_click_buy_frame_7)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_25 = QFrame(self.one_click_buy_frame_7)
        self.frame_25.setObjectName(u"frame_25")
        self.horizontalLayout_35 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_45 = QLabel(self.frame_25)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMinimumSize(QSize(70, 30))
        font15 = QFont()
        font15.setPointSize(10)
        font15.setBold(True)
        self.label_45.setFont(font15)
        self.label_45.setStyleSheet(u"")
        self.label_45.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_35.addWidget(self.label_45)


        self.verticalLayout_19.addWidget(self.frame_25)

        self.btn_one_boost_buy_1 = QPushButton(self.one_click_buy_frame_7)
        self.btn_one_boost_buy_1.setObjectName(u"btn_one_boost_buy_1")
        self.btn_one_boost_buy_1.setFont(font13)
        self.btn_one_boost_buy_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_one_boost_buy_1.setFlat(False)

        self.verticalLayout_19.addWidget(self.btn_one_boost_buy_1)

        self.frame_26 = QFrame(self.one_click_buy_frame_7)
        self.frame_26.setObjectName(u"frame_26")
        self.horizontalLayout_36 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_46 = QLabel(self.frame_26)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font14)
        self.label_46.setStyleSheet(u"color: rgb(42, 237, 123);\n"
"margin: 3px;")

        self.horizontalLayout_36.addWidget(self.label_46)

        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_37)

        self.label_48 = QLabel(self.frame_26)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font14)

        self.horizontalLayout_36.addWidget(self.label_48)


        self.verticalLayout_19.addWidget(self.frame_26)


        self.horizontalLayout_34.addWidget(self.one_click_buy_frame_7)

        self.one_click_buy_frame_9 = QFrame(self.buy_ckicks_frame_2)
        self.one_click_buy_frame_9.setObjectName(u"one_click_buy_frame_9")
        self.one_click_buy_frame_9.setMinimumSize(QSize(170, 150))
        self.one_click_buy_frame_9.setMaximumSize(QSize(170, 150))
        self.one_click_buy_frame_9.setStyleSheet(u"background-color: rgb(64, 60, 67);\n"
"border-radius:10px;")
        self.verticalLayout_21 = QVBoxLayout(self.one_click_buy_frame_9)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_29 = QFrame(self.one_click_buy_frame_9)
        self.frame_29.setObjectName(u"frame_29")
        self.horizontalLayout_39 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_53 = QLabel(self.frame_29)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setMinimumSize(QSize(70, 30))
        font16 = QFont()
        font16.setPointSize(14)
        font16.setBold(True)
        self.label_53.setFont(font16)
        self.label_53.setStyleSheet(u"")
        self.label_53.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_39.addWidget(self.label_53)


        self.verticalLayout_21.addWidget(self.frame_29)

        self.btn_one_boost_buy_2 = QPushButton(self.one_click_buy_frame_9)
        self.btn_one_boost_buy_2.setObjectName(u"btn_one_boost_buy_2")
        self.btn_one_boost_buy_2.setFont(font13)
        self.btn_one_boost_buy_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_one_boost_buy_2.setFlat(False)

        self.verticalLayout_21.addWidget(self.btn_one_boost_buy_2)

        self.frame_30 = QFrame(self.one_click_buy_frame_9)
        self.frame_30.setObjectName(u"frame_30")
        self.horizontalLayout_40 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_54 = QLabel(self.frame_30)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font14)
        self.label_54.setStyleSheet(u"color: rgb(42, 237, 123);\n"
"margin: 3px;")

        self.horizontalLayout_40.addWidget(self.label_54)

        self.horizontalSpacer_43 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_40.addItem(self.horizontalSpacer_43)

        self.label_56 = QLabel(self.frame_30)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setFont(font14)

        self.horizontalLayout_40.addWidget(self.label_56)


        self.verticalLayout_21.addWidget(self.frame_30)


        self.horizontalLayout_34.addWidget(self.one_click_buy_frame_9)


        self.verticalLayout_14.addWidget(self.buy_ckicks_frame_2)

        self.stackedWidget_2.addWidget(self.shop_page)
        self.stackedWidget.addWidget(self.island_page)

        self.verticalLayout_9.addWidget(self.stackedWidget)
=======
        self.rang.setMaximumSize(QSize(16777215, 200))
        self.verticalLayout_2 = QVBoxLayout(self.rang)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.rang)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)
        self.label_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_3.setStyleSheet(u"text-shadow: -1px 2px 6px rgba(0, 0, 0, 0.5);")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.progressBar = QProgressBar(self.rang)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(200, 0))
        self.progressBar.setMaximumSize(QSize(300, 16777215))
        self.progressBar.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	background-color: rgb(103, 103, 103);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	border-radius: 5px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(85, 255, 127, 255), stop:1 rgba(85, 255, 255, 255));\n"
"}")
        self.progressBar.setValue(22)
        self.progressBar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progressBar.setTextVisible(False)
        self.progressBar.setFormat(u"%p%")

        self.verticalLayout_2.addWidget(self.progressBar)

        self.label_4 = QLabel(self.rang)
        self.label_4.setObjectName(u"label_4")
        font4 = QFont()
        font4.setFamilies([u"a_Concepto"])
        font4.setPointSize(18)
        self.label_4.setFont(font4)
        self.label_4.setStyleSheet(u"text-shadow: -1px 2px 6px rgba(0, 0, 0, 0.5);")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_4)


        self.verticalLayout_4.addWidget(self.rang, 0, Qt.AlignmentFlag.AlignVCenter)

        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(200, 400))
        self.widget.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout_4.addWidget(self.widget)


        self.horizontalLayout_2.addWidget(self.frame)
>>>>>>> main

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

<<<<<<< HEAD
        self.stackedWidget.setCurrentIndex(1)
        self.click_btn.setDefault(False)
        self.stackedWidget_2.setCurrentIndex(2)
=======
        self.pushButton.setDefault(False)
>>>>>>> main


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Crypto Miner", None))
<<<<<<< HEAD
        self.skin_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0438\u043d", None))
        self.label_5.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041c\u041e\u041d\u0415\u0422\u042b", None))
        self.clicks_counter.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.menu_btn.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0410\u0413\u0410\u0417\u0418\u041d", None))
        self.level_number.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0420\u041e\u0412\u0415\u041d\u042c 1", None))
#if QT_CONFIG(accessibility)
        self.rank_bar.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.rating.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.goal.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.level_upgrade_btn.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043b\u0443\u0447\u0448\u0438\u0442\u044c", None))
        self.open_island_btn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0442\u0440\u043e\u0432 \u0437\u0430\u0434\u0430\u043d\u0438\u0439", None))
        self.menu_bar_img1.setText("")
        self.open_shop_btn.setText(QCoreApplication.translate("MainWindow", u"\u043c\u0430\u0433\u0430\u0437\u0438\u043d", None))
        self.menu_bar_img2.setText("")
        self.open_backpack_btn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0440\u0442\u0444\u0435\u043b\u044c", None))
        self.menu_bar_img3.setText("")
        self.close_island_btn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0411\u0420\u0410\u0422\u041d\u041e", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u041c\u041e\u041d\u0415\u0422\u042b", None))
        self.island_money_counter.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0410\u0412\u042b\u041a", None))
        self.island_skill_counter.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.island_level_title.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0410\u0427\u0418\u041d\u0410\u042e\u0429\u0418\u0419", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0434\u0435\u0441\u044c \u0431\u0443\u0434\u0435\u0442 \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0442\u044c\u0441\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0437\u0430\u0434\u0430\u043d\u0438\u0438", None))
#if QT_CONFIG(tooltip)
        self.scrollArea.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u041a\u041b\u0418\u041a\u0418", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"+1", None))
        self.btn_one_click_buy_1.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0423\u041f\u0418\u0422\u042c", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"1750", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"0/10", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"+3", None))
        self.btn_one_click_buy_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0423\u041f\u0418\u0422\u042c", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"5000", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"0/10", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"+5", None))
        self.btn_one_click_buy_3.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0423\u041f\u0418\u0422\u042c", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"9590", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"0/10", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0423\u0421\u0422\u042b", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0412\u0422\u041e-\u041a\u041b\u0418\u041a 15 \u0421\u0415\u041a", None))
        self.btn_one_boost_buy_1.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0423\u041f\u0418\u0422\u042c", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"1750", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"0/10", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"\u04252 30 \u0421\u0415\u041a", None))
        self.btn_one_boost_buy_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0423\u041f\u0418\u0422\u042c", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"9590", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"0/10", None))
=======
        self.label_5.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"COUNT", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0410\u0413\u0410\u0417\u0418\u041d", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"RANG", None))
#if QT_CONFIG(accessibility)
        self.progressBar.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"0/1000", None))
>>>>>>> main
    # retranslateUi

