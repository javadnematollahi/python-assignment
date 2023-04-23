import time

class Time:
   
    def __init__(self,h,m,s):
        # properties
        self.second=s
        self.minute=m
        self.hour=h

    # methods
    def show_time(self):
        while(1):
            print("Current time is"+ str(self.hour)+":"+str(self.minute)+":"+str(self.second))
            time.sleep(1)
            self.second+=1
            if(self.second==60):
                self.second=0
                self.minute+=1
                if self.minute==60:
                    self.minute=0
                    self.hour+=1
                    if self.hour==24:
                        self.hour=0
            
    def set_time(self):
        pass
    def time_correct(self):
        pass


user_time=Time(0,0,0)
user_time.show_time()
     