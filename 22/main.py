import sys,os
from PySide6.QtWidgets import *
from PySide6.QtCore import *

from main_window import Ui_MainWindow
from database import Database
from functools import partial

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.db=Database()
        self.new=0
        self.lablelist=[]
        self.checkboxlist=[]
        self.btnlist=[]
        self.read_from_database()
        self.count_for_latest_task=[]

        self.ui.btn_new_task.clicked.connect(self.newtask)



    def read_from_database(self):
        for i in range(len(self.btnlist)):
            self.btnlist[i].deleteLater()
            self.checkboxlist[i].deleteLater()
            self.lablelist[i].deleteLater()
        self.btnlist.clear();self.checkboxlist.clear();self.lablelist.clear()

        self.tasks=self.db.get_task()
        #sort tasks by done or not done
        self.tasks.sort(key=lambda x: x[3])
        for i in range(len(self.tasks)):
            
            if self.new==1:
                self.new=0
                self.count_for_latest_task.append(self.tasks[len(self.tasks)-1][0])


            new_checkBox=QCheckBox()
            
            new_btn=QPushButton()
            new_label=QPushButton()
            new_btn.setText("\U0001F5D1")
            self.btnlist.append(new_btn);self.checkboxlist.append(new_label);self.lablelist.append(new_checkBox)

            new_label.setText(self.tasks[i][1])

            if self.tasks[i][4]=='1':
                new_label.setStyleSheet(u"QPushButton\n"
                                        "{\n"
                                        "background-color: rgb(255, 101, 90);\n"
                                        "}\n"
                                        "QPushButton::pressed\n"
                                        "{\n"
                                        "background-color: rgb(255, 101, 90);\n"
                                        "}\n"
                                        )
            elif self.tasks[i][4]=='0':
                new_label.setStyleSheet(u"QPushButton\n"
                                        "{\n"
                                        "background-color: rgb(145, 255, 139);\n"
                                        "}\n"
                                        "QPushButton::pressed\n"
                                        "{\n"
                                        "background-color: rgb(145, 255, 139);\n"
                                        "}\n"
                                        "")
            self.ui.gl_tasks.addWidget(new_btn,i,2)

            self.ui.gl_tasks.addWidget(new_label,i,1)
            self.ui.gl_tasks.addWidget(new_checkBox,i,0)

            new_checkBox.setChecked(int(self.tasks[i][3]))
            # new_btn.clicked.connect(partial(new_btn.close))
            # new_btn.clicked.connect(partial(new_label.close))
            # new_btn.clicked.connect(partial(new_label2.close))
            # new_btn.clicked.connect(partial(new_checkBox.close))
            
            new_btn.clicked.connect(partial(self.db.remove_task,self.tasks[i][0],self))
            new_label.clicked.connect(partial(self.showdescription,self.tasks[i][2]))
            new_btn.setFixedWidth(40)
            new_checkBox.setFixedWidth(20)
            # I cant solve this part ,in partial i call self.db.task_done and i gave it one input
            #as I define in database.py in task_done function. but I gave this error:
            #TypeError: Database.task_done() takes 2 positional arguments but 3 were given
            #and I force to define a new input for task_done function that name is r and its 
            # after I print its value I know its 2 when I marked the checkbox.
            new_checkBox.stateChanged.connect(partial(self.db.task_done,self.tasks[i][0]))
            

    def newtask(self):
        self.new=1
        newtitle=self.ui.tb_new_task.text()
        newdescription=self.ui.tb_new_task_description.toPlainText()
        time=self.ui.time.text()
        if self.ui.high.isChecked():
            priority='1'
        else:
            priority='0'
        feedback=self.db.add_new_tasks(newtitle,newdescription,priority,time)
        if feedback==True:
            self.read_from_database()
            self.ui.tb_new_task.setText("")
            self.ui.tb_new_task_description.setText("")
        else:
            msg_box=QMessageBox()
            msg_box.setText("error")
            msg_box.exec()

    def showdescription(self,text):
            msg_box=QMessageBox()
            msg_box.setText(text)
            msg_box.exec()





if __name__=="__main__":
    app=QApplication(sys.argv)

    mainwindow=MainWindow()
    mainwindow.show()

    app.exec()
