import time
from PySide6.QtCore import QThread,Signal
from time1 import MyTime



class StopWatchThread(QThread):

    signal_show=Signal(MyTime)

    def __init__(self):
        super().__init__()
        self.time=MyTime(0,0,0)



    def run(self):
        while True:
            self.time.plus()
            self.signal_show.emit(self.time)
            time.sleep(1)

    def reset(self):
        self.time.hour=0
        self.time.minute=0
        self.time.second=0
        self.signal_show.emit(self.time)