import sqlite3,os,sys


class Database:
    def __init__(self):
        self.conn = sqlite3.connect("clock.db")
        self.cursor=self.conn.cursor() 



    def get_time_timer(self):
        query="SELECT * FROM timetimer"
        result=self.cursor.execute(query)
        tasks=result.fetchall()
        return tasks
    
    def get_alarm(self):
        query="SELECT * FROM timealarm"
        result=self.cursor.execute(query)
        tasks=result.fetchall()
        return tasks    

    def add_new_alarm(self,h,m,active):
        try:
            query= f"INSERT INTO timealarm('hour','minute','active') VALUES('{h}','{m}','{active}')"
            self.cursor.execute(query)
            self.conn.commit()
            return True
        except :
            return False

    def delete_alarm(self,id_num):
        query=f"DELETE FROM timealarm WHERE id={id_num}" 
        self.cursor.execute(query)
        self.conn.commit()



    def set_timer_time(self,window,thredtimer):
        query=f"UPDATE timetimer SET hour='{window.tb_hour_timer.text()}',minute='{window.tb_minute_timer.text()}',second='{window.tb_second_timer.text()}' WHERE id={0}"
        self.cursor.execute(query)
        self.conn.commit()
        thredtimer.time.hour=int(window.tb_hour_timer.text())
        thredtimer.time.minute=int(window.tb_minute_timer.text())
        thredtimer.time.second=int(window.tb_second_timer.text())
        thredtimer.firstshow()

    def update_alarm(self,id,h,m,active):
        try:
            query=f"UPDATE timealarm SET hour='{h}',minute='{m}',active='{active}' WHERE id={id}"
            self.cursor.execute(query)
            self.conn.commit()
            return True
        except:
            return False
