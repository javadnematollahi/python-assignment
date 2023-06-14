from PySide6.QtWidgets import QApplication
from PySide6 import QtCore
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIntValidator,QDoubleValidator,QKeyEvent,QFont
import resources
from get_number import Getnumber

  


app=QApplication()
loader=QUiLoader()

my_calculator=loader.load("my_calculator.ui")
print(type(my_calculator))
getnum=Getnumber(my_calculator)
my_calculator.show()
my_calculator.result.setValidator(QDoubleValidator(-99,99,30))
my_calculator.result.setText("0")

# print(my_calculator.one.keyPressEvent(QtCore.Qt.Key_1))

my_calculator.one.clicked.connect(getnum.one)

my_calculator.two.clicked.connect(getnum.two)
my_calculator.three.clicked.connect(getnum.three)
my_calculator.four.clicked.connect(getnum.four)
my_calculator.five.clicked.connect(getnum.five)
my_calculator.six.clicked.connect(getnum.six)
my_calculator.seven.clicked.connect(getnum.seven)
my_calculator.eight.clicked.connect(getnum.eight)
my_calculator.nine.clicked.connect(getnum.nine)
my_calculator.zero.clicked.connect(getnum.zero)
my_calculator.add.clicked.connect(getnum.add)
my_calculator.sub.clicked.connect(getnum.sub)
my_calculator.zarb.clicked.connect(getnum.zarb)
my_calculator.taqsim.clicked.connect(getnum.taqsim)
my_calculator.ce.clicked.connect(getnum.ce)
my_calculator.negote.clicked.connect(getnum.negote)
my_calculator.sin.clicked.connect(getnum.sin)
my_calculator.cos.clicked.connect(getnum.cos)
my_calculator.tan.clicked.connect(getnum.tan)
my_calculator.cot.clicked.connect(getnum.cot)
my_calculator.sqrt.clicked.connect(getnum.sqrt)
my_calculator.log.clicked.connect(getnum.log)
my_calculator.dot.clicked.connect(getnum.dot)
my_calculator.equal.clicked.connect(getnum.equal)


app.exec()
