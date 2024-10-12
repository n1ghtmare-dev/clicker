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
    QSpacerItem, QVBoxLayout, QWidget)
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
        self.centralwidget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: #fff;")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_2 = QFrame(self.centralwidget)
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


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.mainframe = QFrame(self.centralwidget)
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

        self.verticalLayout_3.addWidget(self.click_btn, 0, Qt.AlignmentFlag.AlignVCenter)

        self.menu_btn = QPushButton(self.mainframe)
        self.menu_btn.setObjectName(u"menu_btn")
        font4 = QFont()
        font4.setFamilies([u"a_Concepto"])
        font4.setPointSize(22)
        self.menu_btn.setFont(font4)
        self.menu_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.menu_btn.setStyleSheet(u"border: none;\n"
"background: none;\n"
"background-color: rgba(255, 255, 255, 100);\n"
"border-radius: 8px;\n"
"padding: 10px 20px;")

        self.verticalLayout_3.addWidget(self.menu_btn, 0, Qt.AlignmentFlag.AlignVCenter)


        self.horizontalLayout_2.addWidget(self.mainframe, 0, Qt.AlignmentFlag.AlignVCenter)

        self.frame = QFrame(self.centralwidget)
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


        self.horizontalLayout_2.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

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
    # retranslateUi

