import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="Chalbhag@123",database="ticket")
cur=con.cursor()

def first():
    q="create database ticket"
    cur.execute(q)
    con.commit()
#first()

def cr1():
    q="create table admin(user_id char(20),pwd char(30))"
    cur.execute(q)
    con.commit()
#cr1()

def cr2():
    q="create table details(destination char(40),acprice float(2),nonacprice float(2))"
    cur.execute(q)
    con.commit()
#cr2()

def incr1():
	user_id=input("enter user id")
	pas=input("create password")
	t=(user_id,pas)
	q="insert into admin values(%s,%s)"
	cur.execute(q,t)
	con.commit()
	print("data saved")
#incr1()
  
def authcheck():
	user_id=input("enter your user id")
	pas=input("enter your password")
	q="select * from admin"
	cur.execute(q)
	a=cur.fetchone()
	if a[0]==user_id and a[1]==pas:
		print("carry on")
	else:
		print("no matching")
		menu() #recursion

def insert():
    n=int(input("How many destination you want to add "))
    for i in range(n):
        d1=input("enter destination : ")
        p1=float(input("enter ac ticket price : "))
        p2=float(input("enter non ac ticket price : "))
        s=float(input("enter number of seats "))
        t=(d1,p1,p2,s)
        q="insert into details values(%s,%s,%s,%s)"
        cur.execute(q,t)
        con.commit()
#insert()

def searchA():
    q="select * from details"
    cur.execute(q)
    records=cur.fetchall()
    d={}
    count=1
    for a in records:
        print()
        print("Destination  ",a[0])
        print("AC price: ",a[1])
        print("Non AC price: ",a[2])
        print("total seats: ",a[3])
        d[a[0]]=[a[1],a[2],a[3]]
        count+=1
    return d

def updateACprice():
    m=input("enter destination name whose price you want to update ")
    p=float(input("enter new acprice "))
    q="update details set acprice=%s where destination=%s"
    t=(p,m)
    cur.execute(q,t)
    con.commit()
    print("data updated")


def updateNONACprice():
    m=input("enter destination name whose price you want to update ")
    n=float(input("enter new nonacprice "))
    r="update details set nonacprice=%s where destination=%s"
    t=(n,m)
    cur.execute(r,t)
    con.commit()
    print("data updated")


    
def delete():
    searchA()
    m=input("enter destination that you want to delete ")
    t=(m,)
    q="delete from details where destination=%s"
    cur.execute(q,t)
    con.commit()
    print("data deleted")


def menu():
    authcheck()
    print("-"*12,"BUS MANAGEMENT SYSTEM","-"*12)
    while True:        
        print("enter 1 to insert new records")
        print("enter 2 to delete a record")
        print("enter 3 to display all records")
        print("enter 4 to update AC Price")
        print("enter 5 to to update Non AC price")
        print("enter 6 to exit")
        c=int(input("enter your choice "))
        if c==1:
            insert()
        elif c==2:
            delete()
        elif c==3:
            searchA()
        elif c==4:
            updateACprice()
        elif c==5:
            updateNONACprice()
        elif c==6:
            print("thank you")
            break











		
