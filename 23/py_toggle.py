from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class PyToggle(QCheckBox):
    def __init__(self,
                 width=60,
                 bg_color='8777',
                 circle_color="#DDD",
                active_color="#00BCff" ):
        QCheckBox.__init__(self)

        self.setFixedSize(width,28)
        self.setCursor(Qt.PointingHandCursor)

        self.bg_color=bg_color
        self.circle_color=circle_color
        self.active_color=active_color

        self.stateChanged.connect(self.debug)


    def debug(self):
        ...

    def hitButton(self,pos:QPoint):
        return self.contentsRect().contains(pos)

    def paintEvent(self,e):
        p=QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)

        p.setPen(Qt.NoPen)

        rect=QRect(0,0,self.width(),self.height())
        if not self.isChecked():

            p.setBrush(QColor(self.bg_color))
            p.drawRoundedRect(0,0,rect.width(),self.height(),self.height()/2,self.height()/2)

            p.setBrush(QColor(self.circle_color))
            p.drawEllipse(3,3,22,22)

        else:
            p.setBrush(QColor(self.active_color))
            p.drawRoundedRect(0,0,rect.width(),self.height(),self.height()/2,self.height()/2)

            p.setBrush(QColor(self.circle_color))
            p.drawEllipse(self.width()-26,3,22,22)

        p.end()
