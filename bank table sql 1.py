# installed library mysql-connector-python




import mysql.connector

#creating connection 

class insert:
    def __init__(self):
        self.conn=mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "Sarvesh_1",
                database = "bank"
                )
        
    def personal_details(self,cid,fname,lname,addr,pn,an,pan):
        cur = self.conn.cursor() # creating cursor
        cur.execute(f"INSERT INTO PERSONALDETAILS VALUES({cid},'{fname}','{lname}','{addr}',{pn},'{an}','{pan}')")
        self.conn.commit()
        



