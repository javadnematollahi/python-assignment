# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'password_generate.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(810, 537)
        MainWindow.setStyleSheet(u"background-color: rgb(228, 217, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_8 = QSpacerItem(199, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_8, 0, 0, 1, 3)

        self.passwordgenerator = QLabel(self.centralwidget)
        self.passwordgenerator.setObjectName(u"passwordgenerator")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passwordgenerator.sizePolicy().hasHeightForWidth())
        self.passwordgenerator.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.passwordgenerator.setFont(font)

        self.gridLayout.addWidget(self.passwordgenerator, 0, 3, 1, 3)

        self.horizontalSpacer_7 = QSpacerItem(200, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 0, 6, 1, 3)

        self.weak = QRadioButton(self.centralwidget)
        self.weak.setObjectName(u"weak")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.weak.sizePolicy().hasHeightForWidth())
        self.weak.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(14)
        self.weak.setFont(font1)
        self.weak.setStyleSheet(u"background-color: rgb(255, 93, 96);")

        self.gridLayout.addWidget(self.weak, 1, 1, 1, 7)

        self.horizontalSpacer_6 = QSpacerItem(22, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 2, 0, 1, 1)

        self.medium = QRadioButton(self.centralwidget)
        self.medium.setObjectName(u"medium")
        sizePolicy1.setHeightForWidth(self.medium.sizePolicy().hasHeightForWidth())
        self.medium.setSizePolicy(sizePolicy1)
        self.medium.setFont(font1)
        self.medium.setStyleSheet(u"background-color: rgb(255, 157, 92);")

        self.gridLayout.addWidget(self.medium, 2, 1, 1, 7)

        self.horizontalSpacer_5 = QSpacerItem(23, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 2, 8, 1, 1)

        self.strong = QRadioButton(self.centralwidget)
        self.strong.setObjectName(u"strong")
        sizePolicy1.setHeightForWidth(self.strong.sizePolicy().hasHeightForWidth())
        self.strong.setSizePolicy(sizePolicy1)
        self.strong.setSizeIncrement(QSize(0, 0))
        self.strong.setBaseSize(QSize(0, 0))
        self.strong.setFont(font1)
        self.strong.setStyleSheet(u"background-color: rgb(169, 255, 205);\n"
"background-color: rgb(32, 147, 0);")

        self.gridLayout.addWidget(self.strong, 3, 1, 1, 7)

        self.horizontalSpacer = QSpacerItem(111, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 4, 0, 1, 2)

        self.showpass = QLineEdit(self.centralwidget)
        self.showpass.setObjectName(u"showpass")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.showpass.sizePolicy().hasHeightForWidth())
        self.showpass.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        self.showpass.setFont(font2)
        self.showpass.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.showpass, 4, 2, 1, 5)

        self.horizontalSpacer_2 = QSpacerItem(111, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 4, 7, 1, 2)

        self.generate = QPushButton(self.centralwidget)
        self.generate.setObjectName(u"generate")
        sizePolicy1.setHeightForWidth(self.generate.sizePolicy().hasHeightForWidth())
        self.generate.setSizePolicy(sizePolicy1)
        self.generate.setFont(font2)
        self.generate.setStyleSheet(u"background-color: rgb(255, 170, 0);")

        self.gridLayout.addWidget(self.generate, 5, 4, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(316, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 5, 0, 1, 4)

        self.horizontalSpacer_3 = QSpacerItem(334, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 5, 5, 1, 4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.passwordgenerator.setText(QCoreApplication.translate("MainWindow", u"PASSWORD GENERATOR", None))
        self.weak.setText(QCoreApplication.translate("MainWindow", u"Generate a Standard Strength Password\n"
"(8 characters long including a number, a special character and an uppercase letter)", None))
        self.medium.setText(QCoreApplication.translate("MainWindow", u"Generate an Extra Strong Password\n"
"(12 characters long with multiple numbers, special characters and uppercase letters)", None))
        self.strong.setText(QCoreApplication.translate("MainWindow", u"Generate a Super Strong Password\n"
"(20 characters long with multiple numbers, special characters and uppercase letters)", None))
        self.generate.setText(QCoreApplication.translate("MainWindow", u"GENERATE", None))
    # retranslateUi

