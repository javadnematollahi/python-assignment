import time
from PySide6.QtCore import QThread,Signal
from datetime import datetime
import pytz


class WorldclockThread(QThread):
    
    signal_show=Signal(str,str,str)

    def __init__(self):
        super().__init__()



    def run(self):
        while True:
            iran = datetime.now(pytz.timezone('Iran')).strftime("%H:%M:%S")
            us = datetime.now(pytz.timezone('US/Eastern')).strftime("%H:%M:%S")
            germany = datetime.now(pytz.timezone('Europe/Berlin')).strftime("%H:%M:%S")
            self.signal_show.emit(iran,us,germany)
            time.sleep(1)