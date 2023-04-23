class Complex:
    def __init__(self,real,image):
        self.real= real
        self.image= image

    def show(self):
        print(self.real,"+","i",self.image)

    def sum(self,other):
        result_real=self.real+other.real
        result_image=self.image+other.image
        result=Complex(result_real,result_image)
        return result

    def sub(self,other):
        result_real=self.real-other.real
        result_image=self.image-other.image
        result=Complex(result_real,result_image)
        return result

    def mul(self,other):
        result_real=self.real*other.real - self.image*other.image
        result_image=self.real*other.image + self.image*other.real
        result=Complex(result_real,result_image)
        return result    



a= Complex(5,8)
a.show()

b=Complex(6,3)
b.show()

c=a.sum(b)
c.show()

c=a.sub(b)
c.show()

c=a.mul(b)
c.show()