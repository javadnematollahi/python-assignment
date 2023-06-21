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

        self.buttons=[[self.obj.sin,self.obj.cos,self.obj.tan,self.obj.cot],
            [self.obj.log,self.obj.sqrt,self.obj.ce,self.obj.taqsim],
            [self.obj.seven,self.obj.eight,self.obj.nine,self.obj.zarb],
            [self.obj.four,self.obj.five,self.obj.six,self.obj.sub],
            [self.obj.one,self.obj.two,self.obj.three,self.obj.add],
            [self.obj.negote,self.obj.zero,self.obj.dot,self.obj.equal]]
        
        self.func=[[self.sin,self.cos,self.tan,self.cot],
                   [self.log,self.sqrt,self.ce,self.taqsim],
                   [self.num,self.num,self.num,self.zarb],
                   [self.num,self.num,self.num,self.sub],
                   [self.num,self.num,self.num,self.add],
                   [self.negote,self.num,self.num,self.equal]]
        

    def num(self,x,y):
        if self.equals==1:
            self.obj.result.setText("")
            self.equals=0        
        self.a=self.buttons[x][y].text()
        self.count+=1
        if self.count<32:
            self.obj.result.setText(self.obj.result.text()+self.a)


    def add(self,x,y):
        self.count=0
        self.define_operation=1
        # if self.obj.result.text()=="":
        #     self.d=0
        # else:
        self.d=float(self.obj.result.text())

        self.obj.result.setText("")
        
    def sub(self,x,y):
        self.count=0
        self.define_operation=2
        # if self.obj.result.text()=="":
        #     self.d=0
        # else:
        self.d=float(self.obj.result.text())
        self.obj.result.setText("")

    def sqrt(self,x,y):
        self.equals=1
        try:
            self.d=float(self.obj.result.text())
            self.d=math.sqrt(self.d)
            self.obj.result.setText(str(self.d))
        except:
            self.obj.result.setText("Invalid input")

    def log(self,x,y):
        self.equals=1
        try:
            self.d=float(self.obj.result.text())
            self.d=math.log10(self.d)
            self.obj.result.setText(str(self.d))
        except:
            self.obj.result.setText("Invalid input")

    def sin(self,x,y):
        self.equals=1
        self.d=float(self.obj.result.text())  
        self.d=math.sin(math.radians(self.d))
        self.d=round(self.d, 4)
        self.obj.result.setText(str(self.d))

    def cos(self,x,y):
        self.equals=1
        self.d=float(self.obj.result.text())  
        self.d=math.cos(math.radians(self.d))
        self.d=round(self.d, 4)
        self.obj.result.setText(str(self.d))

    def tan(self,x,y):
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

    def cot(self,x,y):
        self.equals=1
        try:
            self.d=float(self.obj.result.text())  
            self.d=math.tan(math.radians(self.d))
            self.d=1/self.d
            self.d=round(self.d, 4)
            self.obj.result.setText(str(self.d))
        except:
            self.obj.result.setText("Invalid input for cot")

    def zarb(self,x,y):
        self.count=0
        self.define_operation=3
        self.d=float(self.obj.result.text())
        self.obj.result.setText("")

    def taqsim(self,x,y):
        self.count=0
        self.define_operation=4
        self.d=float(self.obj.result.text())
        self.obj.result.setText("")

    def negote(self,x,y):
        check_type=0
        if self.count<32:
            self.d=float(self.obj.result.text())
            self.d=-self.d
            check_type=self.d*10
            if check_type%10==0:
                self.d=int(self.d)
            self.obj.result.setText(str(self.d))
                


    def ce(self,x,y):
        self.count=0
        self.obj.result.setText("0")

    def equal(self,x,y):
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


