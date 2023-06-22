import sys
from PySide6.QtWidgets import QMainWindow,QApplication
from line_breaker import Ui_MainWindow
import pyperclip



class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.linebreaker.clicked.connect(self.convert)
        self.ui.copytoclip.clicked.connect(self.copy)


    def convert(self):
        newtext=''
        newtext=self.ui.input.toPlainText()

        if self.ui.lbreaker.isChecked():
            newtext=newtext.replace("\n","")

        elif self.ui.pbreaker.isChecked():
            newtext=newtext.replace("\r\n","")
            newtext=newtext.replace("\n","")
        self.ui.output.clear()
        self.ui.output.setPlainText(newtext)

    def copy(self):
        pyperclip.copy(self.ui.output.toPlainText())







app=QApplication(sys.argv)

main_window=Mainwindow()
main_window.show()

app.exec()