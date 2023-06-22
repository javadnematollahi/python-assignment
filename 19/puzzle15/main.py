import sys
import random
from functools import partial
from PySide6.QtWidgets import QApplication, QMainWindow,QMessageBox
from Puzzle_ui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.list=[]
        self.count=0
        self.bottuns=[[self.ui.btn1,self.ui.btn2,self.ui.btn3,self.ui.btn4],
                      [self.ui.btn5,self.ui.btn6,self.ui.btn7,self.ui.btn8],
                      [self.ui.btn9,self.ui.btn10,self.ui.btn11,self.ui.btn12],
                      [self.ui.btn13,self.ui.btn14,self.ui.btn15,self.ui.btn16]]
        for i in range(16):
            self.list.append(i+1)
        for i in range(4):
            for j in range(4):
                r=random.randint(0,15-self.count)
                self.bottuns[i][j].setText(str(self.list[r]))
                self.bottuns[i][j].clicked.connect(partial(self.play,i,j))
                if self.list[r] == 16:
                    self.empty_i=i
                    self.empty_j=j
                    self.bottuns[i][j].setVisible(False)
                self.list.pop(r)
                self.count+=1


    def play(self,i,j):
        if (abs(j-self.empty_j)==1 and i==self.empty_i) or ((abs(i-self.empty_i)==1) and j==self.empty_j):
            self.bottuns[self.empty_i][self.empty_j].setText(self.bottuns[i][j].text())
            self.bottuns[i][j].setText("16")
            self.bottuns[self.empty_i][self.empty_j].setVisible(True)
            self.bottuns[i][j].setVisible(False)
            self.empty_i=i
            self.empty_j=j       

        if self.check_win()==True:
            msg_box=QMessageBox()
            msg_box.setText("تبریک")
            msg_box.exec()

    def check_win(self):
        index=1
        for i in range(4):
            for j in range(4):
                if int(self.bottuns[i][j].text())!=index:
                    return False
                index+=1
        return True


app=QApplication(sys.argv)

main_window = MainWindow()
main_window.show()

app.exec()