import time
from PySide6.QtCore import QThread,Signal
from datetime import datetime


class AlarmThread(QThread):

    signal_show=Signal(str)

    def __init__(self,window):
        super().__init__()
        self.window=window
       

    def run(self):
        while True:
            self.signal_show.emit(self.window.irantime.text())
            time.sleep(1)