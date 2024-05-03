from tkinter import *
from tkinter.messagebox import *
from zoneinfo import available_timezones
class Test:
    def bus_run(self):
        root=Tk()
        #Create the database in python
        import sqlite3
        con=sqlite3.Connection('Bus_Booking.db')
        cur=con.cursor()
        cur.execute('create table if not exists operator(Operator_ID number PRIMARY KEY,Name char(30),Address varchar(40),Phone number,Email varchar(40))')
        cur.execute('create table if not exists Bus(Bus_ID number PRIMARY KEY,Bustype varchar(30),Capacity number,Fare number,operator_i number,route_i number,foreign key(operator_i) references operator(Operator_ID),foreign key(route_i) references Route(Routeid))')
        cur.execute('create table if not exists Runs(Busi number ,Date varchar(25),Seat_available number,PRIMARY KEY(Busi,Date),foreign key(Busi) references Bus(Bus_ID))')
        cur.execute('create table if not exists Route(Routeid number,Stationid number,Station_name char(60),PRIMARY KEY(Routeid,Stationid))')
        cur.execute('create table if not exists Booking_history(passenger_name varchar(20), Gender varchar(12),No_of_seats number, mobile number PRIMARY KEY,age number,bus_select number,t_o varchar(13),fr varchar(13),date varchar(25),fare number)')

        root.title('Add Bus Running Details')
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
        img=PhotoImage(file='.\\Bus_for_project.png')
        img_home=PhotoImage(file='.\\home.png')
        Label(root,image=img).grid(row=0,column=6,columnspan=20)
        img_home=PhotoImage(file='.\\home.png')
        Label(root,text="Online Bus Booking System",font="Arial 22 bold",bg="light blue",fg="red").grid(row=1,column=6,columnspan=20)
        Label(root,text="").grid(row=2,column=0)
        Label(root,text="Add Bus Running Details",font="Arial 18 bold",fg='green').grid(row=3,column=6,columnspan=20)
        Label(root,text="                                                     ").grid(row=4,column=0)
        Label(root,text="").grid(row=5,column=0)
        Label(root,text="").grid(row=6,column=0)
        Label(root,text="").grid(row=7,column=0)
        Label(root,text="Bus ID",font="Arial 12 bold",fg="black").grid(row=8,column=4)
        Bus_ID=Entry(root,font="Arial 10 bold")
        Bus_ID.grid(row=8,column=5)
        Label(root,text="Running Date",font="Arial 12 bold",fg="black").grid(row=8,column=6)
        Running_Date=Entry(root,font="Arial 10 bold")
        Running_Date.grid(row=8,column=7)
        Label(root,text="Seat Available",font="Arial 12 bold",fg="black").grid(row=8,column=8)
        Seat_Available=Entry(root,font="Arial 10 bold")
        Seat_Available.grid(row=8,column=9)
        Label(root,text="").grid(row=8,column=10)
        def Add_Run():
            if(len(Bus_ID.get())!=0 and len(Running_Date.get())!=0 and len(Seat_Available.get())!=0):
                y=(Bus_ID.get(),Running_Date.get(),Seat_Available.get())
                query=('insert into Runs(Busi ,Date ,Seat_available) values(?,?,?)')
                cur.execute(query,y)
                con.commit()
                showinfo('Add Bus Entry','Bus Record Added')
                y1=(Bus_ID.get(),Running_Date.get())
                query1=('select * from Runs where Busi=? and Date=?')
                cur.execute(query1,y1)
                con.commit()
                result=cur.fetchall()
                Label(root,text=result,font="Arial 10 bold").grid(row=10,column=4,columnspan=30)
                print(result)
                Bus_ID.delete(0,END)
                Running_Date.delete(0,END)
                Seat_Available.delete(0,END)
            else:
                showerror('Value Missing','Please Enter The Correct Values')

        def Delete_Run():
             if len(Bus_ID.get())!=0 or len(Running_Date.get())!=0 or len(Seat_Available.get())!=0:
                y=(Bus_ID.get(),Running_Date.get())
                query='select * from Runs where Busi=? and Date=?'
                cur.execute(query,y)
                res=cur.fetchall()
                if(res):
                    showinfo('Found','record found')
                    y1=(Bus_ID.get(),Running_Date.get()) 
                    cur.execute('Delete from Runs where Busi=? and Date=?',y1)
                    con.commit()
                    showinfo('Bus Entry Deleted','Bus Record Deleted Successfully')
                    y1=(Bus_ID.get(),Running_Date.get())
                    query1=('select * from Runs where Busi=? and Date=?')
                    cur.execute(query1,y1)
                    con.commit()
                    result=cur.fetchall()
                    Label(root,text='     Deleted     ',font="Arial 10 bold").grid(row=10,column=4,columnspan=30)
                    print(result)
                    Bus_ID.delete(0,END)
                    Running_Date.delete(0,END)
                    Seat_Available.delete(0,END)
                else:
                    showinfo('Bus Entry ERORR!!','Please enter Busid and Date correctly')
             else:
                 showerror('Value Missing','Please Enter The Correct Values')  
                  
        Button(root,text="Add Run",bg="light green",fg="black",font="Arial 12 bold",command=Add_Run).grid(row=8,column=11)
        Label(root,text="").grid(row=8,column=12)
        Label(root,text="").grid(row=8,column=13)
        Label(root,text="").grid(row=8,column=14)
        Button(root,text="Delete Run",bg="light green",fg="red",font="Arial 12 bold",command=Delete_Run).grid(row=8,column=15)
        Label(root,text="").grid(row=9,column=0)
        Label(root,text="").grid(row=10,column=0)
        Label(root,text="").grid(row=11,column=0)
        def fun7():
            root.destroy()
            self.home()
        Button(root,image=img_home,command=fun7).grid(row=12,column=11)
        root.mainloop()
    #PAGE8
    def bus_route(self):
        root=Tk()
         #Create the database in python
        import sqlite3
        con=sqlite3.Connection('Bus_Booking.db')
        cur=con.cursor()
        cur.execute('create table if not exists operator(Operator_ID number PRIMARY KEY,Name char(30),Address varchar(40),Phone number,Email varchar(40))')
        cur.execute('create table if not exists Bus(Bus_ID number PRIMARY KEY,Bustype varchar(30),Capacity number,Fare number,operator_i number,route_i number,foreign key(operator_i) references operator(Operator_ID),foreign key(route_i) references Route(Routeid))')
        cur.execute('create table if not exists Runs(Busi number,Date varchar(25),Seat_available number,PRIMARY KEY(Busi,Date),foreign key(Busi) references Bus(Bus_ID))')
        cur.execute('create table if not exists Route(Routeid number,Station_name char(60),Stationid number,PRIMARY KEY(Routeid,Stationid))')
        cur.execute('create table if not exists Booking_history(passenger_name varchar(20), Gender varchar(12),No_of_seats number, mobile number PRIMARY KEY,age number,bus_select number,t_o varchar(13),fr varchar(13),date varchar(25),fare number)')


        root.title('Add Bus Route Details')
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
        img=PhotoImage(file='.\\Bus_for_project.png')
        img_home=PhotoImage(file='.\\home.png')
        Label(root,image=img).grid(row=0,column=5,columnspan=20)
        img_home=PhotoImage(file='.\\home.png')
        Label(root,text="Online Bus Booking System",font="Arial 22 bold",bg="light blue",fg="red").grid(row=1,column=5,columnspan=20)
        Label(root,text="").grid(row=2,column=0)
        Label(root,text="Add Bus Route Details",font="Arial 18 bold",fg='green').grid(row=3,column=5,columnspan=20)
        Label(root,text="                                                     ").grid(row=4,column=0)
        Label(root,text="").grid(row=5,column=0)
        Label(root,text="").grid(row=6,column=0)
        Label(root,text="").grid(row=7,column=0)
        Label(root,text="Route ID",font="Arial 12 bold",fg="black").grid(row=8,column=4)
        Route_ID=Entry(root,font="Arial 10 bold")
        Route_ID.grid(row=8,column=5)
        Label(root,text="Station Name",font="Arial 12 bold",fg="black").grid(row=8,column=6)
        Station_Name=Entry(root,font="Arial 10 bold")
        Station_Name.grid(row=8,column=7)
        Label(root,text="Station ID",font="Arial 12 bold",fg="black").grid(row=8,column=8)
        Station_ID=Entry(root,font="Arial 10 bold")
        Station_ID.grid(row=8,column=9)
        Label(root,text="").grid(row=8,column=10)
        def Add_Route():
            if(len(Route_ID.get())!=0 and len(Station_Name.get())!=0 and len(Station_ID.get())!=0):
                y=(Route_ID.get(),Station_Name.get(),Station_ID.get())
                query=('insert into Route(Routeid ,Station_name,Stationid) values(?,?,?)')
                cur.execute(query,y)
                con.commit()
                showinfo('Add Bus Entry','Bus Record Added')
                y1=(Route_ID.get(),Station_ID.get())
                query1=('select * from Route where Routeid=? and Stationid=?')
                cur.execute(query1,y1)
                con.commit()
                result=cur.fetchall()
                Label(root,text=result,font="Arial 10 bold").grid(row=10,column=4,columnspan=30)
                print(result)
                Route_ID.delete(0,END)
                Station_Name.delete(0,END)
                Station_ID.delete(0,END)
            else:
                showerror('Value Missing','Please Enter The Correct Values')   
        def Delete_Route():
            if len(Route_ID.get())!=0 or len(Station_Name.get())!=0 or len(Station_ID.get())!=0:
                y=(Route_ID.get(),Station_ID.get())
                query='select * from Route where Routeid=? and Stationid=?'
                cur.execute(query,y)
                res=cur.fetchall()
                if(res):
                    showinfo('Found','record found')
                    y1=(Route_ID.get(),Station_ID.get()) 
                    cur.execute('Delete from Route where Routeid=? and Stationid=?',y1)
                    con.commit()
                    showinfo('Bus Entry Deleted','Bus Record Deleted Successfully')
                    y1=(Route_ID.get(),Station_ID.get())
                    query1=('select * from Route where Routeid=? and Stationid=?')
                    cur.execute(query1,y1)
                    con.commit()
                    result=cur.fetchall()
                    Label(root,text='      Deleted         ',font="Arial 10 bold").grid(row=10,column=4,columnspan=30)
                    print(result)
                    Route_ID.delete(0,END)
                    Station_Name.delete(0,END)
                    Station_ID.delete(0,END)
                else:
                    showinfo('Bus Entry ERORR!!','Please enter Route id and Station id correctly')
            else:
                 showerror('Value Missing','Please Enter The Correct Values')       
        Button(root,text="Add Route",bg="light green",fg="black",font="Arial 12 bold",command=Add_Route).grid(row=8,column=11)
        Label(root,text="").grid(row=8,column=12)
        Label(root,text="").grid(row=8,column=13)
        Label(root,text="").grid(row=8,column=14)
        Button(root,text="Delete Route",bg="light green",fg="red",font="Arial 12 bold",command=Delete_Route).grid(row=8,column=15)
        Label(root,text="").grid(row=9,column=0)
        Label(root,text="").grid(row=10,column=0)
        Label(root,text="").grid(row=11,column=0)
        def fun8():
            root.destroy()
            self.home()
        Button(root,image=img_home,command=fun8).grid(row=12,column=11)
        root.mainloop()

    #PAGE7
    def bus_new(self):
        root=Tk()
        #Create the database in python
        import sqlite3
        con=sqlite3.Connection('Bus_Booking.db')
        cur=con.cursor()
        cur.execute('create table if not exists operator(Operator_ID number PRIMARY KEY,Name char(30),Address varchar(40),Phone number,Email varchar(40))')
        cur.execute('create table if not exists Bus(Bus_ID number PRIMARY KEY,Bustype varchar(30),Capacity number,Fare number,operator_i number,route_i number,foreign key(operator_i) references operator(Operator_ID),foreign key(route_i) references Route(Routeid))')
        cur.execute('create table if not exists Runs(Busi number,Date varchar(25),Seat_available number,PRIMARY KEY(Busi,Date),foreign key(Busi) references Bus(Bus_ID))')
        cur.execute('create table if not exists Route(Routeid number,Stationid number,Station_name char(60),PRIMARY KEY(Routeid,Stationid))')
        cur.execute('create table if not exists Booking_history(passenger_name varchar(20), Gender varchar(12),No_of_seats number, mobile number PRIMARY KEY,age number,bus_select number,t_o varchar(13),fr varchar(13),date varchar(25),fare number)')



        root.title("Add Bus Details Page")
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
        img=PhotoImage(file='.\\Bus_for_project.png')
        img_home=PhotoImage(file='.\\home.png')
        Label(root,image=img).grid(row=0,column=3,columnspan=20)
        img_home=PhotoImage(file='.\\home.png')
        Label(root,text="Online Bus Booking System",font="Arial 22 bold",bg="light blue",fg="red").grid(row=1,column=3,columnspan=20)
        Label(root,text="").grid(row=2,column=0)
        Label(root,text="Add Bus Details",font="Arial 18 bold",fg='green').grid(row=3,column=3,columnspan=20)
        Label(root,text="").grid(row=4,column=0)
        Label(root,text="").grid(row=5,column=0)
        Label(root,text="                                                   ").grid(row=6,column=4)
        Label(root,text="Bus ID",font="Arial 12 bold",fg="black").grid(row=6,column=1)
        Bus_ID=Entry(root,font='Arial 10 bold')
        Bus_ID.grid(row=6,column=2)
        Label(root,text="Bus Type",font="Arial 12 bold",fg="black").grid(row=6,column=3)
        Bus_type=StringVar()
        opt=["AC 2x2","AC 3x2","Non AC 2x2","Non AC 3x2","AC-Sleeper 2x1","Non AC-Sleeper 2x1"]
        d_menu=OptionMenu(root,Bus_type,*opt).grid(row=6,column=4,columnspan=10)
        Bus_type.set("Select_Bus_Type")
        Label(root,text="Capacity",font="Arial 12 bold").grid(row=6,column=14)
        Capacity=Entry(root,font='Arial 10 bold')
        Capacity.grid(row=6,column=15)
        Label(root,text="Fare Rs",font="Arial 12 bold").grid(row=6,column=16)
        Fare=Entry(root,font='Arial 10 bold')
        Fare.grid(row=6,column=17)
        Label(root,text="Operator ID",font="Arial 12 bold").grid(row=6,column=18)
        Operator_ID=Entry(root,font='Arial 10 bold')
        Operator_ID.grid(row=6,column=19)
        Label(root,text="Route ID",font="Arial 12 bold").grid(row=6,column=20)
        Route_ID=Entry(root,font='Arial 10 bold')
        Route_ID.grid(row=6,column=21)
        def Bus_Add():
                if len(Operator_ID.get())!=0 or len(Route_ID.get())!=0 or len(Fare.get())!=0 or len(Capacity.get())!=0 or len(Bus_ID.get())!=0:
                    y=(Bus_ID.get(),Bus_type.get(),Capacity.get(),Fare.get(),Operator_ID.get(),Route_ID.get())
                    query=('insert into Bus(Bus_ID ,bustype ,capacity,fare,operator_i,route_i) values(?,?,?,?,?,?)')
                    cur.execute(query,y)
                    con.commit()
                    showinfo('Add Bus Entry','Bus Record Added')
                    y1=(Bus_ID.get())
                    query1=('select * from Bus where Bus_ID=?')
                    cur.execute(query1,y1)
                    con.commit()
                    result=cur.fetchall()
                    Label(root,text=result,font="Arial 10 bold").grid(row=8,column=6,columnspan=30)
                    print(result)
                    Bus_ID.delete(0,END)
                    Capacity.delete(0,END)
                    Fare.delete(0,END)
                    Route_ID.delete(0,END)
                    Operator_ID.delete(0,END)
                else:
                    showerror('Value Missing','Please Enter The Correct Values')
        def Bus_Edit():
            if len(Operator_ID.get())!=0 or len(Route_ID.get())!=0 or len(Fare.get())!=0 or len(Capacity.get())!=0 or len(Bus_ID.get())!=0:
                y=(Bus_ID.get())
                query='select * from Bus where Bus_ID=?'
                cur.execute(query,y)
                res=cur.fetchall()
                if(res):
                    showinfo('Found','record found')
                    y1=(Bus_ID.get(),Bus_type.get(),Capacity.get(),Fare.get(),Operator_ID.get(),Route_ID.get(),Bus_ID.get()) 
                    cur.execute('UPDATE bus SET Bus_ID=? ,bustype=? ,capacity=? ,fare=?,operator_i=?,route_i=?  WHERE Bus_ID=?',y1)
                    con.commit()
                    showinfo('Bus Entry Edit','Bus Record Edited Successfully')
                    y2=(Bus_ID.get())
                    query1=('select * from Bus where Bus_ID=?')
                    cur.execute(query1,y2)
                    con.commit()
                    result=cur.fetchall()
                    Label(root,text=result,font="Arial 10 bold").grid(row=8,column=6,columnspan=30)
                    print(result)
                    Bus_ID.delete(0,END)
                    Capacity.delete(0,END)
                    Fare.delete(0,END)
                    Route_ID.delete(0,END)
                    Operator_ID.delete(0,END)
                else:
                    showinfo('Bus Entry ERORR!!','Bus Record Not Found')
            else:
                showerror('Value Missing','Please Enter The Correct Values')        
        Label(root,text="").grid(row=7,column=0)
        Label(root,text="").grid(row=8,column=0)
        Label(root,text="  ").grid(row=9,column=0)
        Button(root,text="Add Bus",font="Arial 12 bold",fg="black",bg="light green",command=Bus_Add).grid(row=10,column=16)
        Button(root,text="Edit Bus",font="Arial 12 bold",fg="black",bg="light green",command=Bus_Edit).grid(row=10,column=17)
        def fun9():
            root.destroy()
            self.home()
        Button(root,image=img_home,command=fun9).grid(row=10,column=18)
        root.mainloop()
    #PAGE6
    def new_operator(self):
        root=Tk()
        #Create the database in python
        import sqlite3
        con=sqlite3.Connection('Bus_Booking.db')
        cur=con.cursor()
        cur.execute('create table if not exists operator(Operator_ID number PRIMARY KEY,Name char(30),Address varchar(40),Phone number,Email varchar(40))')
        cur.execute('create table if not exists Bus(Bus_ID number PRIMARY KEY,Bustype varchar(30),Capacity number,Fare number,operator_i number,route_i number,foreign key(operator_i) references operator(Operator_ID),foreign key(route_i) references Route(Routeid))')
        cur.execute('create table if not exists Runs(Busi number,Date varchar(25),Seat_available number,PRIMARY KEY(Busi,Date),foreign key(Busi) references Bus(Bus_ID))')
        cur.execute('create table if not exists Route(Routeid number,Stationid number,Station_name char(60),PRIMARY KEY(Routeid,Stationid))')
        cur.execute('create table if not exists Booking_history(passenger_name varchar(20), Gender varchar(12),No_of_seats number, mobile number PRIMARY KEY,age number,bus_select number,t_o varchar(13),fr varchar(13),date varchar(25),fare number)')

        root.title("Add_Bus_Operator_Details_Page")
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
        img=PhotoImage(file='.\\Bus_for_project.png')
        img_home=PhotoImage(file='.\\home.png')
        Label(root,image=img).grid(row=0,column=6,columnspan=20)
        Label(root,text="Online Bus Booking System",font="Arial 22 bold",bg="light blue",fg="red").grid(row=1,column=6,columnspan=20)
        Label(root,text="").grid(row=2,column=0)
        Label(root,text="").grid(row=3,column=0)
        Label(root,text="Add Bus Operator Details",font="Arial 18 bold",fg='green').grid(row=4,column=6,columnspan=20)
        Label(root,text="").grid(row=5,column=0)
        Label(root,text="").grid(row=6,column=0)
        Label(root,text="").grid(row=7,column=0)
        Label(root,text="                       ").grid(row=8,column=0)
        Label(root,text="Operator ID",font="Arial 10 bold").grid(row=8,column=3)
        Operator_ID=Entry(root,font="Arial 10 bold")
        Operator_ID.grid(row=8,column=4)
        Label(root,text="Name",font="Arial 10 bold").grid(row=8,column=5)
        Name=Entry(root,font="Arial 10 bold")
        Name.grid(row=8,column=6)
        Label(root,text="Address",font="Arial 10 bold").grid(row=8,column=7)
        Address=Entry(root,font="Arial 10 bold")
        Address.grid(row=8,column=8)
        Label(root,text="Phone",font="Arial 10 bold").grid(row=8,column=9)
        Phone=Entry(root,font="Arial 10 bold")
        Phone.grid(row=8,column=10)
        Label(root,text="Email",font="Arial 10 bold").grid(row=8,column=11)
        Email=Entry(root,font="Arial 10 bold")
        Email.grid(row=8,column=12)
        def Add():
            if(len(Operator_ID.get())!=0 or len(Name.get())!=0 or len(Address.get())!=0 or len(Phone.get())!=0 or len(Email.get())!=0):
                y=(Operator_ID.get(),Name.get(),Phone.get(),Address.get(),Email.get())
                query=('insert into operator(Operator_ID ,Name ,Phone ,Address,Email) values(?,?,?,?,?)')
                cur.execute(query,y)
                con.commit()
                showinfo('Add Bus Entry','Bus Record Added')
                y1=(Operator_ID.get())
                query1=('select * from operator where Operator_ID=?')
                cur.execute(query1,y1)
                con.commit()
                result=cur.fetchall()
                Label(root,text=result,font="Arial 10 bold").grid(row=10,column=6,columnspan=30)
                print(result)
                Operator_ID.delete(0,END)
                Name.delete(0,END)
                Address.delete(0,END)
                Phone.delete(0,END)
                Email.delete(0,END)
            else:
                showerror('Value Missing','Please Enter The Correct Values')
        def Edit():
            if len(Operator_ID.get())!=0 or len(Name.get())!=0 or len(Address.get())!=0 or len(Phone.get())!=0 or len(Email.get())!=0:
                y=(Operator_ID.get())
                query='select * from operator where Operator_ID=?'
                cur.execute(query,y)
                res=cur.fetchall()
                if(res):
                    showinfo('Found','record found')
                    y1=(Operator_ID.get(),Name.get(),Phone.get(),Address.get(),Email.get(),Operator_ID.get()) 
                    cur.execute('UPDATE operator SET Operator_ID=? ,Name=? ,Phone=? ,Address=? , Email=? WHERE Operator_ID=?',y1)
                    con.commit()
                    showinfo('Bus Entry Edit','Bus Record Edited Successfully')
                    y2=(Operator_ID.get())
                    query1=('select * from operator where Operator_ID=?')
                    cur.execute(query1,y2)
                    con.commit()
                    result=cur.fetchall()
                    Label(root,text=result,font="Arial 10 bold").grid(row=10,column=6,columnspan=30)
                    print(result)
                    Operator_ID.delete(0,END)
                    Name.delete(0,END)
                    Address.delete(0,END)
                    Phone.delete(0,END)
                    Email.delete(0,END)
                else:
                    showinfo('Bus Entry ERORR!!','Bus Record Not Found')
            else:
                showerror('Value Missing','Please Enter The Correct Values')  
                  
        Button(root,text="Add",fg="black",bg="light green",font="Arial 10 bold",command=Add).grid(row=8,column=13)
        Label(root,text="").grid(row=8,column=14)
        Button(root,text="Edit",fg="black",bg="light green",font="Arial 10 bold",command=Edit).grid(row=8,column=15)
        Label(root,text="").grid(row=9,column=0)
        Label(root,text="").grid(row=10,column=0)
        Label(root,text="").grid(row=11,column=0)
        def fun10():
            root.destroy()
            self.home()

        Button(root,image=img_home,font="Arial 10",command=fun10).grid(row=12,column=15)


        root.mainloop()


    #PAGE5    
    def seat_booked(self):
        root=Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
        # Creating Database
        import sqlite3
        con=sqlite3.Connection('Bus_Booking.db')
        cur=con.cursor()

        cur.execute('create table if not exists operator(operator_id number PRIMARY KEY,Name varchar(30),address varchar(40),phone number,email varchar(40))')
        cur.execute('create table if not exists bus(Bus_id number PRIMARY KEY,type varchar(30),capacity number,fare number, operator_id number,route_id number,foreign key(operator_id) references operator(operator_id),foreign key(Bus_id) references runs(Bus_id),foreign key(route_id) references route(route_id))')
        cur.execute('create table if not exists route(route_id number ,station_name varchar(20),station_id  number,PRIMARY KEY(route_id,station_id))')
        cur.execute('create table if not exists runs(Bus_id number,date varchar(25),seat_avaiable number,PRIMARY KEY(Bus_id,date))')
        cur.execute('create table if not exists Booking_history(passenger_name varchar(20), Gender varchar(12),No_of_seats number, mobile varchar(10) PRIMARY KEY,age number,bus_select number,t_o varchar(13),fr varchar(13),date varchar(25),fare number)')


        root.title("Check Your Booking")

        img_Bus=PhotoImage(file=".\\Bus_for_project.png")
        img_home=PhotoImage(file=".\\home.png")

        Label(root,image=img_Bus).grid(row=0,column=0,padx=w//3+155,columnspan=82)

        Label(root,text="Online Bus Booking System",font="Arial 35 bold",bg="light blue",fg="red").grid(row=1,column=0,columnspan=82,pady=30)

        Label(root,text="Enter Your Mobile No.:",font="Arial 15 bold",fg="black").grid(row=3,column=40)
        mobile=Entry(root,font='Arial 10 bold')
        mobile.grid(row=3,column=41)

        def check_booking():
            if(mobile.get().isnumeric() and len(mobile.get())==10):
                frame=Frame(root,relief="groove",bd=5)
                frame.grid(row=6,column=2,columnspan=100)

                Label(root,text="Bus Ticket",font='Arial 12 bold').grid(row=5,column=41,)
                value=mobile.get()
                cur.execute('select  * from booking_history where mobile=(?)',[value])

                res=cur.fetchall()
                if(res):
                    
                    Label(frame,text="Passenger:",font='Arial 10 bold').grid(row=3,column=0,)
                    Label(frame,text=res[0][0],font='Arial 10 bold').grid(row=3,column=1,)
                
                    Label(frame,text="Gender:",font='Arial 10 bold').grid(row=3,column=3,)
                    Label(frame,text=res[0][1],font='Arial 10 bold').grid(row=3,column=4,)
                
                    Label(frame,text="No. Of Seat:",font='Arial 10 bold').grid(row=4,column=0,)
                    Label(frame,text=res[0][2],font='Arial 10 bold').grid(row=4,column=1,)
                
                    Label(frame,text="Phone:",font='Arial 10 bold').grid(row=4,column=3,)
                    Label(frame,text=res[0][3],font='Arial 10 bold').grid(row=4,column=4,)
                
                    Label(frame,text="Age.:",font='Arial 10 bold').grid(row=5,column=0)
                    Label(frame,text=res[0][4],font='Arial 10 bold').grid(row=5,column=1,)
                
                    Label(frame,text="Bus No.:",font='Arial 10 bold').grid(row=5,column=3,)
                    Label(frame,text=res[0][5],font='Arial 10 bold').grid(row=5,column=4,)
                
                    Label(frame,text="From:",font='Arial 10 bold').grid(row=6,column=0)
                    Label(frame,text=res[0][6],font='Arial 10 bold').grid(row=6,column=1,)
                
                    Label(frame,text="To:",font='Arial 10 bold').grid(row=6,column=3)
                    Label(frame,text=res[0][7],font='Arial 10 bold').grid(row=6,column=4)
                
                    Label(frame,text="Travel on:",font='Arial 10 bold').grid(row=7,column=0)
                    Label(frame,text=res[0][8],font='Arial 10 bold').grid(row=7,column=1)
                
                    Label(frame,text="Fare:",font='Arial 10 bold').grid(row=7,column=3)
                    Label(frame,text=res[0][2]*res[0][9],font='Arial 10 bold').grid(row=7,column=4)
                    value=str(res[0][2]*res[0][9])

                    Label(root,text="Your fare price is  Rs."+value,font='Arial 15 bold',fg='blue').grid(row=9,column=0,columnspan=82)
                else:
                    showerror('Error','No booking with this Mobile no.')
                    if(askyesno('Booking','Do you want to do booking?')):
                        root.destroy()
                        self.bus_booking()
                        
            
                
                
            else:
                showerror("Booking","Enter the correct mobile no.!")
                
        Button(root,text="Check Booking",font="Arial 12 bold",fg="black",command=check_booking).grid(row=3,column=42)
        def fun11():
            root.destroy()
            self.home()

        Button(root,image=img_home,bg='green',command=fun11).grid(row=3,column=43)

        root.mainloop()

    #PAGE4
    def add_bus(self):
        root=Tk()
        root.title("Add_Bus_Details_to_Database_Page")
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
        fr=Frame(root)
        fr.grid(row=0,column=0,columnspan=10)
        img_Bus=PhotoImage(file=".\\Bus_for_project.png")
        Label(fr,image=img_Bus).grid(row=0,column=0,padx=w//4+200)
        fr.grid(row=1,column=0,columnspan=10)
        Label(fr,text="Online Bus Booking System",font="Arial 20 bold",bg="light blue",fg="red").grid(row=1,column=0,columnspan=20,pady=20)
        Label(root,text="Add New Details to DataBase",font="Arial 18 bold",fg='green').grid(row=2,column=0,pady=20,columnspan=20)
        Label(root,text="").grid(row=3,column=0,padx=150,pady=25)

        def fun4():
            root.destroy()
            self.new_operator()
        Button(root,text="New Operator",font="Arial 12 bold",bg="light green",fg="black",command=fun4).grid(row=3,column=1)
        def fun5():
            root.destroy()
            self.bus_new()

        Button(root,text="New Bus",font="Arial 12 bold",bg="orange red",fg="black",command=fun5).grid(row=3,column=2)
        def fun6():
            root.destroy()
            self.bus_route()

        Button(root,text="New Route",font="Arial 12 bold",bg="cornflower blue",fg="black",command=fun6).grid(row=3,column=3)
        def fun7():
            root.destroy()
            self.bus_run()

        Button(root,text="New Run",font="Arial 12 bold",fg='black',bg='sienna1',command=fun7).grid(row=3,column=4)

        root.mainloop()

    





    #PAGE3
    def bus_booking(self):
        #Creating Database
        root=Tk()
        import sqlite3
        con=sqlite3.Connection('Bus_Booking.db')
        cur=con.cursor()
        cur.execute('create table if not exists operator(Operator_ID number PRIMARY KEY,Name char(30),Address varchar(40),Phone number,Email varchar(40))')
        cur.execute('create table if not exists Bus(Bus_ID number PRIMARY KEY,Bustype varchar(30),Capacity number,Fare number,operator_i number,route_i number,foreign key(operator_i) references operator(Operator_ID),foreign key(route_i) references Route(Routeid))')
        cur.execute('create table if not exists Runs(Busi number,Date varchar(25),Seat_available number,PRIMARY KEY(Busi,Date),foreign key(Busi) references Bus(Bus_ID))')
        cur.execute('create table if not exists Route(Routeid number,Stationid number,Station_name char(60),PRIMARY KEY(Routeid,Stationid))')
        cur.execute('create table if not exists Booking_history(passenger_name varchar(20), Gender varchar(12),No_of_seats number, mobile number PRIMARY KEY,age number,bus_select number,t_o varchar(13),fr varchar(13),date varchar(25),fare number)')


        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))

        root.title("Enter Journey Details")
    #    root.title("Enter Journey Details")
        bus_select=IntVar()
        Bus1=0
        Bus2=0

        img_Bus=PhotoImage(file=".\\Bus_for_project.png")
        img_home=PhotoImage(file=".\\home.png")
        Label(root,image=img_Bus).grid(row=0,column=0,padx=w//3+155,columnspan=81)                               

        Label(root,text="Online Bus Booking System",font="Arial 20 bold",bg="light blue",fg="red").grid(row=1,column=0,columnspan=81)
        Label(root,text="Enter Journey Details",font="Arial 16 bold",bg="light green",fg="dark green").grid(row=2,column=0,columnspan=81,pady=30)

        Label(root,text="To",font="Arial 15 bold").grid(row=3,column=33)
        To=Entry(root,font="Arial 10 bold")
        To.grid(row=3,column=34)

        Label(root,text="From",font="Arial 15 bold").grid(row=3,column=35)
        From=Entry(root,font="Arial 10 bold")
        From.grid(row=3,column=36)

        Label(root,text="Journey Date",font="Arial 15 bold").grid(row=3,column=37)
        JDate=Entry(root,font="Arial 10 bold")
        JDate.grid(row=3,column=38)
        dict={}

        def show_bus():
            
            if(To.get().isspace() or From.get().isspace() or JDate.get().isspace()):
                showerror("Error","Missing!")
            elif(len(To.get())==0 or len(From.get())==0 or len(JDate.get())==0):
                showerror("Missing","Enter all the fields")
         
            elif(To.get().isnumeric() or From.get().isnumeric()):
                showerror("Missing","Enter city names correctly!")
            
            else:
                to=To.get()
                fr=From.get()
                Jd=JDate.get()

                value=(to,fr,Jd)
                query='select Name,Bustype,Seat_available,Capacity,Fare,Runs.Busi from operator,Bus,Runs,Route as t,Route as f where operator.Operator_ID=bus.operator_i and Bus.Bus_ID=Runs.Busi and Bus.route_i=t.Routeid and t.Station_name=? and f.Station_name=? and date=?'
                cur.execute(query,value)
                res=cur.fetchall()
                print(res)
                i=1
                for a in res:
                    dict.update({i:a})
                    n=0
                    for b in a:
                        Bus1=Radiobutton(root,text="BUS"+str(i),variable=bus_select,value=i,font="Arial 10 bold")
                        Bus1.grid(row=6+i,column=33)
                        Label(root,text=b,font="Arial 10 bold").grid(row=6+i,column=34+n)
                        n=n+1
                    i=i+1
                #print(res)


                
                Label(root,text=" ").grid(row=4,column=0)
                Label(root,text="Select Bus",font="Arial 13 bold",fg="dark green").grid(row=5,column=33)
                Label(root,text="Operator",font="Arial 13 bold",fg="dark green").grid(row=5,column=34)
                Label(root,text="Bus Type",font="Arial 13 bold",fg="dark green").grid(row=5,column=35)
                Label(root,text="Available",font="Arial 13 bold",fg="dark green").grid(row=5,column=36)
                Label(root,text="Capacity",font="Arial 13 bold",fg="dark green").grid(row=5,column=37)
                Label(root,text="Fare",font="Arial 13 bold",fg="dark green").grid(row=5,column=38)
                Label(root,text="Bus ID",font="Arial 13 bold",fg="dark green").grid(row=5,column=39)
                Button(root,text="Proceed To Book",font="Arial 13 bold",bg="light green",fg="black",command=selecting_bus).grid(row=6,column=40)

                
                Bus1=Radiobutton(root,text="BUS1",variable=bus_select,value=1,font="Arial 10 bold")
                Bus1.grid(row=7,column=33)
                Bus2=Radiobutton(root,text="BUS2",variable=bus_select,value=2,font="Arial 10 bold")
                Bus2.grid(row=8,column=33)

                
        def selecting_bus():
            import sqlite3
            con=sqlite3.Connection('Bus_Booking.db')
            cur=con.cursor()
            cur.execute('create table if not exists operator(Operator_ID number PRIMARY KEY,Name char(30),Address varchar(40),Phone number,Email varchar(40))')
            cur.execute('create table if not exists Bus(Bus_ID number PRIMARY KEY,Bustype varchar(30),Capacity number,Fare number,operator_i number,route_i number,foreign key(operator_i) references operator(Operator_ID),foreign key(route_i) references Route(Routeid))')
            cur.execute('create table if not exists Runs(Busi number,Date varchar(25),Seat_available number,PRIMARY KEY(Busi,Date),foreign key(Busi) references Bus(Bus_ID))')
            cur.execute('create table if not exists Route(Routeid number,Stationid number,Station_name char(60),PRIMARY KEY(Routeid,Stationid))')
            cur.execute('create table if not exists Booking_history(passenger_name varchar(20), Gender varchar(12),No_of_seats number, mobile number PRIMARY KEY,age number,bus_select number,t_o varchar(13),fr varchar(13),date varchar(25),fare number)')
            if bus_select.get()==0:
                showerror('Select','Please Select Bus')
            else:
                #print(bus_select.get())
                k=bus_select.get()
                #print(dict[k])
                pass_details=dict[k]
                #print(ans[0],ans[3])
                Label(root,text="Fill Passenger Details To Book The Bus Ticket",font="Arial 20 bold",bg="light blue",fg="red").grid(row=13,column=0,columnspan=81,pady=30)

                Label(root,text="Name",font="Arial 15 bold").grid(row=14,column=33)
                name=Entry(root,font="Arial 10 bold")
                name.grid(row=14,column=34)

                Label(root,text="Gender",font="Arial 15 bold").grid(row=14,column=35)
                gender=StringVar()
                gender.set("Gender")
                opt=("Male","Female","Third")
                d_menu=OptionMenu(root,gender,*opt).grid(row=14,column=36)

                Label(root,text="No. Of Seats",font="Arial 15 bold").grid(row=14,column=37)
                seat=Entry(root,font="Arial 10 bold")
                seat.grid(row=14,column=38)

                Label(root,text="Mobile No.",font="Arial 15 bold").grid(row=14,column=39)
                mobile=Entry(root,font="Arial 10 bold")
                mobile.grid(row=14,column=40)

                Label(root,text="Age",font="Arial 15 bold").grid(row=14,column=41) 
                age=Entry(root,font="Arial 10 bold")
                age.grid(row=14,column=42)
                def book_seat():
                    if(len(name.get())==0 or len(seat.get())==0 or len(age.get())==0 or len(mobile.get())==0):
                        showerror("Missing","Enter all the fields")
                    elif(name.get().isnumeric()):
                        showerror("Missing","Enter Name correctly!")
                    elif(seat.get().isalpha()):
                        showerror("Error","Enter the seat in numeric")
                    elif(len(mobile.get())!=10) or mobile.get().isalpha():
                        showerror("Error","Enter 10 digit Mobile no.")
                    elif(age.get().isalpha() or int(age.get())<=0 or int(age.get())>120 ):
                        showerror("Missing","Enter age correctly!")
                    else:
                        if(askyesnocancel('Confirm','Do you want to proceed ?')):
                            m=int(pass_details[2])
                            n=int(seat.get())
                           # if(n>m):
                            #    showerror("Error","Seat cant be booked")
                        if(m-n==0):
                            showerror("Error","seats cant be booked")
                        elif(m-n<0):
                            showerror("Error","seats cant be booked")
                        elif(m-n>0):
                                    query1='update Runs set Seat_available =(?) where Busi=? and date=?'
                                    value1=((m-n),pass_details[5],JDate.get())
                                    cur.execute(query1,value1)
                                    con.commit()
                                    value=(name.get(),gender.get(),seat.get(),mobile.get(),age.get(),pass_details[0],To.get(),From.get(),JDate.get(),pass_details[4])
                                    query='insert into Booking_history(passenger_name,Gender,No_of_seats,mobile,age,bus_select,t_o,fr,date,fare)values(?,?,?,?,?,?,?,?,?,?)'
                                    cur.execute(query,value)
                                    con.commit() 
                                    showinfo("Success","Booked Successfully")
                                    s=int(seat.get())
                                    f=int(pass_details[4])
                                    v=s*f
                                    showinfo('Fare','Fare is Rs.'+str(v))
                                    if(askyesnocancel('Bus Ticket','Do you want to check your Ticket')):
                                    
                                        root.destroy()
                                        self.seat_booked()
                        
                        else:
                            showerror("Error","seats not available")    
                
                    

                Button(root,text="Book Seat",font="Arial 13 bold",bg="light green",fg="black",command=book_seat).grid(row=14,column=43)
            


            
        Button(root,text="Show Bus",font="Arial 15 bold",bg="light green",fg="black",command=show_bus).grid(row=3,column=39)
        def fun12():
            root.destroy()
            self.home()
        Button(root,image=img_home,command=fun12).grid(row=3,column=40)
                                                                                        

        root.mainloop()





    #PAGE2
    def home(self):
        root=Tk()
        root.title('Bus Booking Home Page')
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
        img=PhotoImage(file='.\\Bus_for_project.png')
        Label(root,image=img).grid(row=0,column=7)
        Label(root,text='Online Bus Booking System',font='Arial 24 bold',bg='Light Skyblue1',fg='red').grid(row=1,column=7)
        Label(root,text="").grid(row=2,column=0)
        Label(root,text="").grid(row=3,column=0)
        Label(root,text="").grid(row=4,column=0)
        Label(root,text="                                                                                                         ").grid(row=4,column=0)
        def fun1():
            root.destroy()
            self.bus_booking()
        def fun2():
            root.destroy()
            self.seat_booked()
        def fun3():
            root.destroy()
            self.add_bus()
        Button(root,text='Seat Booking',font='Arial 16 bold',bg='Light green',fg='black',command=fun1).grid(row=4,column=2,pady=25)     
        Button(root,text='Check Booked Seat',font='Arial 16 bold',bg='lime green',fg='black',command=fun2).grid(row=4,column=7,pady=25)
        Button(root,text='Add Bus Details',font='Arial 16 bold',bg='forest green',fg='black',command=fun3).grid(row=4,column=8,pady=25)
        Label(root,text="For Admin Only",font='Arial 14 bold',fg="red").grid(row=6,column=8)
        root.mainloop()


    #PAGE1
    def cover(self):
        root=Tk()
        root.title('Python Project')
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        #root.geometry('%dx%d+0+0'%(w,h))
        root.state('zoomed')
        img=PhotoImage(file='.\\Bus_for_project.png')
        Label(root,image=img).pack()
        Label(root,text='Online Bus Booking System',font='Arial 22 bold',bg='Light Skyblue1',fg='red').pack()
        Label(root,text="").pack()
        Label(root,text='Name:Saket Bagdi',font='Arial 16 bold',fg='blue').pack()
        Label(root,text=" ").pack()
        Label(root,text='Er. 211B265',font='Arial 16 bold',fg='blue').pack()
        Label(root,text=" ").pack()
        Label(root,text='Mobile:6232731297',font='Arial 16 bold',fg='blue').pack()
        Label(root,text=" ").pack()
        Label(root,text=" ").pack()
        Label(root,text='Submitted To:Dr.Mahesh Kumar',font='Arial 18 bold',bg='Light Skyblue1',fg='red').pack()
        Label(root,text='Project Based Learning',font='Arial 16 bold',fg='red').pack()

        def gohome(e=0):
            root.destroy()
            self.home()
        #root.after(3000,closehome)    
        root.bind('<KeyPress>',gohome)    
        root.mainloop()

t=Test()
t.cover()

