from PySide6.QtWidgets import *
from PySide6 import QtCore
from mainwindow import Ui_mainWindow
import sys
from sudoku import Sudoku
from functools import partial
import random
from py_toggle import PyToggle


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_mainWindow()
        self.ui.setupUi(self)
        QMainWindow.setStyleSheet(self,"background-color: rgb(255, 201, 252);")
        self.lineedits=[[None for i in range(9)] for j in range(9)]
        self.label=QLabel()
        self.label.setText("DarkMode: ")
        self.label.setStyleSheet("font-weight: bold;font-size:24px")
        self.ui.horizontal_Layout.addWidget(self.label)
        self.toggle=PyToggle()
        self.dark=0
        self.ui.horizontal_Layout.addWidget(self.toggle)
        self.toggle.stateChanged.connect(self.darkcheck)
        for i in range(9):
            for j in range(9):

                new_cell=QLineEdit()
                new_cell.setMinimumWidth(50)
                new_cell.setMaximumHeight(150)
                new_cell.setAlignment(QtCore.Qt.AlignCenter)
                
                f=new_cell.font()
                f.setPointSize(20)
                new_cell.setFont(f)

                self.set_style(new_cell,i,j,self.dark)
                self.ui.grid_Layout.addWidget(new_cell,i,j)
                new_cell.textChanged.connect(partial(self.validation,i,j))
                self.lineedits[i][j]=new_cell     
        self.ui.menunew.triggered.connect(self.new_game)
        self.ui.menuopenfile.triggered.connect(self.open_file)
        self.ui.solve_current_puzzle.triggered.connect(self.solve)
        self.ui.Exit.triggered.connect(self.exit)
        self.ui.Back_to_game.triggered.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))
        self.ui.About.triggered.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.Help.triggered.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))
        self.new_game()

    def darkcheck(self):
        if self.toggle.isChecked():
            self.dark=3
            self.ui.label.setStyleSheet("background-color: rgb(147, 147, 147);")
            self.ui.label_2.setStyleSheet("background-color: rgb(147, 147, 147);")
        else:
            self.dark=0
            self.ui.label.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.ui.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        for i in range(9):
            for j in range(9):
                if self.puzzle.board[i][j]==None:
                    self.set_style(self.lineedits[i][j],i,j,self.dark)


    def exit(self):
        self.close()

    def set_style(self,cell,i,j,r):
        if r==0:
            color="background-color: rgb(255, 255, 255);"
        elif r==1:
            color="background-color: rgb(240, 206, 255);"
        elif r==2:
            color="background-color: rgb(255, 87, 90);"
        elif r==3:
            color="background-color: rgb(147, 147, 147);"
        
        if i%3==0 and j%3==0:
            cell.setStyleSheet(f"{color}border:1px solid;border-color: rgb(66, 66, 65);border-top: 4px solid;border-left: 4px solid;")
        elif i%3==0 and (j+1)%3==0:
            cell.setStyleSheet(f"{color}border:1px solid;border-color: rgb(66, 66, 65);border-top: 4px solid;border-right: 4px solid;")
        elif (i+1)%3==0 and j%3==0:
            cell.setStyleSheet(f"{color}border:1px solid;border-color: rgb(66, 66, 65);border-bottom: 4px solid;border-left: 4px solid;")
        elif (i+1)%3==0 and (j+1)%3==0:
            cell.setStyleSheet(f"{color}border:1px solid;border-color: rgb(66, 66, 65);border-bottom: 4px solid;border-right: 4px solid;")      
        elif (i)%3==0 and (j)%3==1:
            cell.setStyleSheet(f"{color}border:1px solid;border-color: rgb(66, 66, 65);border-top: 4px solid;")  
        elif (i+1)%3==0 and (j)%3==1:
            cell.setStyleSheet(f"{color}border:1px solid;border-color: rgb(66, 66, 65);border-bottom: 4px solid;")  
        elif i%3==1 and j%3==0:
            cell.setStyleSheet(f"{color}border:1px solid;border-color: rgb(66, 66, 65);border-left: 4px solid;")  
        elif i%3==1 and (j+1)%3==0:
            cell.setStyleSheet(f"{color}border:1px solid;border-color: rgb(66, 66, 65);border-right: 4px solid;")  
        else:
            cell.setStyleSheet(f"{color}border:1px solid;border-color: rgb(66, 66, 65);")  
        
            
    def validation(self,i,j,text):
        if text not in ['1','2','3','4','5','6','7','8','9']:
            self.lineedits[i][j].setText("")
        else:
            self.check(i,j)

            

    def open_file(self):
        filepath , _ = QFileDialog.getOpenFileName(self,"Open file ...")
        print(filepath)
        f=open(filepath,'r')
        big_text=f.read()
        rows=big_text.split('\n')
        puzzle_board=[[None for i in range(9)] for j in range(9)]
        for i in range(len(rows)):
            cell=rows[i].split(' ')
            for j in range(len(cell)):
                puzzle_board[i][j]=int(cell[j])
        check,text=self.check_valid_puzzle(puzzle_board)
        if check==False:
            msg_box=QMessageBox()
            msg_box.setText(str(text))
            msg_box.exec()
            return
        for i in range(9):
            for j in range(9):
                self.lineedits[i][j].setText("")
                self.set_style(self.lineedits[i][j],i,j,self.dark)
        for i in range(9):
            for j in range(9):
                self.lineedits[i][j].setReadOnly(False)
                if self.puzzle.board[i][j]!=0:
                    self.lineedits[i][j].setText(str(self.puzzle.board[i][j]))
                    self.lineedits[i][j].setReadOnly(True)
                    self.set_style(self.lineedits[i][j],i,j,1)
                else:
                    self.lineedits[i][j].setText("")

    def check_valid_puzzle(self,puzzle):
        puz = Sudoku(3, 3, board=puzzle)
        try:
            puz.solve(raising=True)
            return True,"puzzle is valid"
        except Exception as e:
            return False,f'puzzle is invalid\n{e}'




    def new_game(self):
        self.puzzle=Sudoku(3,seed=random.randint(1,1000)).difficulty(0.5)
        for i in range(9):
            for j in range(9):
                self.lineedits[i][j].setText("")
                self.set_style(self.lineedits[i][j],i,j,self.dark)

        for i in range(9):
            for j in range(9):
                self.lineedits[i][j].setReadOnly(False)
                if self.puzzle.board[i][j]!=None:
                    self.lineedits[i][j].setText(str(self.puzzle.board[i][j]))
                    self.lineedits[i][j].setReadOnly(True)
                    self.set_style(self.lineedits[i][j],i,j,1)
                else:
                    self.lineedits[i][j].setText("")


    def solve(self):
        puzz=self.puzzle.solve()  #.show_full()
        for i in range(9):
            for j in range(9):
                if self.puzzle.board[i][j]==None:
                    self.lineedits[i][j].setText(str(puzz.board[i][j]))


    def check(self,x,y):
        # check rows
        i=x;j=y
        for k in range(0,9): 
            if k!=j:
                number1= self.lineedits[i][j].text()
                number2= self.lineedits[i][k].text()
                if number1== number2:
                    print("row")
                    
                    self.set_style(self.lineedits[i][j],i,j,2)
                    return False
        # check columns
        i=x;j=y
        for k in range(0,9): 
            if k!=i:
                number1= self.lineedits[i][j].text()
                number2= self.lineedits[k][j].text()
                if number1== number2:
                    print(f'({k},{j})')
                    
                    self.set_style(self.lineedits[i][j],i,j,2)
                    print("column")
                    return False
        # check 3*3
        i=x//3;j=y//3
        a=x;b=y
        for r in range(0,3):
            for k in range(0,3):
                if r+(i*3)!=a or k+(j*3)!=b:
                    number1= self.lineedits[r+(i*3)][k+(j*3)].text()
                    number2= self.lineedits[a][b].text()
                    if number1== number2:
                        print(f'({r+(i*3)},{k+(j*3)})')
                        
                        self.set_style(self.lineedits[i][j],i,j,2)
                        print("square")
                        return False
        i=x;j=y
        self.set_style(self.lineedits[i][j],i,j,self.dark)
        for i in range(9):
            for j in range(9):
                if self.lineedits[i][j].text()=="":
                    return True
        msg_box=QMessageBox()
        msg_box.setText("Congragulation!")
        msg_box.exec()

                




if __name__=="__main__":
    app=QApplication(sys.argv)

    window=MainWindow()
    window.show()

    app.exec()