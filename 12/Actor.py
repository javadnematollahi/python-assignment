

class Actor:
    def __init__(self,n,l,f,a,m):
        self.name=n
        self.lastname=l
        self.film=f
        self.age=a
        self.married=m

a=Actor('javad','nematollahi',['grbe','fol','sadeh'])
print(a.film)
