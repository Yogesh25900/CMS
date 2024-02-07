from tkinter import *
import mysql.connector
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry

class staffDatabase:
    def __init__(self,master,**kwargs):
        self.master = master
        self.master.title('Admin adding staff')
        self.master.geometry('1300x700+0+2')
        
        self.host ="localhost"
        self.port ='3306'
        self.database='canteen_database1'
        self.user='root'
        self.password=''
        


        #assigning variable for staff table
        self.staffid = StringVar()
        self.cus_name =StringVar()
        self.mail =StringVar()
        self.phone =StringVar()
        self.address =StringVar()
        self.username =StringVar()
        self.key =StringVar()
        self.labeltitle = Label(self.master,text="Staff ",font=('helvetica','15'))
        self.labeltitle.pack()
         #new frame for registering staffs
        self.register_frame = Frame(self.master,bd=7,relief=GROOVE,width=400,height=450)
        self.register_frame.pack(expand=TRUE)
       
        #frame for buttons
        

        label_id = Label(self.register_frame, text="Enter Staff Id")
        label_id.place(x=2,y=235)
        self.searchid= StringVar()
        entry_search = Entry(self.register_frame, width=20,textvariable=self.searchid)
        entry_search.place(x=100,y=235)


        register_button = Button(self.register_frame, text="Add",command=self.add_staff)  # Add a command to register new students
        register_button.place(x=60,y=267)



        

        self.c_id=Label(self.register_frame, text="Staff ID")
        self.c_id.place(x=2,y=3)
        self.e1 =Entry(self.register_frame, width=30,textvariable=self.staffid)
        self.e1.place(x=90,y=3)

        self.label_cname= Label(self.register_frame, text="Name")
        self.label_cname.place(x=2,y=35)
        self.e2= Entry(self.register_frame, width=30,textvariable=self.cus_name)
        self.e2.place(x=90,y=35)

        self.label_contact =Label(self.register_frame, text="Contact")
        self.label_contact.place(x=2,y=67)
        self.e3=Entry(self.register_frame, width=30,textvariable=self.phone)
        self.e3.place(x=90,y=67)

       
        self.maill = Label(self.register_frame, text="Email")
        self.maill.place(x=2,y=99)
        self.e4=Entry(self.register_frame, width=30,textvariable=self.mail)
        self.e4.place(x=90,y=99)

        self.label_address= Label(self.register_frame, text="Address")
        self.label_address.place(x=2,y=131)
        self.e5 =Entry(self.register_frame, width=30,textvariable=self.address)
        self.e5.place(x=90,y=131)

        

        self.uname = Label(self.register_frame, text="username")
        self.uname.place(x=2,y=163)
        self.e6 =Entry(self.register_frame, width=30,textvariable=self.username)
        self.e6.place(x=90,y=163)

        self.pwd = Label(self.register_frame, text="Password")
        self.pwd.place(x=2,y=195)
        self.e7 =Entry(self.register_frame, width=30,textvariable=self.key)
        self.e7.place(x=90,y=195)


    
    #add new staff to DB
    def add_staff(self):
        
        c_id =self.staffid.get()
        name= self.cus_name.get()
        phone=self.phone.get()
        mail= self.mail.get()
        address= self.address.get()
        uname =self.username.get()
        pwd= self.key.get()
        try:
            connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database,
            )
            cursor = connection.cursor()
            

            query ="INSERT INTO tbstaff(staffid,name,phone,email,address,username,password) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            values =(c_id,name,phone,mail,address,uname,pwd)
            cursor.execute(query,values)
            connection.commit()
            messagebox.showinfo("Success","staff registered Successfully")
        except Exception as e:
            print(f"Error: {e}")
            messagebox.showerror("Error", f"Error: {e}")
            return False
  

def main():
    master =Tk()
    instance = staffDatabase(master)
    master.mainloop()
if __name__ == '__main__':
    main()