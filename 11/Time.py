class Time:
    fix_need=0
    def __init__(self,hh,mm,ss):
        self.hour=hh
        self.minute=mm 
        self.second=ss
        self.fix()
 

    def show(self):
        print(self.hour,":",self.minute,":",self.second)

    def sum(self, other):
        s_new=self.second+other.second
        m_new=self.minute+other.minute
        h_new=self.hour+other.hour
        Time.fix_need=1
        result=Time(h_new,m_new,s_new)
        return result
    
    def sub(self, other):
        s_new=self.second-other.second
        m_new=self.minute-other.minute
        h_new=self.hour-other.hour
        Time.fix_need=1
        result=Time(h_new,m_new,s_new)
        return result
    
    def second_to_time(self,second):
        Calculated_HOUR=second//3600
        b=second-3600*Calculated_HOUR
        Calculated_MINUTE=b//60
        Calculated_SECOND=b-60*Calculated_MINUTE
        result=Time(Calculated_HOUR,Calculated_MINUTE,Calculated_SECOND)
        return result
    
    def time_to_second(self, other):
        Calculated_SECOND= other.hour*3600 + other.minute*60 + other.second
        result=Calculated_SECOND
        return result

    def GMT_to_Tehrantime(self, GMT):
        tehan_s=0+GMT.second
        tehran_m=30+GMT.minute
        tehran_h=3+GMT.hour
        result=Time(tehran_h,tehran_m,tehan_s)
        return result

    def fix(self):
        if self.second >= 60:
            if self.fix_need==1:
                self.minute+=1
            self.second%=60
            
        if self.minute >=60:
            if self.fix_need==1:
               self.hour+=1
            self.minute%=60

        if self.hour >=24:
            self.hour%=24

        if self.second <0:
            self.second*=-1
            self.second%=60
            self.second=60-self.second
            if self.fix_need==1:
                self.minute-=1

        if self.minute <0:
            self.minute*=-1
            self.minute%=60
            self.minute=60-self.minute
            if self.fix_need==1:
                self.hour-=1

        if self.hour <0:
            self.hour*=-1
            self.hour%=24
            self.hour=24-self.hour
            if self.hour == 24:
                self.hour=0
        
        Time.fix_need=0



    



t1= Time(3,45,17)
t1.show()

t2=Time(4,13,23)
t2.show()

t3=t1.sum(t2)
t3.show()

t3=t1.sub(t2)
t3.show()