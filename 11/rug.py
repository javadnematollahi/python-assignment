class Rug():
    
    def __init__(self):
        self.lenght=int(input("Please enter an odd number: "))

    def make_rug(self):
        if self.lenght%2!=0:
            self.rug=[] 
            for i in range(self.lenght):
                 self.rug.append([0]*self.lenght)
            for i in range(self.lenght):
                for j in range(self.lenght):
                    #print(max(abs(self.lenght//2 - i),abs(self.lenght//2 - j)))
                    self.rug[i][j]=max(abs(self.lenght//2 - i),abs(self.lenght//2 - j))
            self.show_rug()
        else:
             print("Please enter an odd number")
    def show_rug(self):
            for i in range(self.lenght):
                 print(f"{self.rug[i][:]}\n")
                 
            
                   
                       
        
a=Rug()
a.make_rug()


