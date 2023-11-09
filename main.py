
from create import insert

obj = insert()

print("------------- Baak Management System ---------------")
print("For Inserting the data press 1 : ")
print("For Reading the data press 2 : ")
print("For Updating the data press 3 : ")
print("For Deleting the data press 4 : ")

opr = int(input("Please enter your operation: "))

def myopr():
    print("---- For Personal information press 1 ----")
    print("---- For Bank details press 2 ------------")
    print("---- For transaction details press 3 -----")
    print("---- For Account details press 4 ---------")
    vr = int(input("Please Select your table : "))
    if vr == 1:
        return 'personaldetails'
    elif vr ==2:
        return 'bankdetails'
    elif vr ==3:
        return 'transactiondetails'
    elif vr ==4:
        return 'accountdetails'
    

if opr ==1:
    h = myopr() 
    if h=='personal_details':
        cid = int(input("please enter customer id:"))
        fname = input("please enter customer first name:")
        lname = input("please enter customer last name:")
        addr = input("please eneter customer address:")
        pn = int(input("please enter customer phone number:"))
        an = input("please enter customer aadhar number:")
        pan = input("please enter customer pan number:")
        obj.personal_details(cid,fname,lname,addr,pn,an,pan)

    elif h=='bank_details':
        acn = int(input("please enter account number:"))
        cid = int(input("please enter customerid:"))
        ifsc = input("please enter ifsc code:")
        actype = input("please enter account type:")
        obj.bank_details(acn,cid,ifsc,actype)
    

    elif h == 'transactiondetails':
        tid = int(input("please enter transaction id:"))
        sac = int(input("please enter sender account:"))
        rac = int(input("please enter receiver account:"))
        amt = int(input("please enter amount:"))
        mthd = input("please enter method type:")

        obj.transaction_details(tid,sac,rac,amt,mthd)
    
    elif h == 'accountdetails':
        accn = int(input("please enter account number:"))
        amt = int(input("please enter amount:"))
        cbal = int(input("please enter closing balance:"))
        tid = int(input("please enter transaction id:"))
        transtype=input("please enter transactiontype")
        obj.account_details(accn,amt,cbal,tid,transtype)

#read
from read import read
objread = read()
if opr==2: # user wanted to read the data
    j = myopr()
    cusid = int(input("please enter customer id for fetching data"))
    objread.specific_info(cusid,j)

#update
# installed library mysql-connector-python
import mysql.connector

#creating connection 

class update:
    def __init__(self):
        self.conn = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "Sarvesh_1",
                database = "bank"
                )
        
    def myupdate(self,table_name,column_name,new_value,cusid):
        cur = self.conn.cursor()
        if new_value.isnumeric():
            print("test1")
            cur.execute(f"UPDATE {table_name} set {column_name}={int(new_value)} where customerid={cusid}")
        else:
            print("test2")
            cur.execute(f"UPDATE {table_name} set {column_name}='{new_value}' where customerid={cusid}")
        self.conn.commit()
        print("updated sucessfully")


from update import update
objupdate = update()
if opr ==3:
    j = myopr()
    cusid = int(input("please enter customer id for fetching data"))
    colname = input("please enter column name:")
    newval = input("please enter new values:") # 500 str # 'jhon'
    objupdate.myupdate(j,colname,newval,cusid)

#delete
from delete import delete
objdelete = delete()

if opr ==4:
    k = myopr()
    cusid = int(input("please enter customer id to delete the data: "))
    objdelete.specific_del(k,cusid)





