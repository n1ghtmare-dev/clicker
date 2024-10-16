# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'error.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Error(object):
    def setupUi(self, Error):
        if not Error.objectName():
            Error.setObjectName(u"Error")
        Error.resize(332, 174)
        Error.setStyleSheet(u"background-color: rgb(65, 66, 66);")
        self.frame = QFrame(Error)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 10, 331, 161))
        self.frame.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame1 = QFrame(self.frame)
        self.frame1.setObjectName(u"frame1")
        font = QFont()
        font.setPointSize(25)
        self.frame1.setFont(font)
        self.horizontalLayout = QHBoxLayout(self.frame1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.frame1)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(120, 50))
        self.label.setMaximumSize(QSize(120, 50))
        font1 = QFont()
        font1.setFamilies([u"Gill Sans"])
        font1.setPointSize(25)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 103, 102);\n"
"border-radius: 10px;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frame1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(15)
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.frame2 = QFrame(self.frame)
        self.frame2.setObjectName(u"frame2")
        self.horizontalLayout_2 = QHBoxLayout(self.frame2)
#ifndef Q_OS_MAC
        self.horizontalLayout_2.setSpacing(-1)
#endif
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(125, 25))
        self.pushButton.setMaximumSize(QSize(125, 25))
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 153, 151);\n"
"border-radius: 5px;")

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.frame2)


        self.retranslateUi(Error)

        QMetaObject.connectSlotsByName(Error)
    # setupUi

    def retranslateUi(self, Error):
        Error.setWindowTitle(QCoreApplication.translate("Error", u"Form", None))
        self.label.setText(QCoreApplication.translate("Error", u"\u0423\u041f\u0421...", None))
        self.label_2.setText(QCoreApplication.translate("Error", u"\u041d\u0415\u0414\u041e\u0421\u0422\u0410\u0422\u041e\u0427\u041d\u041e\n"
" \u0421\u0420\u0415\u0414\u0421\u0422\u0412", None))
        self.pushButton.setText(QCoreApplication.translate("Error", u"OK", None))
    # retranslateUi

