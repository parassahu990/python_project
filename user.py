import mysql.connector

con=mysql.connector.connect(host="localhost",user="root",passwd="Chalbhag@123",database="ticket")

cur=con.cursor()

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
#searchA()

def bookticket():
    a=searchA()
    dn=input("enter destination name ")
    tic=int(input("how many tickets you want to book "))
    p=a.get(dn)
    print("enter 1 to book AC tickets and 2 for Non AC tickets")
    c=int(input("enter your choice"))
    if c==1:
        print("total price",tic*p[0])
    elif c==2:
        print("total price",tic*p[1])
    ch=input("enter Y/y to confirm your ticket and n/N to decline")
    if ch=='y' or ch=='Y':
        remain=p[2]-tic
        q="update details set seats=%s where destination=%s"
        t=(remain,dn)
        cur.execute(q,t)
        con.commit()
        print("enjoy your ride")
    else:
        print("thank you")
#bookticket()

def menu():
  while True:
    print("1 to book a ticket")
    print("2 to display all destinations")
    print("3 to come back to privious menu ")
    ch=int(input("enter your choice "))
    if ch==1:
        bookticket()
    elif ch==2:
        searchA()
    elif ch==3:
        break
    else:
        print("please enter right choice!!!")
    













        
