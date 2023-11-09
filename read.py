# installed library mysql-connector-python
import mysql.connector

#creating connection 

class read:
    def __init__(self):
        self.conn = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "Sarvesh_1",
                database = "bank"
                )
    
    def specific_info(self,customer_id,table_name):
        cur = self.conn.cursor()
        if table_name=='personaldetails' or table_name=='bankdetails':
            cur.execute(f"SELECT * FROM {table_name} WHERE CUSTOMERID={customer_id}")
            print(cur.fetchall())

        if table_name=='transactiondetails':
            cur.execute(f'''SELECT * FROM TRANSACTIONDETAILS WHERE TRANSACTIONID IN
                (SELECT TRANSACTIONID FROM ACCOUNTDETAILS WHERE ACCOUNT_NUMBER IN 
                (SELECT ACCOUNT_NUMBER FROM BANKDETAILS WHERE CUSTOMERID={customer_id}));
                        ''')
            print(cur.fetchall())
        