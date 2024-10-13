# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu_ui_widget.ui'
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
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import images_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(900, 600)
        Form.setMinimumSize(QSize(900, 600))
        Form.setMaximumSize(QSize(900, 600))
        Form.setStyleSheet(u"background-image: url(:/images/winterbg.png);")
        self.frame_13 = QFrame(Form)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setEnabled(True)
        self.frame_13.setGeometry(QRect(230, 160, 161, 191))
        self.frame_13.setStyleSheet(u"background: #403C43;\n"
"border-radius: 5px;")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_13)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pushButton_5 = QPushButton(self.frame_13)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"color: #fff;")

        self.verticalLayout_5.addWidget(self.pushButton_5)

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
        font = QFont()
        font.setFamilies([u"Data Trash"])
        font.setPointSize(8)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet(u"color: white;\n"
"background: none;")

        self.horizontalLayout_10.addWidget(self.label_19)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_11)


        self.verticalLayout_5.addWidget(self.frame_15)

        self.label_20 = QLabel(self.frame_13)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setEnabled(True)
        font1 = QFont()
        font1.setFamilies([u"Intro Black"])
        font1.setPointSize(8)
        font1.setBold(True)
        self.label_20.setFont(font1)
        self.label_20.setStyleSheet(u"color: white;\n"
"background: none;")
        self.label_20.setScaledContents(False)
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_20)

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


        self.verticalLayout_5.addWidget(self.frame_16, 0, Qt.AlignmentFlag.AlignVCenter)

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
        font2 = QFont()
        font2.setFamilies([u"Intro Black"])
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"color: #fff;")

        self.horizontalLayout_13.addWidget(self.label_7)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_15)


        self.verticalLayout_5.addWidget(self.frame_17)

        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(230, 70, 660, 80))
        self.frame_3.setMinimumSize(QSize(660, 80))
        self.frame_3.setMaximumSize(QSize(660, 80))
        self.frame_3.setStyleSheet(u"background: #403C43;\n"
"border-radius: 5px;")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.progressBar = QProgressBar(self.frame_3)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
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

        self.verticalLayout_4.addWidget(self.progressBar)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.label_2 = QLabel(self.frame_7)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: #fff;")

        self.horizontalLayout_6.addWidget(self.label_2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)


        self.verticalLayout_4.addWidget(self.frame_7)

        self.frame_4 = QFrame(Form)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(230, 10, 660, 53))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setMinimumSize(QSize(660, 0))
        self.frame_4.setMaximumSize(QSize(660, 16777215))
        self.frame_4.setStyleSheet(u"background: #403C43;\n"
"border-radius: 5px;")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.money_count_frame = QFrame(self.frame_4)
        self.money_count_frame.setObjectName(u"money_count_frame")
        self.money_count_frame.setEnabled(True)
        self.money_count_frame.setStyleSheet(u"background:none;\n"
"")
        self.horizontalLayout_2 = QHBoxLayout(self.money_count_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_13 = QLabel(self.money_count_frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setEnabled(False)
        font3 = QFont()
        font3.setFamilies([u"Code Pro Bold"])
        font3.setPointSize(10)
        self.label_13.setFont(font3)
        self.label_13.setStyleSheet(u"color: white;\n"
"background: none;")

        self.horizontalLayout_2.addWidget(self.label_13)

        self.label_9 = QLabel(self.money_count_frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font3)
        self.label_9.setStyleSheet(u"color: white;\n"
"background: none;")

        self.horizontalLayout_2.addWidget(self.label_9)


        self.horizontalLayout_4.addWidget(self.money_count_frame)

        self.skill_count_frame = QFrame(self.frame_4)
        self.skill_count_frame.setObjectName(u"skill_count_frame")
        self.skill_count_frame.setStyleSheet(u"background: none;")
        self.horizontalLayout = QHBoxLayout(self.skill_count_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_10 = QLabel(self.skill_count_frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setEnabled(False)
        self.label_10.setFont(font3)
        self.label_10.setStyleSheet(u"color: white;\n"
"background: none;")

        self.horizontalLayout.addWidget(self.label_10)

        self.label_11 = QLabel(self.skill_count_frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font3)
        self.label_11.setStyleSheet(u"color: white;\n"
"background: none;")

        self.horizontalLayout.addWidget(self.label_11)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.horizontalLayout_4.addWidget(self.skill_count_frame)

        self.label_12 = QLabel(self.frame_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setEnabled(False)
        self.label_12.setFont(font3)
        self.label_12.setStyleSheet(u"color: white;\n"
"background: none;")

        self.horizontalLayout_4.addWidget(self.label_12)

        self.frame_5 = QFrame(Form)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(-1, -1, 221, 601))
        self.frame_5.setStyleSheet(u"background: #403C43;")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.menu_bar = QFrame(self.frame_5)
        self.menu_bar.setObjectName(u"menu_bar")
        self.menu_bar.setGeometry(QRect(40, 20, 144, 75))
        self.menu_bar.setStyleSheet(u"background: none;\n"
"border: none;\n"
"")
        self.verticalLayout = QVBoxLayout(self.menu_bar)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(self.menu_bar)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(False)
        font4 = QFont()
        font4.setFamilies([u"Disket Mono"])
        font4.setPointSize(10)
        font4.setBold(True)
        self.pushButton.setFont(font4)
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background: none;\n"
"border: none;\n"
"color: #2AED7B;")

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.menu_bar)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setFont(font4)
        self.pushButton_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"background: none;\n"
"border: none;\n"
"color: white;")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.menu_bar)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font4)
        self.pushButton_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"background: none;\n"
"border: none;\n"
"color: white;")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.frame_14 = QFrame(Form)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setEnabled(True)
        self.frame_14.setGeometry(QRect(400, 160, 161, 191))
        self.frame_14.setStyleSheet(u"background: #403C43;\n"
"border-radius: 5px;")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_14)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pushButton_6 = QPushButton(self.frame_14)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_6.setStyleSheet(u"color: #fff;")

        self.verticalLayout_6.addWidget(self.pushButton_6)

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
        self.label_21.setFont(font)
        self.label_21.setStyleSheet(u"color: white;\n"
"background: none;")

        self.horizontalLayout_11.addWidget(self.label_21)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_13)


        self.verticalLayout_6.addWidget(self.frame_18)

        self.label_22 = QLabel(self.frame_14)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setEnabled(True)
        self.label_22.setFont(font1)
        self.label_22.setStyleSheet(u"color: white;\n"
"background: none;")
        self.label_22.setScaledContents(False)
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_22)

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


        self.verticalLayout_6.addWidget(self.frame_19, 0, Qt.AlignmentFlag.AlignVCenter)

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
        self.label_14.setFont(font2)
        self.label_14.setStyleSheet(u"color: #fff;")

        self.horizontalLayout_15.addWidget(self.label_14)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_17)


        self.verticalLayout_6.addWidget(self.frame_20)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u044b\u0432\u0430\u0442\u044c", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u044b\u0447\u043d\u0430\u044f \u0448\u0430\u0445\u0442\u0430", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"7 \u043e\u0447\u043a. \u043d\u0430\u0432\u044b\u043a\u0430 / 3\u0441\u0435\u043a.", None))
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("Form", u"0/550", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0417\u0434\u0435\u0441\u044c \u0431\u0443\u0434\u0435\u0442 \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0442\u044c\u0441\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0437\u0430\u0434\u0430\u043d\u0438\u0438", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"\u041c\u041e\u041d\u0415\u0422\u042b", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u041d\u0410\u0412\u042b\u041a", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"\u041d\u0410\u0427\u0418\u041d\u0410\u042e\u0429\u0418\u0419", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u041e\u0421\u0422\u0420\u041e\u0412 \u0417\u0410\u0414\u0410\u041d\u0418\u0419", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u041c\u0410\u0413\u0410\u0417\u0418\u041d", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u041f\u041e\u0420\u0422\u0424\u0415\u041b\u042c", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u044b\u0432\u0430\u0442\u044c", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u044b\u0447\u043d\u0430\u044f \u0448\u0430\u0445\u0442\u0430", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"7 \u043e\u0447\u043a. \u043d\u0430\u0432\u044b\u043a\u0430 / 3\u0441\u0435\u043a.", None))
        self.label_8.setText("")
        self.label_14.setText(QCoreApplication.translate("Form", u"0/550", None))
    # retranslateUi

