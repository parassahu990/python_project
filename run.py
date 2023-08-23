import mysql.connector
import admin, user
con=mysql.connector.connect(host="localhost",user="root",passwd="Chalbhag@123",database="ticket")

def panel():
    while True:
        print("-"*10,"BUS MANAGEMENT SYSTEM","-"*10)
        print("select 1 for admin pannel")
        print("select 2 for user pannel")
        ch=int(input("enter your choice "))
        try:
            if ch==1:
                admin.menu()
            elif ch==2:
                user.menu()
            else:
                print("invalid choice")
        except:
            print("please enter right value")
panel()

