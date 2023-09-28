
import sys
import time
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import QThread,Signal
from time1 import MyTime


class TimerThread(QThread):
    signal_show=Signal(MyTime,int)

    def __init__(self,h,m,s,db):
        super().__init__()
        self.hour=h
        self.minute=m
        self.second=s
        self.end=0
        self.time=MyTime(self.hour,self.minute,self.second)
        
    def run(self):
        while True:
            self.time.minus()
            self.signal_show.emit(self.time,self.end)
            time.sleep(1)
            if self.time.hour==0 and self.time.minute==0 and self.time.second==0:
                self.end=1
                break
        self.signal_show.emit(self.time,self.end)

    def firstshow(self):
        self.signal_show.emit(self.time,self.end)

    def reset(self,time):
        self.time.hour=time[0][0]
        self.time.minute=time[0][1]
        self.time.second=time[0][2]
        self.firstshow()
        
