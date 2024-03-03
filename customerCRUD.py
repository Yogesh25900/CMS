from tkinter import *
import mysql.connector
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk
class cruduser:
    def __init__(self,master,**kwargs):
        self.master = master
        self.master.title('Manage Customer Details')
        self.master.geometry('900x700+0+2')
        self.master.resizable(False, False)
        file ="register.jpg"
        org =Image.open(file)
        resize = org.resize((900,700))
        self.bg_image=ImageTk.PhotoImage(resize)

        label_img = Label(self.master,image=self.bg_image)
        label_img.pack()
        
        self.host ="localhost"
        self.port ='3306'
        self.database='canteen_database1'
        self.user='root'
        self.password=''
        


        #assigning variable for customer table
        self.customerid = StringVar()
        self.cus_name =StringVar()
        self.mail =StringVar()
        self.phone =StringVar()
        self.address =StringVar()
        self.username =StringVar()
        self.key =StringVar()

      
       

    

         #new frame for registering customers
        self.register_frame = LabelFrame(self.master,text="Manage Customer",font=(16),bd=7,relief=GROOVE,width=400,height=450)
        self.register_frame.place(x=100,y=100)
       
        #frame for buttons
        

      

        

       

        

      

        self.label_cname= Label(self.register_frame, text="Name",font=(16))
        self.label_cname.place(x=2,y=40)
        self.e2= Entry(self.register_frame, width=20,textvariable=self.cus_name,font=(16))
        self.e2.place(x=110,y=40)

        self.label_contact =Label(self.register_frame, text="Contact",font=(16))
        self.label_contact.place(x=2,y=75)
        self.e3=Entry(self.register_frame, width=20,textvariable=self.phone,font=(16))
        self.e3.place(x=110,y=75)

       
        self.maill = Label(self.register_frame, text="Email",font=(16))
        self.maill.place(x=2,y=110)
        self.e4=Entry(self.register_frame, width=20,textvariable=self.mail,font=(16))
        self.e4.place(x=110,y=110)

        self.label_address= Label(self.register_frame, text="Address",font=(16))
        self.label_address.place(x=2,y=145)
        self.e5 =Entry(self.register_frame, width=20,textvariable=self.address,font=(16))
        self.e5.place(x=110,y=145)

        

        self.uname = Label(self.register_frame, text="Username",font=(16))
        self.uname.place(x=2,y=180)
        self.e6 =Entry(self.register_frame, width=20,textvariable=self.username,font=(16))
        self.e6.place(x=110,y=180)

        self.pwd = Label(self.register_frame, text="Password",font=(16))
        self.pwd.place(x=2,y=220)
        self.e7 =Entry(self.register_frame, width=20,textvariable=self.key,show ='*',font=(16))
        self.e7.place(x=110,y=220)

        label_id = Label(self.register_frame, text="Enter customer Name",font=(16))
        label_id.place(x=2,y=270)
        self.searchid= StringVar()

        entry_search = Entry(self.register_frame, width=20,textvariable=self.searchid)
        entry_search.place(x=200,y=270)

        search_button = Button(self.register_frame, text="Search",font=(16),command=self.search_customer)
        search_button.place(x=80,y=305)


        register_button = Button(self.register_frame, text="Add",font=(16),command=self.add_customer)  # Add a command to register new customers
        register_button.place(x=150,y=305)

        update_button = Button(self.register_frame, text="Update",font=(16),command=self.update_customer)
        update_button.place(x=200,y=305)

        delete_button = Button(self.register_frame, text="Delete", font=(16),command=self.delete_customer)  # Add a command to delete customers
        delete_button.place(x=280,y=305)


    
    #add new customer to DB
    def add_customer(self):
        
        c_id =self.customerid.get()
        name= self.cus_name.get()
        phone=self.phone.get()
        mail= self.mail.get()
        address= self.address.get()
        uname =self.username.get()
        pwd= self.key.get()
        if  not name or not phone or not mail or not address or not uname or not pwd:
            messagebox.showerror("Invlaid","Please enter the data in all fields below")
        else:
            if len(phone) != 10:
                messagebox.showerror("Invalid","Please enter valid phone number")
            else:
                try:
                    connection = mysql.connector.connect(
                        host=self.host,
                        port=self.port,
                        user=self.user,
                        password=self.password,
                        database=self.database,
                    )
                    cursor = connection.cursor()
                    

                    query ="INSERT INTO tbcustomer(name,phone,email,address,username,password) VALUES (%s,%s,%s,%s,%s,%s)"
                    values =(name,phone,mail,address,uname,pwd,)
                    cursor.execute(query,values)
                    connection.commit()
                    messagebox.showinfo("Success","Customer registered Successfully")
                except Exception as e:
                    print(f"Error: {e}")
                    messagebox.showerror("Error", f"Error: {e}")
                    return False
                finally:
                    
                    cursor.close()
                    connection.close()

            
            
       


    def update_customer(self):
        c_id =self.searchid.get()
        name =self.e2.get()
        phone = self.e3.get()
        email = self.e4.get()
        address = self.e5.get()
        username = self.e6.get()
        password= self.e7.get()
                
        try:
            connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database,
            )
            cursor = connection.cursor()
            cursor.execute("SELECT customerid from tbcustomer WHERE LOWER(name) = LOWER(%s)",(c_id,))
            id = cursor.fetchone()[0]
            
            query ="UPDATE tbcustomer SET name=%s,phone = %s ,email = %s , address = %s ,username = %s ,password = %s where customerid=%s "
            values =(name,phone,email,address,username,password,id)

            cursor.execute(query, values)
            connection.commit()
            messagebox.showinfo("Success", "customer details updated successfully!")

        except Exception as e:
            print(f"Error: {e}")
            messagebox.showerror("Error", f"Error: {e}")
            return False
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    #deleting the customer
    def delete_customer(self):
        c_id =self.searchid.get()

        try:
            connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database,
            )
            cursor = connection.cursor()
            
            

            query = "DELETE FROM tbcustomer WHERE LOWER(name)=%s"
            values = (c_id,)

            cursor.execute(query, values)
            connection.commit()
            messagebox.showinfo("Success", "customer deleted successfully!")
            self.e2.delete(0, END)
            self.e3.delete(0, END)
            self.e4.delete(0, END)
            self.e5.delete(0, END)
            self.e6.delete(0, END)
            self.e7.delete(0, END)




           


        except Exception as e:
            print(f"Error: {e}")
            messagebox.showerror("Error", f"Error: {e}")
            return False
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    def search_customer(self):
        c_id =self.searchid.get()


        try:
            connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database,
            )
            cursor=connection.cursor()

            if not c_id:
                messagebox.showerror("Empty field","Please enter the data in search field.")
            else:
                query = "SELECT * FROM tbcustomer WHERE customerid=%s or LOWER(name)= LOWER(%s)"
                values = (c_id,c_id)
                cursor.execute(query, values)
                self.rows = cursor.fetchall()


                if self.rows:
                    messagebox.showinfo("Success", "Found")

                    customer_data = self.rows[0]  # Assuming you are fetching a single customer

                    # Update Entry widgets with the data from the database
                    
                    self.e2.delete(0, END)  # Clear the existing value
                    self.e2.insert(0, customer_data[1])  # Assuming the third column is rate
                    
                    self.e3.delete(0, END)  # Clear the existing value
                    self.e3.insert(0, customer_data[2])  # Assuming the third column is rate

                    self.e4.delete(0, END)  # Clear the existing value
                    self.e4.insert(0, customer_data[3])  # Assuming the third column is rate

                    self.e5.delete(0, END)  # Clear the existing value
                    self.e5.insert(0, customer_data[4])  # Assuming the third column is rate

                    self.e6.delete(0, END)  # Clear the existing value
                    self.e6.insert(0, customer_data[5])  # Assuming the third column is rate

                    self.e7.delete(0, END)  # Clear the existing value
                    self.e7.insert(0, customer_data[6])  # Assuming the third column is rate






                

                else: 
                    messagebox.showinfo("OOps", "Not Found")
    


                
            connection.commit()

        except Exception as e:
            print(f"Error: {e}")
            messagebox.showerror("Error", f"Error: {e}")
            return False
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

def main():
    master =Tk()
    instance = cruduser(master)
    master.mainloop()
if __name__ == '__main__':
    main()
        