import math
from PySide6.QtGui import QFont

class Getnumber:
    def __init__(self,objec):
        self.a=0
        self.b=0
        self.c=0
        self.d=0
        self.equals=1
        self.count=0
        self.obj=objec
        self.define_operation=0
        self.font = QFont()

        
    def one(self):
        if self.equals==1:
            self.obj.result.setText("")
            self.equals=0
        self.a=self.obj.one.text()
        self.count+=1
        # if self.count>15:
        #     self.font.setFamilies([u"Times New Roman"])
        #     self.font.setPointSize(44-self.count)
        #     self.font.setBold(True)
        #     self.obj.result.setFont(self.font)
        if self.count<32:
            self.obj.result.setText(self.obj.result.text()+self.a)

            

    def two(self):
        if self.equals==1:
            self.obj.result.setText("")
            self.equals=0        
        self.a=self.obj.two.text()
        self.count+=1
        if self.count<32:
            self.obj.result.setText(self.obj.result.text()+self.a)


    def three(self):
        if self.equals==1:
            self.obj.result.setText("")
            self.equals=0
        self.a=self.obj.three.text()
        self.count+=1
        if self.count<32:
            self.obj.result.setText(self.obj.result.text()+self.a)
        
    def four(self):
        if self.equals==1:
            self.obj.result.setText("")
            self.equals=0
        self.a=self.obj.four.text()
        self.count+=1
        if self.count<32:
            self.obj.result.setText(self.obj.result.text()+self.a)

    def five(self):
        if self.equals==1:
            self.obj.result.setText("")
            self.equals=0
        self.a=self.obj.five.text()
        self.count+=1
        if self.count<32:
            self.obj.result.setText(self.obj.result.text()+self.a)

    def six(self):
        if self.equals==1:
            self.obj.result.setText("")
            self.equals=0
        self.a=self.obj.six.text()
        self.count+=1
        if self.count<32:
            self.obj.result.setText(self.obj.result.text()+self.a)

    def seven(self):
        if self.equals==1:
            self.obj.result.setText("")
            self.equals=0
        self.a=self.obj.seven.text()
        self.count+=1
        if self.count<32:
            self.obj.result.setText(self.obj.result.text()+self.a)

    def eight(self):
        if self.equals==1:
            self.obj.result.setText("")
            self.equals=0
        self.a=self.obj.eight.text()
        self.count+=1
        if self.count<32:
            self.obj.result.setText(self.obj.result.text()+self.a)

    def nine(self):
        if self.equals==1:
            self.obj.result.setText("")
            self.equals=0
        self.a=self.obj.nine.text()
        self.count+=1
        if self.count<32:
            self.obj.result.setText(self.obj.result.text()+self.a)

    def dot(self):
        if self.equals==1:
            self.obj.result.setText("")
            self.equals=0 
        self.a=self.obj.dot.text()
        self.count+=1
        if self.count<32:
            self.obj.result.setText(self.obj.result.text()+self.a)

    def zero(self):
        if self.equals==1:
            self.obj.result.setText("")
            self.equals=0
        self.a=self.obj.zero.text()
        self.count+=1
        if self.count<32:
            self.obj.result.setText(self.obj.result.text()+self.a)

    def add(self):
        self.count=0
        self.define_operation=1
        # if self.obj.result.text()=="":
        #     self.d=0
        # else:
        self.d=float(self.obj.result.text())

        self.obj.result.setText("")
        
    def sub(self):
        self.count=0
        self.define_operation=2
        # if self.obj.result.text()=="":
        #     self.d=0
        # else:
        self.d=float(self.obj.result.text())
        self.obj.result.setText("")

    def sqrt(self):
        self.equals=1
        try:
            self.d=float(self.obj.result.text())
            self.d=math.sqrt(self.d)
            self.obj.result.setText(str(self.d))
        except:
            self.obj.result.setText("Invalid input")

    def log(self):
        self.equals=1
        try:
            self.d=float(self.obj.result.text())
            self.d=math.log10(self.d)
            self.obj.result.setText(str(self.d))
        except:
            self.obj.result.setText("Invalid input")

    def sin(self):
        self.equals=1
        self.d=float(self.obj.result.text())  
        self.d=math.sin(math.radians(self.d))
        self.d=round(self.d, 4)
        self.obj.result.setText(str(self.d))

    def cos(self):
        self.equals=1
        self.d=float(self.obj.result.text())  
        self.d=math.cos(math.radians(self.d))
        self.d=round(self.d, 4)
        self.obj.result.setText(str(self.d))

    def tan(self):
        self.equals=1
        try:
            self.d=float(self.obj.result.text())  
            self.c=math.sin(math.radians(self.d))
            self.d=math.cos(math.radians(self.d))
            if round(self.d, 4)==0:
                self.d=round(self.d, 4)
            self.d=self.c/self.d
            self.d=round(self.d, 4)
            self.obj.result.setText(str(self.d))
        except:
            self.obj.result.setText("Invalid input for tan")

    def cot(self):
        self.equals=1
        try:
            self.d=float(self.obj.result.text())  
            self.d=math.tan(math.radians(self.d))
            self.d=1/self.d
            self.d=round(self.d, 4)
            self.obj.result.setText(str(self.d))
        except:
            self.obj.result.setText("Invalid input for cot")

    def zarb(self):
        self.count=0
        self.define_operation=3
        self.d=float(self.obj.result.text())
        self.obj.result.setText("")

    def taqsim(self):
        self.count=0
        self.define_operation=4
        self.d=float(self.obj.result.text())
        self.obj.result.setText("")

    def negote(self):
        check_type=0
        if self.count<32:
            self.d=float(self.obj.result.text())
            self.d=-self.d
            check_type=self.d*10
            if check_type%10==0:
                self.d=int(self.d)
            self.obj.result.setText(str(self.d))
                


    def ce(self):
        self.count=0
        self.obj.result.setText("0")

    def equal(self):
        check_type=0
        self.equals=1
        if self.define_operation==1:
            self.c=float(self.obj.result.text())
            self.b=self.d+self.c
            self.b=round(self.b, 8)
            check_type=self.b*10
            if check_type%10==0:
                self.b=int(self.b)
            check_type=0
            self.obj.result.setText(str(self.b))

        elif self.define_operation==2:
            self.c=float(self.obj.result.text())
            self.b=self.d - self.c
            self.b=round(self.b, 8)
            check_type=self.b*10
            if check_type%10==0:
                self.b=int(self.b)
            check_type=0
            self.obj.result.setText(str(self.b))

        elif self.define_operation==3:
            self.c=float(self.obj.result.text())
            self.b=self.d * self.c
            
            self.b=round(self.b, 8)
            check_type=self.b*10
            if check_type%10==0:
                self.b=int(self.b)
            check_type=0
            self.obj.result.setText(str(self.b))

        elif self.define_operation==4:
            self.c=float(self.obj.result.text())
            try:
                self.b=self.d / self.c
                self.b=round(self.b, 8)
                check_type=self.b*10
                if check_type%10==0:
                    self.b=int(self.b)
                check_type=0
                self.obj.result.setText(str(self.b))
            except:
                self.obj.result.setText("division by zero Error")


