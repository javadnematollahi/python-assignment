class Fraction:
    def __init__(self,ss,mm):
        self.s=ss
        self.m=mm

    def sum(self,f1):
        s=self.s * f1.m + self.m *f1.s
        m=self.m*f1.m
        x=Fraction(s,m)
        return x
    
    def mul(self,f1):
        result_s = f1.s * self.s
        result_m = f1.m * self.m
        x=Fraction(result_s,result_m)
        return x
    
    def sub(self,f1):
        result_s = self.s *f1.m - self.m * f1.s
        result_m = f1.m * self.m
        x=Fraction(result_s,result_m)
        return x

    def fraction(self,f1):
        result_s = f1.m * self.s
        result_m = f1.s * self.m
        x=Fraction(result_s,result_m)
        x1=x.Simplification()
        return x1

    def to_number(self):
        result =  self.s/self.m 
        return result

    def Simplification(self):
        if (self.m < self.s):
            y1=self.m;x1=self.s
        else:
            y1=self.s;x1=self.m

        while (y1 != 0):
            remainder = x1 % y1
            x1 = y1
            y1 = remainder

        r = x1
        result_s=(self.s // r)
        result_m=(self.m // r)
        x=Fraction(result_s,result_m)
        return x
    
    def show(self):
        print(self.s , "/" , self.m)


a=Fraction(20,36)
c=a.Simplification()
c.show()

b=Fraction(7,3)
b.show()
z1=b.sum(c)
z1.show()
z1=b.mul(c)
z1.show()
z1=b.sub(c)
z1.show()
z1=b.fraction(c)
z1.show()
z1=b.to_number()
print(z1)