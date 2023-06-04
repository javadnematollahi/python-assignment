import sys
import cv2
import numpy as np
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from question5_encrypt import *
from question5_decrypt import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        layout=QVBoxLayout()
        pic_layout = QHBoxLayout()
        button_layout = QHBoxLayout()
        self.my_label=QLabel(self)
        self.image_BGR=0
        self.image_encrypt=0
        self.image_decrypt=0
        self.password=0
        # self.my_label.setFont("Times New Roman",18)
        # self.my_label.setStyleSheet('color:red')

        pic_layout.addWidget(self.my_label)

        layout.addLayout(button_layout)
        layout.addLayout(pic_layout)

        self.setGeometry(100,100,1000,500)
        self.setWindowTitle("Encrypt Image")
        self.setWindowIcon(QIcon('input/hand1.jpg'))

        btn= QPushButton("Encrypt",self)
        btn.setGeometry(50,50,140,50)
        btn.setFont(QFont("Sanserif",14))
        btn.setStyleSheet('background-color:white')
        btn.clicked.connect(self.encrypt)
        button_layout.addWidget(btn)


        btn= QPushButton("Decrypt",self)
        btn.setGeometry(50,200,140,50)
        btn.setFont(QFont("Sanserif",14))
        btn.setStyleSheet('background-color:white')
        btn.clicked.connect(self.decrypt)
        button_layout.addWidget(btn)

        btn= QPushButton("Upload Image",self)
        btn.setGeometry(50,350,140,50)
        btn.setFont(QFont("Sanserif",14))
        btn.setStyleSheet('background-color:white')
        btn.clicked.connect(self.upload)
        button_layout.addWidget(btn)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)




    def encrypt(self):
        enc=Encrypt(self.image_BGR)
        self.image_encrypt,self.password=enc.encrypt()
        image=cv2.cvtColor(self.image_encrypt,cv2.COLOR_BGR2RGB)
        image_qt=QImage(image,image.shape[1],image.shape[0],QImage.Format.Format_RGB888)
        image_qpixmap=QPixmap.fromImage(image_qt)
        self.my_label.setPixmap(image_qpixmap)
    def decrypt(self):
        dec=Decrypt(self.image_encrypt,self.password)
        self.image_decrypt=dec.decrypt()
        image=cv2.cvtColor(self.image_decrypt,cv2.COLOR_BGR2RGB)
        image_qt=QImage(image,image.shape[1],image.shape[0],QImage.Format.Format_RGB888)
        image_qpixmap=QPixmap.fromImage(image_qt)
        self.my_label.setPixmap(image_qpixmap)
    def upload(self):
        self.image_BGR=cv2.imread("input/AI.jpg")
        image=cv2.cvtColor(self.image_BGR,cv2.COLOR_BGR2RGB)
        image_qt=QImage(image,image.shape[1],image.shape[0],QImage.Format.Format_RGB888)
        image_qpixmap=QPixmap.fromImage(image_qt)
        self.my_label.setPixmap(image_qpixmap)

        self.my_label.frameSize()





if __name__=="__main__":
    app=QApplication(sys.argv)

    window=MyWindow()
    window.show()

    app.exec()