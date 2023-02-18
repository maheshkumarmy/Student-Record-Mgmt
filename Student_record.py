import sqlite3
# Importing tabulate module for better view in tabular format 
from tabulate import tabulate
# Sqlite3 database connection establishment with python
conn = sqlite3.connect('Student.db')

# Insert function to add the student record in existing db
def insertData():
    print("Enter the following data to insert in DataBase : ")
    a=int(input("Enter Student ID : "))
    b=input("Enter Student Name : ")
    c=input("Enter Student Dept : ")
    d=input("Enter Student Sex : ")
    e=float(input("Enter Student CGPA : "))
    f=input("Enter Student Location: ")
    # Query to be executed in DB
    q="insert into Student (SID,SName,Dept,Sex,CGPA,Location) values (?,?,?,?,?,?);"
    result=conn.execute(q,(a,b,c,d,e,f))
    # Commit method to save the changes in db
    conn.commit()
    print("Student details are inserted successfully.")

# Update function to modify the student record in existing db
def updateData():
    print("enter the following data to update in DataBase : ")
    a=int(input("Enter Student ID : "))
    b=input("Enter Student name : ")
    c=input("Enter Student Dept : ")
    d=input("Enter Student Sex : ")
    e=float(input("Enter Student CGPA : "))
    f=input("Enter Student Location : ")
    q="update Student set SName=?,Dept=?,Sex=?,CGPA=?,Location=? where SID=?; "
    conn.execute(q,(b,c,d,e,f,a))
    conn.commit()
    print("Student details are updated successfully.")

# Delete function to delete the student record from db
def deleteData():
    n=input("Enter Student ID to delete the Student record from DataBase :")
    q="delete from Student where SID=?;"
    conn.execute(q,(n))
    conn.commit()
    print("Student record for SID {} is deleted successfully. ".format(n))

# selectuniqueData function to return the unique student record where SID is used as a primary key.
def selectuniqueData():
    n=input("Enter the ID to see the Student record from DataBase :")
    q="select * from Student where SID=?;"
    result=conn.execute(q,(n))
    conn.commit()
    print("Student record for SID {} is found successfully. ".format(n))
    print(" ")
    print(tabulate(result,headers=["SID","SName","Dept","Sex","CGPA","Location"]))
    print(" ")
    
# selectallData function to return all the students record in db
def selectallData():
    q="select * from Student;"
    result=conn.execute(q)
    conn.commit()
    print("All Students record is found successfully. ")
    print(" ")
    print(tabulate(result,headers=["SID","SName","Dept","Sex","CGPA","Location"]))
    print(" ")

msg = '''
1. Insert
2. Update
3. Delete
4. Select Unique Student Record
5. Select All Students Record
6. Exit
'''
i='1'
while i=='1':
    print(msg)
    n = input("Enter your choice : ")
    if n=='1':
        insertData()
    elif n=='2':
        updateData()
    elif n=='3':
        deleteData()
    elif n=='4':
        selectuniqueData()
    elif n=='5':
        selectallData()
    elif n=='6':
        print("ThankYou....Bye....!!!")
        exit()
    else:
        print("Invalid inputs ....!")
    i = input("Enter 1 to continue : ")
    if i=='1':
        continue
    else:
        break
