# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Puzzle_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(399, 448)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 40, 391, 361))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(20)
        self.widget.setFont(font)
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.btn1 = QPushButton(self.widget)
        self.btn1.setObjectName(u"btn1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn1.sizePolicy().hasHeightForWidth())
        self.btn1.setSizePolicy(sizePolicy1)
        self.btn1.setFont(font)

        self.gridLayout.addWidget(self.btn1, 0, 0, 1, 1)

        self.btn2 = QPushButton(self.widget)
        self.btn2.setObjectName(u"btn2")
        sizePolicy1.setHeightForWidth(self.btn2.sizePolicy().hasHeightForWidth())
        self.btn2.setSizePolicy(sizePolicy1)
        self.btn2.setFont(font)

        self.gridLayout.addWidget(self.btn2, 0, 1, 1, 1)

        self.btn3 = QPushButton(self.widget)
        self.btn3.setObjectName(u"btn3")
        sizePolicy1.setHeightForWidth(self.btn3.sizePolicy().hasHeightForWidth())
        self.btn3.setSizePolicy(sizePolicy1)
        self.btn3.setFont(font)

        self.gridLayout.addWidget(self.btn3, 0, 2, 1, 1)

        self.btn4 = QPushButton(self.widget)
        self.btn4.setObjectName(u"btn4")
        sizePolicy1.setHeightForWidth(self.btn4.sizePolicy().hasHeightForWidth())
        self.btn4.setSizePolicy(sizePolicy1)
        self.btn4.setFont(font)

        self.gridLayout.addWidget(self.btn4, 0, 3, 1, 1)

        self.btn5 = QPushButton(self.widget)
        self.btn5.setObjectName(u"btn5")
        sizePolicy1.setHeightForWidth(self.btn5.sizePolicy().hasHeightForWidth())
        self.btn5.setSizePolicy(sizePolicy1)
        self.btn5.setFont(font)

        self.gridLayout.addWidget(self.btn5, 1, 0, 1, 1)

        self.btn6 = QPushButton(self.widget)
        self.btn6.setObjectName(u"btn6")
        sizePolicy1.setHeightForWidth(self.btn6.sizePolicy().hasHeightForWidth())
        self.btn6.setSizePolicy(sizePolicy1)
        self.btn6.setFont(font)

        self.gridLayout.addWidget(self.btn6, 1, 1, 1, 1)

        self.btn7 = QPushButton(self.widget)
        self.btn7.setObjectName(u"btn7")
        sizePolicy1.setHeightForWidth(self.btn7.sizePolicy().hasHeightForWidth())
        self.btn7.setSizePolicy(sizePolicy1)
        self.btn7.setFont(font)

        self.gridLayout.addWidget(self.btn7, 1, 2, 1, 1)

        self.btn8 = QPushButton(self.widget)
        self.btn8.setObjectName(u"btn8")
        sizePolicy1.setHeightForWidth(self.btn8.sizePolicy().hasHeightForWidth())
        self.btn8.setSizePolicy(sizePolicy1)
        self.btn8.setFont(font)

        self.gridLayout.addWidget(self.btn8, 1, 3, 1, 1)

        self.btn9 = QPushButton(self.widget)
        self.btn9.setObjectName(u"btn9")
        sizePolicy1.setHeightForWidth(self.btn9.sizePolicy().hasHeightForWidth())
        self.btn9.setSizePolicy(sizePolicy1)
        self.btn9.setFont(font)

        self.gridLayout.addWidget(self.btn9, 2, 0, 1, 1)

        self.btn10 = QPushButton(self.widget)
        self.btn10.setObjectName(u"btn10")
        sizePolicy1.setHeightForWidth(self.btn10.sizePolicy().hasHeightForWidth())
        self.btn10.setSizePolicy(sizePolicy1)
        self.btn10.setFont(font)

        self.gridLayout.addWidget(self.btn10, 2, 1, 1, 1)

        self.btn11 = QPushButton(self.widget)
        self.btn11.setObjectName(u"btn11")
        sizePolicy1.setHeightForWidth(self.btn11.sizePolicy().hasHeightForWidth())
        self.btn11.setSizePolicy(sizePolicy1)
        self.btn11.setFont(font)

        self.gridLayout.addWidget(self.btn11, 2, 2, 1, 1)

        self.btn12 = QPushButton(self.widget)
        self.btn12.setObjectName(u"btn12")
        sizePolicy1.setHeightForWidth(self.btn12.sizePolicy().hasHeightForWidth())
        self.btn12.setSizePolicy(sizePolicy1)
        self.btn12.setFont(font)

        self.gridLayout.addWidget(self.btn12, 2, 3, 1, 1)

        self.btn13 = QPushButton(self.widget)
        self.btn13.setObjectName(u"btn13")
        sizePolicy1.setHeightForWidth(self.btn13.sizePolicy().hasHeightForWidth())
        self.btn13.setSizePolicy(sizePolicy1)
        self.btn13.setFont(font)

        self.gridLayout.addWidget(self.btn13, 3, 0, 1, 1)

        self.btn14 = QPushButton(self.widget)
        self.btn14.setObjectName(u"btn14")
        sizePolicy1.setHeightForWidth(self.btn14.sizePolicy().hasHeightForWidth())
        self.btn14.setSizePolicy(sizePolicy1)
        self.btn14.setFont(font)

        self.gridLayout.addWidget(self.btn14, 3, 1, 1, 1)

        self.btn15 = QPushButton(self.widget)
        self.btn15.setObjectName(u"btn15")
        sizePolicy1.setHeightForWidth(self.btn15.sizePolicy().hasHeightForWidth())
        self.btn15.setSizePolicy(sizePolicy1)
        self.btn15.setFont(font)

        self.gridLayout.addWidget(self.btn15, 3, 2, 1, 1)

        self.btn16 = QPushButton(self.widget)
        self.btn16.setObjectName(u"btn16")
        sizePolicy1.setHeightForWidth(self.btn16.sizePolicy().hasHeightForWidth())
        self.btn16.setSizePolicy(sizePolicy1)
        self.btn16.setFont(font)

        self.gridLayout.addWidget(self.btn16, 3, 3, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 399, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Puzzle15", None))
        self.btn1.setText("")
        self.btn2.setText("")
        self.btn3.setText("")
        self.btn4.setText("")
        self.btn5.setText("")
        self.btn6.setText("")
        self.btn7.setText("")
        self.btn8.setText("")
        self.btn9.setText("")
        self.btn10.setText("")
        self.btn11.setText("")
        self.btn12.setText("")
        self.btn13.setText("")
        self.btn14.setText("")
        self.btn15.setText("")
        self.btn16.setText("")
    # retranslateUi

