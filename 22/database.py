import sqlite3,os,sys


class Database:
    def __init__(self):
        # self.con=sqlite3.connect("todolist.db")
        self.conn = sqlite3.connect("todolist.db")
        self.cursor=self.conn.cursor() 



    def get_task(self):
        query="SELECT * FROM tasks"
        result=self.cursor.execute(query)
        tasks=result.fetchall()
        return tasks
    
    def add_new_tasks(self,new_title,new_description,priority,time):
        try:
            query= f"INSERT INTO tasks('title','description','priority') VALUES('{new_title}','{new_description}\n{time}',{priority})"
            self.cursor.execute(query)
            self.conn.commit()
            return True
        except :
            return False

    def remove_task(self,id_num,obj):
        query=f"DELETE FROM tasks WHERE id={id_num}" 
        self.cursor.execute(query)
        self.conn.commit()
        obj.read_from_database()



    def task_done(self,id_num,r):
        # print(r)
        # query_read_state=f"SELECT is_done FROM tasks WHERE id={id_num} "
        # result=self.cursor.execute(query_read_state)
        # state=result.fetchall()
        # state1=state[0][0]
        # if state1=='1':
        #     state1='0'
        # elif state1=='0': 
        #     state1='1'
        if r==2:
            r=1
        query=f"UPDATE tasks SET is_done='{r}' WHERE id={id_num}"
        self.cursor.execute(query)
        self.conn.commit()