from functools import partial
import sys
import random
from PySide6.QtWidgets import QApplication,QMessageBox
from PySide6.QtUiTools import QUiLoader

# variable hae list niazi be global kardan nadarand va dakhel tavabe ham ghabel 
# dastresi va taqir hastand

#vali variable hae mamoli ra hatman bayad global tarif kard ta dakhele tavabe
# ghabel dastres bashad


def computer():
    global wingame,player
    if main_window.pvc.isChecked() and wingame==0:
        if len(bottun_clicked)==0:
            btn_computer=bottuns[random.randint(0,2)][random.randint(0,2)]
            btn_computer.setText("O")
            btn_computer.setStyleSheet("color: red;background-color:pink;")
        else:
            while True:
                btn_computer=bottuns[random.randint(0,2)][random.randint(0,2)]
                for k in bottun_clicked:
                    if btn_computer==k:
                        break
                else:
                    btn_computer.setText("O")
                    btn_computer.setStyleSheet("color: red;background-color:pink;")
                    break
        main_window.turn.setText(f"Turn:Player1")
        player=1 
        bottun_clicked.append(btn_computer)
        check()


def newgame():
    global wingame,player
    for i in range(3):
        for j in range(3):
            bottuns[i][j].setText("")
            bottuns[i][j].setStyleSheet("color: red;background-color:white;")
    bottun_clicked.clear()
    text=main_window.round.text()
    text=text.split(":")
    main_window.round.setText(f"Round:{int(text[1])+1}")
    wingame=0
    if player==1:
        main_window.turn.setText(f"Turn:Player1")
    elif player==2:
        main_window.turn.setText(f"Turn:Player2")
    if player==2 and main_window.pvc.isChecked():
        check()


def play(row,col):
    global player,wingame  # واجب
    global bottuns  # مستحب
    if wingame==0:
        for i in bottun_clicked:
            if i==bottuns[row][col]:
                break
        else:
            if player==1:
                bottuns[row][col].setText("X")
                bottuns[row][col].setStyleSheet("color: blue; background-color:lightblue")
                main_window.turn.setText(f"Turn:Player2")
                player=2  
            elif player==2:
                # if main_window.pvc.isChecked()==False:
                bottuns[row][col].setText("O")
                bottuns[row][col].setStyleSheet("color: red;background-color:pink;")
                main_window.turn.setText(f"Turn:Player1")
                player=1 
            bottun_clicked.append(bottuns[row][col])

        check() 
    #  if msg_box ra global tarif konim messagebox baste nemishavad
# ya inke be jae show() az exec()  estefade konim ta baste nashavad

def check():
    global player
    checklist=["X","O"]
    
    global msg_box,wingame
    for j in range(len(checklist)):
        for i in range(3):
            if bottuns[i][0].text()==checklist[j]  and bottuns[i][1].text()==checklist[j] and bottuns[i][2].text()==checklist[j] or\
                bottuns[0][i].text()==checklist[j]  and bottuns[1][i].text()==checklist[j] and bottuns[2][i].text()==checklist[j] or\
                bottuns[0][0].text()==checklist[j]  and bottuns[1][1].text()==checklist[j] and bottuns[2][2].text()==checklist[j] or\
                bottuns[0][2].text()==checklist[j]  and bottuns[1][1].text()==checklist[j] and bottuns[2][0].text()==checklist[j] :
                msg_box=QMessageBox(text=f" بازیکن شماره {j+1} برنده شد")
                wingame=1
                # msg_box.exec()
                msg_box.show()
                if j+1==1:
                    text=main_window.player1score.text()
                    text1=text.split(":")
                    main_window.player1score.setText(f"Player1:{int(text1[1])+1}")
                    player=1
                    break
                elif j+1==2:
                    text=main_window.player2score.text()
                    text1=text.split(":")
                    main_window.player2score.setText(f"Player2:{int(text1[1])+1}")
                    player=2
                    break

    if len(bottun_clicked)==9 and wingame!=1:
            msg_box=QMessageBox(text= "مساوی!")
            text=main_window.player2score.text()
            text1=text.split(":")
            main_window.ties.setText(f"Ties:{int(text1[1])+1}")
            # msg_box.exec()
            wingame=2
            msg_box.show()
    if player==2:
        computer()


app=QApplication(sys.argv)

player=1
wingame=0
loader=QUiLoader()
main_window=loader.load("tiktaktoe.ui")
main_window.show()

bottun_clicked=[]
bottuns=[[main_window.btn_1,main_window.btn_2,main_window.btn_3],
         [main_window.btn_4,main_window.btn_5,main_window.btn_6],
         [main_window.btn_7,main_window.btn_8,main_window.btn_9]]

for i in range(3):
    for j in range(3):
        bottuns[i][j].clicked.connect(partial(play,i,j))

main_window.main.clicked.connect(lambda: main_window.stackedWidget.setCurrentWidget(main_window.page))
main_window.setting.clicked.connect(lambda: main_window.stackedWidget.setCurrentWidget(main_window.page_2))
main_window.about.clicked.connect(lambda: main_window.stackedWidget.setCurrentWidget(main_window.page_3))
main_window.newgame.clicked.connect(newgame)

app.exec()