# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clock.ui'
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
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QTabWidget, QTimeEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(730, 653)
        MainWindow.setStyleSheet(u"background-color: rgb(165, 165, 165);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_8 = QGridLayout(self.tab)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"Gill Sans MT Ext Condensed Bold"])
        font.setPointSize(40)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"background-color: rgb(208, 208, 208);")
        self.label_3.setFrameShape(QFrame.WinPanel)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_3, 0, 0, 1, 1)

        self.irantime = QLabel(self.tab)
        self.irantime.setObjectName(u"irantime")
        font1 = QFont()
        font1.setFamilies([u"Seven Segment"])
        font1.setPointSize(40)
        self.irantime.setFont(font1)
        self.irantime.setStyleSheet(u"background-color: rgb(208, 208, 208);")
        self.irantime.setFrameShape(QFrame.WinPanel)
        self.irantime.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.irantime, 0, 1, 1, 1)

        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"background-color: rgb(208, 208, 208);")
        self.label_4.setFrameShape(QFrame.WinPanel)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_4, 1, 0, 1, 1)

        self.germanytime = QLabel(self.tab)
        self.germanytime.setObjectName(u"germanytime")
        self.germanytime.setFont(font1)
        self.germanytime.setStyleSheet(u"background-color: rgb(208, 208, 208);")
        self.germanytime.setFrameShape(QFrame.WinPanel)
        self.germanytime.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.germanytime, 1, 1, 1, 1)

        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"background-color: rgb(208, 208, 208);")
        self.label_5.setFrameShape(QFrame.WinPanel)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_5, 2, 0, 1, 1)

        self.usatime = QLabel(self.tab)
        self.usatime.setObjectName(u"usatime")
        self.usatime.setFont(font1)
        self.usatime.setStyleSheet(u"background-color: rgb(208, 208, 208);")
        self.usatime.setFrameShape(QFrame.WinPanel)
        self.usatime.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.usatime, 2, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_7 = QGridLayout(self.tab_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.stackedWidget = QStackedWidget(self.tab_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_alarms = QWidget()
        self.page_alarms.setObjectName(u"page_alarms")
        self.gridLayout_10 = QGridLayout(self.page_alarms)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.grid_alarm = QGridLayout()
        self.grid_alarm.setObjectName(u"grid_alarm")

        self.gridLayout_10.addLayout(self.grid_alarm, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_alarms)
        self.page_setalarm = QWidget()
        self.page_setalarm.setObjectName(u"page_setalarm")
        self.gridLayout_9 = QGridLayout(self.page_setalarm)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.verticalSpacer_4 = QSpacerItem(20, 88, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_9.addItem(self.verticalSpacer_4, 0, 3, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(68, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_12, 1, 0, 1, 1)

        self.timeEdit = QTimeEdit(self.page_setalarm)
        self.timeEdit.setObjectName(u"timeEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeEdit.sizePolicy().hasHeightForWidth())
        self.timeEdit.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Seven Segment"])
        font2.setPointSize(80)
        self.timeEdit.setFont(font2)
        self.timeEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.timeEdit.setAlignment(Qt.AlignCenter)
        self.timeEdit.setCurrentSection(QDateTimeEdit.HourSection)
        self.timeEdit.setTimeSpec(Qt.LocalTime)

        self.gridLayout_9.addWidget(self.timeEdit, 1, 1, 1, 4)

        self.horizontalSpacer_13 = QSpacerItem(68, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_13, 1, 5, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 28, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_9.addItem(self.verticalSpacer_6, 2, 2, 1, 2)

        self.horizontalSpacer_15 = QSpacerItem(198, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_15, 3, 0, 1, 2)

        self.btn_set_alarm = QPushButton(self.page_setalarm)
        self.btn_set_alarm.setObjectName(u"btn_set_alarm")
        font3 = QFont()
        font3.setFamilies([u"Gill Sans Ultra Bold Condensed"])
        font3.setPointSize(22)
        self.btn_set_alarm.setFont(font3)
        self.btn_set_alarm.setStyleSheet(u"background-color: rgb(208, 208, 208);")

        self.gridLayout_9.addWidget(self.btn_set_alarm, 3, 2, 1, 2)

        self.horizontalSpacer_14 = QSpacerItem(208, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_14, 3, 4, 1, 2)

        self.horizontalSpacer_16 = QSpacerItem(198, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_16, 4, 0, 1, 2)

        self.btn_back = QPushButton(self.page_setalarm)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setFont(font3)
        self.btn_back.setStyleSheet(u"background-color: rgb(208, 208, 208);")

        self.gridLayout_9.addWidget(self.btn_back, 4, 2, 1, 2)

        self.horizontalSpacer_17 = QSpacerItem(208, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_17, 4, 4, 1, 2)

        self.verticalSpacer_5 = QSpacerItem(20, 58, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_9.addItem(self.verticalSpacer_5, 5, 2, 1, 1)

        self.stackedWidget.addWidget(self.page_setalarm)
        self.page_edit = QWidget()
        self.page_edit.setObjectName(u"page_edit")
        self.gridLayout_11 = QGridLayout(self.page_edit)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.verticalSpacer_7 = QSpacerItem(20, 58, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_11.addItem(self.verticalSpacer_7, 0, 2, 1, 1)

        self.horizontalSpacer_22 = QSpacerItem(68, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_22, 1, 0, 1, 1)

        self.timeEdit_2 = QTimeEdit(self.page_edit)
        self.timeEdit_2.setObjectName(u"timeEdit_2")
        sizePolicy.setHeightForWidth(self.timeEdit_2.sizePolicy().hasHeightForWidth())
        self.timeEdit_2.setSizePolicy(sizePolicy)
        self.timeEdit_2.setFont(font2)
        self.timeEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.timeEdit_2.setAlignment(Qt.AlignCenter)
        self.timeEdit_2.setCurrentSection(QDateTimeEdit.HourSection)
        self.timeEdit_2.setTimeSpec(Qt.LocalTime)

        self.gridLayout_11.addWidget(self.timeEdit_2, 1, 1, 1, 3)

        self.horizontalSpacer_23 = QSpacerItem(68, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_23, 1, 4, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 38, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_11.addItem(self.verticalSpacer_9, 2, 2, 1, 1)

        self.horizontalSpacer_18 = QSpacerItem(198, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_18, 3, 0, 1, 2)

        self.btn_save_alarm = QPushButton(self.page_edit)
        self.btn_save_alarm.setObjectName(u"btn_save_alarm")
        self.btn_save_alarm.setFont(font3)
        self.btn_save_alarm.setStyleSheet(u"background-color: rgb(208, 208, 208);")

        self.gridLayout_11.addWidget(self.btn_save_alarm, 3, 2, 1, 1)

        self.horizontalSpacer_19 = QSpacerItem(208, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_19, 3, 3, 1, 2)

        self.horizontalSpacer_21 = QSpacerItem(198, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_21, 4, 0, 1, 2)

        self.btn_back_edit = QPushButton(self.page_edit)
        self.btn_back_edit.setObjectName(u"btn_back_edit")
        self.btn_back_edit.setFont(font3)
        self.btn_back_edit.setStyleSheet(u"background-color: rgb(208, 208, 208);")

        self.gridLayout_11.addWidget(self.btn_back_edit, 4, 2, 1, 1)

        self.horizontalSpacer_20 = QSpacerItem(208, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_20, 4, 3, 1, 2)

        self.verticalSpacer_8 = QSpacerItem(20, 58, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_11.addItem(self.verticalSpacer_8, 5, 2, 1, 1)

        self.stackedWidget.addWidget(self.page_edit)

        self.gridLayout_5.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 3)

        self.btn_alarm_add = QPushButton(self.tab_2)
        self.btn_alarm_add.setObjectName(u"btn_alarm_add")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_alarm_add.sizePolicy().hasHeightForWidth())
        self.btn_alarm_add.setSizePolicy(sizePolicy1)
        font4 = QFont()
        font4.setFamilies([u"Gill Sans Ultra Bold Condensed"])
        font4.setPointSize(12)
        self.btn_alarm_add.setFont(font4)
        self.btn_alarm_add.setStyleSheet(u"background-color: rgb(208, 208, 208);")

        self.gridLayout_6.addWidget(self.btn_alarm_add, 1, 1, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(468, 48, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_11, 1, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_4 = QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_7 = QSpacerItem(138, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)

        self.labelstopwatch = QLabel(self.tab_3)
        self.labelstopwatch.setObjectName(u"labelstopwatch")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.labelstopwatch.sizePolicy().hasHeightForWidth())
        self.labelstopwatch.setSizePolicy(sizePolicy2)
        font5 = QFont()
        font5.setFamilies([u"Seven Segment"])
        font5.setPointSize(60)
        self.labelstopwatch.setFont(font5)
        self.labelstopwatch.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.labelstopwatch)

        self.horizontalSpacer_6 = QSpacerItem(138, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)


        self.gridLayout_4.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 58, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_9 = QSpacerItem(94, 17, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_9)

        self.btnstartstopwatch = QPushButton(self.tab_3)
        self.btnstartstopwatch.setObjectName(u"btnstartstopwatch")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btnstartstopwatch.sizePolicy().hasHeightForWidth())
        self.btnstartstopwatch.setSizePolicy(sizePolicy3)
        font6 = QFont()
        font6.setFamilies([u"Seven Segment"])
        font6.setPointSize(20)
        font6.setBold(True)
        self.btnstartstopwatch.setFont(font6)
        self.btnstartstopwatch.setStyleSheet(u"background-color: rgb(208, 208, 208);")

        self.horizontalLayout.addWidget(self.btnstartstopwatch)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.btnresetstopwatch = QPushButton(self.tab_3)
        self.btnresetstopwatch.setObjectName(u"btnresetstopwatch")
        sizePolicy3.setHeightForWidth(self.btnresetstopwatch.sizePolicy().hasHeightForWidth())
        self.btnresetstopwatch.setSizePolicy(sizePolicy3)
        self.btnresetstopwatch.setFont(font6)
        self.btnresetstopwatch.setStyleSheet(u"background-color: rgb(208, 208, 208);")

        self.horizontalLayout.addWidget(self.btnresetstopwatch)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_8)

        self.btnstopstopwatch = QPushButton(self.tab_3)
        self.btnstopstopwatch.setObjectName(u"btnstopstopwatch")
        sizePolicy3.setHeightForWidth(self.btnstopstopwatch.sizePolicy().hasHeightForWidth())
        self.btnstopstopwatch.setSizePolicy(sizePolicy3)
        self.btnstopstopwatch.setFont(font6)
        self.btnstopstopwatch.setStyleSheet(u"background-color: rgb(208, 208, 208);")

        self.horizontalLayout.addWidget(self.btnstopstopwatch)

        self.horizontalSpacer_10 = QSpacerItem(95, 17, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_10)


        self.gridLayout_4.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 88, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 3, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_3 = QGridLayout(self.tab_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(58, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tb_hour_timer = QLineEdit(self.tab_4)
        self.tb_hour_timer.setObjectName(u"tb_hour_timer")
        self.tb_hour_timer.setFont(font1)
        self.tb_hour_timer.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tb_hour_timer.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.tb_hour_timer)

        self.label_2 = QLabel(self.tab_4)
        self.label_2.setObjectName(u"label_2")
        font7 = QFont()
        font7.setPointSize(40)
        self.label_2.setFont(font7)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.tb_minute_timer = QLineEdit(self.tab_4)
        self.tb_minute_timer.setObjectName(u"tb_minute_timer")
        self.tb_minute_timer.setFont(font1)
        self.tb_minute_timer.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tb_minute_timer.setCursorPosition(2)
        self.tb_minute_timer.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.tb_minute_timer)

        self.label = QLabel(self.tab_4)
        self.label.setObjectName(u"label")
        self.label.setFont(font7)

        self.horizontalLayout_2.addWidget(self.label)

        self.tb_second_timer = QLineEdit(self.tab_4)
        self.tb_second_timer.setObjectName(u"tb_second_timer")
        self.tb_second_timer.setFont(font1)
        self.tb_second_timer.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.tb_second_timer.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.tb_second_timer)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer_4 = QSpacerItem(58, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 68, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(128, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.btn_set_timer = QPushButton(self.tab_4)
        self.btn_set_timer.setObjectName(u"btn_set_timer")
        self.btn_set_timer.setFont(font6)
        self.btn_set_timer.setStyleSheet(u"background-color: rgb(208, 208, 208);")

        self.horizontalLayout_3.addWidget(self.btn_set_timer)

        self.btn_start_timer = QPushButton(self.tab_4)
        self.btn_start_timer.setObjectName(u"btn_start_timer")
        self.btn_start_timer.setFont(font6)
        self.btn_start_timer.setStyleSheet(u"background-color: rgb(208, 208, 208);\n"
"")

        self.horizontalLayout_3.addWidget(self.btn_start_timer)

        self.btn_reset_timer = QPushButton(self.tab_4)
        self.btn_reset_timer.setObjectName(u"btn_reset_timer")
        self.btn_reset_timer.setFont(font6)
        self.btn_reset_timer.setStyleSheet(u"background-color: rgb(208, 208, 208);")

        self.horizontalLayout_3.addWidget(self.btn_reset_timer)

        self.btn_stop_timer = QPushButton(self.tab_4)
        self.btn_stop_timer.setObjectName(u"btn_stop_timer")
        font8 = QFont()
        font8.setFamilies([u"Seven Segment"])
        font8.setPointSize(20)
        font8.setBold(True)
        font8.setItalic(False)
        font8.setUnderline(False)
        font8.setStrikeOut(False)
        self.btn_stop_timer.setFont(font8)
        self.btn_stop_timer.setStyleSheet(u"background-color: rgb(208, 208, 208);")

        self.horizontalLayout_3.addWidget(self.btn_stop_timer)

        self.horizontalSpacer_2 = QSpacerItem(128, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 730, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"IRAN Local Time:", None))
        self.irantime.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"GERMANY Local Time:", None))
        self.germanytime.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"USA Local Time:", None))
        self.usatime.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"World Clock", None))
        self.timeEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"hh:mm ", None))
        self.btn_set_alarm.setText(QCoreApplication.translate("MainWindow", u"SET ALARM", None))
        self.btn_back.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.timeEdit_2.setDisplayFormat(QCoreApplication.translate("MainWindow", u"hh:mm ", None))
        self.btn_save_alarm.setText(QCoreApplication.translate("MainWindow", u"Save Changes", None))
        self.btn_back_edit.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.btn_alarm_add.setText(QCoreApplication.translate("MainWindow", u"Add New\n"
"alarm", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Alarm", None))
        self.labelstopwatch.setText(QCoreApplication.translate("MainWindow", u"0:0:0", None))
        self.btnstartstopwatch.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.btnresetstopwatch.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.btnstopstopwatch.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Stop Watch", None))
        self.tb_hour_timer.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.tb_minute_timer.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.tb_second_timer.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.btn_set_timer.setText(QCoreApplication.translate("MainWindow", u"set", None))
        self.btn_start_timer.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.btn_reset_timer.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.btn_stop_timer.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Timer", None))
    # retranslateUi

