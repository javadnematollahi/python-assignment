

class Date:
   
    def __init__(self):
        # properties
        self.day=None
        self.month=None
        self.year=None
        self.monthcorrect=0
        self.daycorrect=0

    # methods
    def show_date(self):
            print("Current date is:     "+ str(self.year)+"/"+str(self.month)+"/"+str(self.day))
      
            
    def set_date(self):
        self.set_year()
        self.set_month()
        self.set_day()

    def set_year(self):   
        if self.monthcorrect==0 or self.daycorrect==0:   
            self.year=int(input("Please enter year:"))
            if self.year<0:
                self.year_correct()
    def set_month(self): 
        if self.daycorrect==0:
            self.month=int(input("Please enter month:"))
            if self.month>12 or self.month<1:
                self.month_correct()
    def set_day(self): 
        self.day=int(input("Please enter day:"))
        if self.day>31 or self.day<1:
            self.day_correct()
        self.show_date()
    def year_correct(self):  
            print("Year cannot be smaller than 1")
            self.set_year()
    def month_correct(self): 
            self.monthcorrect=1
            print("Month cannot be bigger than 12 or smaller than 1")
            self.set_month()
    def day_correct(self): 
            self.daycorrect=1
            print("Day cannot be bigger than 31 or smaller than 1")
            self.set_day()


user_date=Date()
user_date.set_date()