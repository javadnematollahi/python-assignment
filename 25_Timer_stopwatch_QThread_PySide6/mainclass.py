import sys
import time
from functools import partial
from PySide6.QtWidgets import *
# from PySide6.QtGui import *
from PySide6.QtCore import Slot,QTime
# from PySide6.QtGui import QFrame
from clock import Ui_MainWindow
from timerthread import TimerThread
from stopwatchthread import StopWatchThread
from worldclockthread import WorldclockThread
from database import Database
from alarmthread import AlarmThread
from hline import QHLine
from toggle import PyToggle







class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_start_timer.clicked.connect(self.start_timer)
        self.ui.labelstopwatch.setText("0:0:0")
        self.ui.btnstartstopwatch.clicked.connect(self.start_stopwatch)
        self.ui.btnstopstopwatch.clicked.connect(self.stop_stopwatch)
        self.ui.btnresetstopwatch.clicked.connect(self.reset_stopwatch)
        self.ui.btn_stop_timer.clicked.connect(self.stop_timer)
        self.ui.btn_reset_timer.clicked.connect(self.reset_timer)
        
        
        self.clock_db=Database()
        time=self.clock_db.get_time_timer()
        self.worldclock=WorldclockThread()
        self.worldclock.signal_show.connect(self.show_time_iran)
        self.worldclock.start()

        self.thread_stopwatch=StopWatchThread()
        self.thread_stopwatch.signal_show.connect(self.show_time_stopwatch)

        self.thread_timer= TimerThread(time[0][0],time[0][1],time[0][2],self.clock_db)
        self.ui.btn_set_timer.clicked.connect(partial(self.clock_db.set_timer_time,self.ui,self.thread_timer))  
        self.thread_timer.signal_show.connect(self.show_time_timer)
        self.thread_timer.firstshow()

        self.thread_alarm=AlarmThread(self.ui)
        self.thread_alarm.signal_show.connect(self.check_time)
        self.thread_alarm.start()

        self.ui.btn_alarm_add.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_setalarm))
        self.ui.btn_back.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_alarms))
        self.ui.btn_back_edit.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_alarms))
        self.ui.btn_set_alarm.clicked.connect(self.set_alarm)
        self.ui.btn_save_alarm.clicked.connect(self.save_changes)

        self.edit_id=None

        self.show_alarms()
        
    def show_time_iran(self,iran,us,germany):
        self.ui.irantime.setText(iran)
        self.ui.germanytime.setText(germany)
        self.ui.usatime.setText(us)


    def save_changes(self):
        text=self.ui.timeEdit_2.dateTime()
        dt_string = text.toString(self.ui.timeEdit.displayFormat())
        time_list=dt_string.split(':')
        print(time_list)
        self.clock_db.update_alarm(self.edit_id,time_list[0],time_list[1],'1')
        self.edit_id=None
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_alarms)
        self.show_alarms()

    def set_alarm(self):
        text=self.ui.timeEdit.dateTime()
        dt_string = text.toString(self.ui.timeEdit.displayFormat())
        time_list=dt_string.split(':')
        alarms=self.clock_db.get_alarm()
        for alarm in alarms:
            if alarm[1]==time_list[0] and alarm[2]==time_list[1]:
                check=self.clock_db.update_alarm(alarm[0],time_list[0],time_list[1],1)
                break
        else:
            check=self.clock_db.add_new_alarm(time_list[0],time_list[1],1)
        if check==True:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_alarms)
            self.show_alarms()
        else:
            msg_box=QMessageBox()
            msg_box.setText("Something Wrong!\nTry Again")
            msg_box.exec()


    def show_alarms(self):
        self.clearall()
        self.ui.grid_alarm.addWidget(QHLine(), 0, 0, 1, 2)
        alarms=self.clock_db.get_alarm()
        self.ui.grid_alarm.addWidget(QHLine(), 0, 0, 1, 2)

        for i,alarm in enumerate(alarms):
            time_label=QLabel()
            time_label.setStyleSheet("font-size:40px;spacing: 20px;width:  60px;height: 60px; ")
            self.ui.grid_alarm.addWidget(time_label,i*2+1,0)
            self.ui.grid_alarm.addWidget(QHLine(), i*2+2, 0, 1, 2)
            time_label.setText(f"{alarm[1]}:{alarm[2]}")
            btn_edit=QPushButton()
            btn_remove=QPushButton()
            btn_edit.setText('Edit')
            btn_remove.setText('Remove')
            btn_edit.setFont("Gill Sans Ultra Bold Condensed")
            btn_remove.setFont("Gill Sans Ultra Bold Condensed")
            btn_remove.setStyleSheet("font-size:30px;background-color: rgb(208, 208, 208); ")
            btn_edit.setStyleSheet("font-size:30px;background-color: rgb(208, 208, 208); ")
            self.ui.grid_alarm.addWidget(btn_edit,i*2+1,1)
            self.ui.grid_alarm.addWidget(btn_remove,i*2+1,2)
            toggle=PyToggle()
            toggle.setChecked(int(alarm[3]))
            toggle.stateChanged.connect(partial(self.active_alarm,toggle,alarm[0],alarm[1],alarm[2]))
            btn_edit.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_edit))
            btn_edit.clicked.connect(partial(self.edit_alarm,alarm[0],alarm[1],alarm[2]))
            btn_remove.clicked.connect(partial(self.remove_alarm,alarm[0]))
            self.ui.grid_alarm.addWidget(toggle,i*2+1,3)

    def clearall(self):
        if self.ui.grid_alarm is not None:
            while self.ui.grid_alarm.count():
                child = self.ui.grid_alarm.takeAt(0)
                if child.widget() is not None:
                    child.widget().deleteLater()


    def active_alarm(self,toggle,id,h,m,t):
        if toggle.isChecked():
            self.clock_db.update_alarm(id,h,m,'1')
        else:
            self.clock_db.update_alarm(id,h,m,'0')

    def edit_alarm(self,id,h,m):
        self.ui.timeEdit_2.setTime(QTime(int(h), int(m)))
        self.edit_id=id


    def remove_alarm(self,id):
        self.clock_db.delete_alarm(id)
        self.show_alarms()


    def reset_timer(self):
        time=self.clock_db.get_time_timer()
        self.thread_timer.reset(time)

    @Slot()
    def check_time(self,text): 
        mytime=text.split(':')

        alarms=self.clock_db.get_alarm()
        for alarm in alarms:
            try:
                if int(alarm[1])==int(mytime[0]) and int(alarm[2])==int(mytime[1]) and int(alarm[3])==1:
                    self.clock_db.update_alarm(alarm[0],alarm[1],alarm[2],'0')
                    self.show_alarms()
                    msg_box=QMessageBox()
                    msg_box.setText("Your Alarm has come")
                    msg_box.exec()
            except:
                ...

    @Slot()
    def stop_stopwatch(self):
        self.thread_stopwatch.terminate()

    @Slot()
    def start_stopwatch(self):
        self.thread_stopwatch.start()

    @Slot()
    def reset_stopwatch(self):
        self.thread_stopwatch.reset()

    @Slot()
    def start_timer(self):
        self.thread_timer.start()

    @Slot()
    def stop_timer(self):
        self.thread_timer.terminate()

    @Slot()
    def show_time_timer(self,time,end):
        self.ui.tb_hour_timer.setText(str(time.hour))
        self.ui.tb_minute_timer.setText(str(time.minute))
        self.ui.tb_second_timer.setText(str(time.second))
        if end==1:
            self.thread_timer.end=0
            t=QMessageBox()
            t.setText("The time that you set has finised.")
            t.exec() 

    @Slot()
    def show_time_stopwatch(self,time):
        self.ui.labelstopwatch.setText(f"{time.hour}:{time.minute}:{time.second}")


app=QApplication(sys.argv)
window=Mainwindow()
window.show()


app.exec()
        