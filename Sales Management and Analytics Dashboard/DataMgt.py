import mysql.connector

class DataMgt: 
    con=mysql.connector.connect(
        host='localhost',
        username='root',
        password='1234',
        database='sales'
    )
    cur=con.cursor()

    pro_details={
        1001:['Hamam',63],
        1002:['lifeboy',80],
        1003:['aleogel',121]
    }

    def insertRecord(self,date,pro_code,qty):
        pro=self.pro_details[pro_code]
        total=qty*pro[1]
        #con.execute('create table sales_data(date text,pro_code int,pro_name text,price int,qty int,total int)')
        self.cur.execute('insert into sales_data values("{0}",{1},"{2}",{3},{4},{5})'.format(date,pro_code,pro[0],pro[1],qty,total))
        print("Data inserted ....")
        self.con.commit()

    def getRecord(self):
        self.cur.execute('select *from sales_data')
        rows=self.cur.fetchall()
        return rows
    
    def authAdmin(self):
        adminId=int(input("Enter Admin Id : "))
        adminPass=str(input("Enter Password : "))
        self.cur.execute('select *from admin_m where adminId = {0} and adminpass = "{1}"'.format(adminId,adminPass))
        row=self.cur.fetchone()
        return row
      
    def closeConn(self):
        self.con.close()
        print('DB Connection Closed')
