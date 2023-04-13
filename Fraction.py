class Fraction:
    def __init__(self,s,m):
        # properties
        self.sorat=s
        self.makhraj=m

    # methods
    def define_type(self):
        print("this method defines type of the fraction:")
        if  self.makhraj%5==0 or self.makhraj%2==0:
            accumulator=0
            #print(self.makhraj//2)
            for i in range(2, self.makhraj//2+1):
                if  i%5!=0 and i%2!=0:
                    if self.makhraj%i==0: 
                        accumulator+=1
            print(accumulator)
            if accumulator>0 :
                print("Type of this Fraction is \"motenaveb morakab\"")
            if accumulator==0 :
                print("Type of this Fraction is \"makhtum\"")
        if (self.makhraj%5)!=0 and (self.makhraj%2)!=0:
            print("Type of this Fraction is \"motenaveb sade\"")

    def Answer_of_fraction(self):
        print("Answer is:")
        print(self.sorat/self.makhraj)


#example= 4/42
fraction1=Fraction(4,21)
fraction1.Answer_of_fraction()
fraction1.define_type()

        
        
