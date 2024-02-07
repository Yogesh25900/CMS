from tkinter import *
import mysql.connector
from tkinter import messagebox
from tkinter import ttk

class staffMenu:
    def __init__(self,master,**kwargs):
        self.master = master
        self.master.title('Staff Menu')
        self.master.geometry('1300x700+0+2')
        
        self.host ="localhost"
        self.port ='3306'
        self.database='canteen_database1'
        self.user='root'
        self.password=''
        


        #assigning variable for food table
        self.foodid = StringVar()
        self.food_name =StringVar()
        self.mail =StringVar()
        self.rate =StringVar()
        self.address =StringVar()
        self.username =StringVar()
        self.key =StringVar()

        self.labeltitle = Label(self.master,text="food ",font=('helvetica','15'))
        self.labeltitle.pack()

         #new frame for registering foods
        self.register_frame = Frame(self.master,bd=7,relief=GROOVE,width=400,height=450)
        self.register_frame.pack(expand=TRUE)
       
        #frame for buttons
        



   
        register_button = Button(self.register_frame, text="Add",command=self.add_food)  # Add a command to register new foods
        register_button.place(x=150,y=267)

      

        

        

        self.c_id=Label(self.register_frame, text="Food ID")
        self.c_id.place(x=2,y=3)
        self.e1 =Entry(self.register_frame, width=30,textvariable=self.foodid)
        self.e1.place(x=90,y=3)

        self.label_cname= Label(self.register_frame, text="Food Name")
        self.label_cname.place(x=2,y=35)
        self.e2= Entry(self.register_frame, width=30,textvariable=self.food_name)
        self.e2.place(x=90,y=35)

        self.label_rate=Label(self.register_frame, text="Rate")
        self.label_rate.place(x=2,y=67)
        self.e3=Entry(self.register_frame, width=30,textvariable=self.rate)
        self.e3.place(x=90,y=67)

       
        

    
    #add new food to DB
    def add_food(self):
        c_id =self.foodid.get()
        name= self.food_name.get()
        rate=self.rate.get()
        
        try:
            connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database,
            )
            cursor = connection.cursor()
            

            query ="INSERT INTO tbfooditems(itemid,name,rate) VALUES (%s,%s,%s)"
            values =(c_id,name,rate)
            cursor.execute(query,values)
            connection.commit()
            messagebox.showinfo("Success","food registered Successfully")
        except Exception as e:
            print(f"Error: {e}")
            messagebox.showerror("Error", f"Error: {e}")
            return False


def main():
    master =Tk()
    instance = staffMenu(master)
    master.mainloop()
if __name__ == '__main__':
    main()