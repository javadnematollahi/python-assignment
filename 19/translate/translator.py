# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'translator.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(893, 722)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 210, 237);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)

        self.input = QComboBox(self.centralwidget)
        self.input.setObjectName(u"input")
        self.input.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.input, 0, 1, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.output = QComboBox(self.centralwidget)
        self.output.setObjectName(u"output")
        self.output.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.output, 0, 3, 1, 1)

        self.translate = QPushButton(self.centralwidget)
        self.translate.setObjectName(u"translate")
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.translate.setFont(font1)
        self.translate.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"\n"
"border: 8px solid;border-color: rgb(255, 23, 147);")

        self.gridLayout.addWidget(self.translate, 2, 2, 1, 2)

        self.source = QTextEdit(self.centralwidget)
        self.source.setObjectName(u"source")
        font2 = QFont()
        font2.setPointSize(12)
        self.source.setFont(font2)
        self.source.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.source, 1, 0, 1, 2)

        self.target = QTextEdit(self.centralwidget)
        self.target.setObjectName(u"target")
        self.target.setFont(font2)
        self.target.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.target, 1, 2, 1, 2)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Translator", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Target Language:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Source Language:", None))
        self.translate.setText(QCoreApplication.translate("MainWindow", u"Translate", None))
    # retranslateUi

