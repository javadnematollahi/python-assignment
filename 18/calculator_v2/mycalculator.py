from functools import partial
from PySide6.QtWidgets import QApplication
from PySide6 import QtCore
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIntValidator,QDoubleValidator,QKeyEvent,QFont
from get_number import Getnumber

  


app=QApplication()
loader=QUiLoader()

my_calculator=loader.load("my_calculator.ui")
print(type(my_calculator))
getnum=Getnumber(my_calculator)
my_calculator.show()
my_calculator.result.setValidator(QDoubleValidator(-99,99,30))
my_calculator.result.setText("0")




for i in range(6):
    for j in range(4):
            getnum.buttons[i][j].clicked.connect(partial(getnum.func[i][j],i,j))



app.exec()
