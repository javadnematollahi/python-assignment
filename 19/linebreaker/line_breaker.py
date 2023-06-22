# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'line_breaker.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QStatusBar, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(899, 821)
        MainWindow.setStyleSheet(u"background-color: rgb(248, 255, 203);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.titr = QLabel(self.centralwidget)
        self.titr.setObjectName(u"titr")
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.titr.setFont(font)

        self.gridLayout.addWidget(self.titr, 0, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(18)
        self.label.setFont(font1)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 2)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 2, 0, 1, 3)

        self.lbreaker = QRadioButton(self.centralwidget)
        self.lbreaker.setObjectName(u"lbreaker")
        self.lbreaker.setFont(font1)

        self.gridLayout.addWidget(self.lbreaker, 3, 0, 1, 1)

        self.pbreaker = QRadioButton(self.centralwidget)
        self.pbreaker.setObjectName(u"pbreaker")
        self.pbreaker.setFont(font1)

        self.gridLayout.addWidget(self.pbreaker, 3, 1, 1, 2)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 4, 0, 1, 3)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setFrameShape(QFrame.NoFrame)

        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 3)

        self.input = QTextEdit(self.centralwidget)
        self.input.setObjectName(u"input")
        self.input.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border: 2px solid;\n"
"")

        self.gridLayout.addWidget(self.input, 6, 0, 1, 3)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        self.label_3.setFont(font2)

        self.gridLayout.addWidget(self.label_3, 7, 0, 1, 1)

        self.linebreaker = QPushButton(self.centralwidget)
        self.linebreaker.setObjectName(u"linebreaker")
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        self.linebreaker.setFont(font3)
        self.linebreaker.setStyleSheet(u"background-color: rgb(255, 170, 0);")

        self.gridLayout.addWidget(self.linebreaker, 7, 2, 1, 1)

        self.output = QTextEdit(self.centralwidget)
        self.output.setObjectName(u"output")
        self.output.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border: 2px solid;")

        self.gridLayout.addWidget(self.output, 8, 0, 1, 3)

        self.copytoclip = QPushButton(self.centralwidget)
        self.copytoclip.setObjectName(u"copytoclip")
        self.copytoclip.setFont(font3)
        self.copytoclip.setStyleSheet(u"background-color: rgb(255, 170, 0);")

        self.gridLayout.addWidget(self.copytoclip, 9, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Text Editor", None))
        self.titr.setText(QCoreApplication.translate("MainWindow", u"Remove Line Breaks", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Choose one of these line break options.", None))
        self.lbreaker.setText(QCoreApplication.translate("MainWindow", u"Remove line breaks only", None))
        self.pbreaker.setText(QCoreApplication.translate("MainWindow", u"Remove line breaks and paragraph breaks", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Paste your text in the box below and then click the button.\n"
"The new text will appear in the box at the bottom of the page.", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"New Text without Line Breaks", None))
        self.linebreaker.setText(QCoreApplication.translate("MainWindow", u"Remove Line Breaks", None))
        self.copytoclip.setText(QCoreApplication.translate("MainWindow", u"Copy to ClipBoard", None))
    # retranslateUi

