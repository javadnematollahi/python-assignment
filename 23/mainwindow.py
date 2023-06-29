# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(747, 759)
        mainWindow.setStyleSheet(u"")
        self.menunew = QAction(mainWindow)
        self.menunew.setObjectName(u"menunew")
        font = QFont()
        font.setPointSize(16)
        font.setKerning(True)
        font.setStyleStrategy(QFont.PreferDefault)
        self.menunew.setFont(font)
        self.menunew.setVisible(True)
        self.menunew.setMenuRole(QAction.ApplicationSpecificRole)
        self.menunew.setIconVisibleInMenu(True)
        self.menuopenfile = QAction(mainWindow)
        self.menuopenfile.setObjectName(u"menuopenfile")
        font1 = QFont()
        font1.setPointSize(16)
        self.menuopenfile.setFont(font1)
        self.solve_current_puzzle = QAction(mainWindow)
        self.solve_current_puzzle.setObjectName(u"solve_current_puzzle")
        self.About = QAction(mainWindow)
        self.About.setObjectName(u"About")
        self.Help = QAction(mainWindow)
        self.Help.setObjectName(u"Help")
        self.Exit = QAction(mainWindow)
        self.Exit.setObjectName(u"Exit")
        self.Back_to_game = QAction(mainWindow)
        self.Back_to_game.setObjectName(u"Back_to_game")
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontal_Layout = QHBoxLayout()
        self.horizontal_Layout.setObjectName(u"horizontal_Layout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontal_Layout.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.horizontal_Layout, 0, 0, 2, 1)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_3 = QGridLayout(self.page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.grid_Layout = QGridLayout()
        self.grid_Layout.setSpacing(0)
        self.grid_Layout.setObjectName(u"grid_Layout")

        self.gridLayout_3.addLayout(self.grid_Layout, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_2 = QGridLayout(self.page_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.page_2)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(12)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label.setFrameShape(QFrame.Box)
        self.label.setLineWidth(3)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_4 = QGridLayout(self.page_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_2 = QLabel(self.page_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFrameShape(QFrame.Box)
        self.label_2.setFrameShadow(QFrame.Plain)
        self.label_2.setLineWidth(3)

        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)

        self.gridLayout.addWidget(self.stackedWidget, 5, 0, 1, 1)

        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 747, 34))
        self.menubar.setFont(font1)
        self.menubar.setStyleSheet(u"background-color: rgb(255, 148, 185);")
        self.menuGame = QMenu(self.menubar)
        self.menuGame.setObjectName(u"menuGame")
        self.menuGame.setGeometry(QRect(183, 183, 245, 312))
        self.menuGame.setFont(font1)
        self.menuGame.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(109, 109, 109);")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuGame.menuAction())
        self.menuGame.addAction(self.Back_to_game)
        self.menuGame.addAction(self.menunew)
        self.menuGame.addAction(self.menuopenfile)
        self.menuGame.addAction(self.solve_current_puzzle)
        self.menuGame.addAction(self.About)
        self.menuGame.addAction(self.Help)
        self.menuGame.addAction(self.Exit)

        self.retranslateUi(mainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Soduku", None))
        self.menunew.setText(QCoreApplication.translate("mainWindow", u"New", None))
        self.menuopenfile.setText(QCoreApplication.translate("mainWindow", u"open file", None))
        self.solve_current_puzzle.setText(QCoreApplication.translate("mainWindow", u"solve current puzzle", None))
        self.About.setText(QCoreApplication.translate("mainWindow", u"About", None))
        self.Help.setText(QCoreApplication.translate("mainWindow", u"Help", None))
        self.Exit.setText(QCoreApplication.translate("mainWindow", u"Exit", None))
        self.Back_to_game.setText(QCoreApplication.translate("mainWindow", u"Back to game", None))
        self.label.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">Hello</span></p><p align=\"center\"><span style=\" font-weight:700;\">Welcome to Sudoku</span></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-family:'Source Sans Pro','sans-serif'; font-size:16px; font-weight:700; color:#000000;\">The history of Sudoku dates back to an 18th Century Swiss mathematician\u2019s</span></p><p align=\"center\"><span style=\" font-family:'Source Sans Pro','sans-serif'; font-size:16px; font-weight:700; color:#000000;\">game called \u201cLatin Squares\u201d (according to this article from the Economist)</span></p><p align=\"center\"><span style=\" font-family:'Source Sans Pro','sans-serif'; font-size:16px; font-weight:700; color:#000000;\">and some of the first number puzzles to appear in newspapers were published</span></p><p align=\"center\"><span style=\" font-family:'Source Sans Pro','sans-serif'; font-size:16px; font-weight:700; color:#000000;\">in France in 1895. But the modern game "
                        "of Sudoku as we recognize it today</span></p><p align=\"center\"><span style=\" font-family:'Source Sans Pro','sans-serif'; font-size:16px; font-weight:700; color:#000000;\">was invented by Howard Garns, a freelance puzzle inventor from Connersville,</span></p><p align=\"center\"><span style=\" font-family:'Source Sans Pro','sans-serif'; font-size:16px; font-weight:700; color:#000000;\">Indiana, USA in 1979 when it was published in\u00a0</span><span style=\" font-family:'Source Sans Pro','sans-serif'; font-size:16px; font-weight:700; font-style:italic; color:#000000;\">Dell Pencil Puzzles and Word </span></p><p align=\"center\"><span style=\" font-family:'Source Sans Pro','sans-serif'; font-size:16px; font-weight:700; font-style:italic; color:#000000;\">Games</span><span style=\" font-family:'Source Sans Pro','sans-serif'; font-size:16px; font-weight:700; color:#000000;\">\u00a0magazine. The puzzle was known as \u201cNumber Place,\u201d since it involved</span></p><p align=\"center\"><span style=\" font-family"
                        ":'Source Sans Pro','sans-serif'; font-size:16px; font-weight:700; color:#000000;\">placing individual numbers into empty spots on a 9 x 9 grid.</span></p><p align=\"center\"><br/><span style=\" font-size:14pt; font-weight:700;\">This game is written by javad nematollahi and py-sudoku python library is</span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">used for drawing the soduku numbers.</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Help:</span></p><p><br/></p><p><span style=\" font-size:12pt;\">help of sudoku will tell you how to play. </span></p><p align=\"center\"><span style=\" font-size:22pt; font-weight:700;\">Playing rules:</span></p><p><br/></p><p><span style=\" font-size:12pt;\">1.You just use these numbers in sudoku</span></p><p><span style=\" font-size:12pt;\">[1,2,3,4,5,6,7,8,9]</span></p><p><span style=\" font-size:12pt;\">2.In each row you should put one of 1 to 9 number and you cant set a number in two cell in a row. </span></p><p><span style=\" font-size:12pt;\">if you do this, the game will change the background color of that cell to red.</span></p><p><span style=\" font-size:12pt;\">3.In each column you should put one of 1 to 9 number and you cant set a number in two cell in a</span></p><p><span style=\" font-size:12pt;\">column. if you do this, the game will change the background color of that cell to red.</span></p><p><span style=\" font-size:12pt;"
                        "\">4.In each square you should put one of 1 to 9 number and you cant set a number in two cell in a </span></p><p><span style=\" font-size:12pt;\">square. if you do this, the game will change the background color of that cell to red.</span></p><p><span style=\" font-size:12pt;\">5. If you find the number of all empty cells, you will win the game.</span></p><p><br/></p><p><br/></p><p><br/></p></body></html>", None))
        self.menuGame.setTitle(QCoreApplication.translate("mainWindow", u"Game", None))
    # retranslateUi

