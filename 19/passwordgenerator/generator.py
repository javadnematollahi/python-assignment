import sys
import random,string
from password_generate import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow,QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.generate.clicked.connect(self.generate)
        self.password=''
        self.digits=string.digits
        self.punctuation=string.punctuation
        self.upper=string.ascii_uppercase
        self.lowercase=string.ascii_lowercase



    def generate(self):
        if self.ui.weak.isChecked():
            self.password=self.choose(string.digits,1)+self.choose(string.punctuation,1)+self.choose(string.ascii_uppercase,1)+self.choose(string.ascii_lowercase,5)
        elif self.ui.medium.isChecked():
            self.password=self.choose(string.digits,2)+self.choose(string.punctuation,2)+self.choose(string.ascii_uppercase,2)+self.choose(string.ascii_lowercase,6)
        elif self.ui.strong.isChecked():
            self.password=self.choose(string.digits,3)+self.choose(string.punctuation,2)+self.choose(string.ascii_uppercase,3)+self.choose(string.ascii_lowercase,12)
        self.password=self.random_arrange(self.password)
        self.ui.showpass.setText(self.password)
        self.password=''

    def random_arrange(self,password):
        newarrange=''
        i=list(range(0,len(password)))
        for _ in range(len(password)):
            a=random.choice(i)
            newarrange+=password[a]
            i.remove(a)
        return newarrange
    
    def choose(self,collection,n):
        newarrange=''
        i=list(range(0,len(collection)))
        for _ in range(n):
            a=random.choice(i)
            newarrange+=collection[a]
            i.remove(a)
        return newarrange

app=QApplication(sys.argv)

main_window=MainWindow()
main_window.show()

app.exec()