import sqlite3

class Database:
      def __init__(self):
            self.conn = sqlite3.connect("plate_database.db")
            self.cursor=self.conn.cursor() 
            self.cursor.execute('''
                  CREATE TABLE IF NOT EXISTS plates
                  ([plate_id] INTEGER PRIMARY KEY, [plate_owner] TEXT, [plate_text] TEXT, [entrance] TEXT)
                  ''')


      def get_plates(self):
            query="SELECT * FROM plates"
            result=self.cursor.execute(query)
            plates=result.fetchall()
            return plates

      def add_new_plate(self,plate_text,plate_owner,entrance=False):
            try:
                  if self.cursor.execute(f"SELECT 1 FROM plates WHERE plate_text = '{plate_text}'").fetchone() == None:
                        query= f"INSERT INTO plates('plate_text','plate_owner','entrance') VALUES('{plate_text}','{plate_owner}','{entrance}')"
                        self.cursor.execute(query)
                        self.conn.commit()
                  return True
            except :
                  return False

      def delete_plate(self,plate_id=None,plate_owner=None):
            try:
                  if plate_id != None:
                        query=f"DELETE FROM plates WHERE plate_id={plate_id}" 
                  elif plate_owner != None:
                        query=f"DELETE FROM plates WHERE plate_owner={plate_owner}" 
                  self.cursor.execute(query)
                  self.conn.commit()
                  return True
            except:
                  return False
            
      def edit_plate(self,plate_text=None,plate_owner=None ,entrance=None):
            try:
                  if plate_text != None:
                        query=f"UPDATE plates SET plate_text='{plate_text}' WHERE plate_owner={plate_owner}"
                  elif entrance != None:
                        query=f"UPDATE plates SET entrance='{entrance}' WHERE plate_owner={plate_owner}"
                  elif plate_owner != None:
                        query=f"UPDATE plates SET plate_owner='{plate_owner}' WHERE plate_owner={plate_owner}"
                  self.cursor.execute(query)
                  self.conn.commit()
                  return True
            except:
                  return False


      def add_default_plate(self):
            for i in range(20):
                  self.add_new_plate(f'56w5{32+i}36', f'nematollahi-{i}')