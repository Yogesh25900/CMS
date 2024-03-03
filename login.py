from tkinter import *
from tkinter import messagebox
import mysql.connector
from tkinter import ttk,Toplevel
from PIL import Image,ImageTk
class login:
    def __init__(self,master):
        self.master = master
        self.master.title("Login Form")
        self.master.resizable(False, False)


        # org =Image.open("customerapp.jpg")
        # resize = org.resize((900,600))
        self.bg_image=ImageTk.PhotoImage(Image.open("login.png"))

        label_img = Label(self.master,image=self.bg_image)
        label_img.pack()

        #Assigning username and password 
        self.username = StringVar()
        self.password = StringVar()
        self.selected = StringVar()

        self.label_qa = Label(self.master,text='Welcome',font=('Calibri',30),bg="black",fg='white')
        self.label_qa.place(x=230,y=10)
        self.label_qa = Label(self.master,text='Login as :',font=(16))
        self.label_qa.place(x=160,y=70)
        def on_combobox_selected(event):
            self.selected =self.box.get()
            
        self.box = ttk.Combobox(self.master,values=['Administrator', 'Staff','Customer','Chef'],state='readonly',width=15,font=(16))
        self.box.set("Select Usertype")
        self.box.place(x=260,y=70)

        self.box.bind("<<ComboboxSelected>>", on_combobox_selected)

        #username label and entry
        self.label_u_name = Label(self.master,text='Username:',font=(16))
        self.label_u_name.place(x=160,y=120)
        self.entry_u_name = Entry(self.master,textvariable=self.username,font=(16),width=15)
        self.entry_u_name.place(x=260,y=120)
        
        #pasword label and entry
        self.label_password = Label(self.master,text='Password:',font=(16))
        self.label_password.place(x=160,y=160)
        self.entry_password = Entry(self.master,textvariable=self.password,show="*",font=(16),width=15)
        self.entry_password.place(x=260,y=160)

        # Login button
        self.btn_login = Button(self.master, text="Login",command=self.check_auth,font=(16))
        self.btn_login.place(x=280,y=200)

        self.btn_login = Button(self.master, text="Register as Customer",command=self.open_register_window,font=(16))
        self.btn_login.place(x=220,y=240)


    

    def check_auth(self):
        username=self.username.get()
        password = self.password.get()
        if username and password:
            try:
                connection =mysql.connector.connect(
                    host="localhost",
                    port='3306',
                    user ='root',
                    password='',
                    database= 'canteen_database1'
                )
                cursor=connection.cursor()
                if self.selected == "Administrator":
                    query = "SELECT * FROM tbadmin WHERE username= %s AND password = %s"
                    data=(username,password)
                    cursor.execute(query,data)
                    result=cursor.fetchone()
                    messagebox.showinfo("Success", "Login success !!!") and self.open_admin() if result else messagebox.showerror("Error", "Error:No such user found as Administrator")

                elif self.selected == 'Staff':
                    query = "SELECT * FROM tbstaff WHERE username= %s AND Password = %s"
                    data=(username,password)
                    cursor.execute(query,data)
                    result=cursor.fetchone()
                    messagebox.showinfo("success", "success") and self.open_staff() if result else messagebox.showerror("error", "Error:No such user found as Staff")
                
                
                elif self.selected == 'Customer':
                    query = "SELECT * FROM tbcustomer WHERE username= %s AND Password = %s"
                    data=(username,password)
                    cursor.execute(query,data)
                    result=cursor.fetchone()
                    messagebox.showinfo("success", "success") and self.open_customer() if result else messagebox.showerror("Error", "Error:No such user found as Customer")
                
                elif self.selected == 'Chef':
                    query = "SELECT * FROM tbchef WHERE username= %s AND Password = %s"
                    data=(username,password)
                    cursor.execute(query,data)
                    result=cursor.fetchone()
                    messagebox.showinfo("success", "success") and self.open_chef() if result else messagebox.showerror("error", "Error:No such user found as Chef")
                
                else:
                    messagebox.showwarning("Invalid",'Please select user type first')
            
            except Exception as e:
                print(f"Error: {e}")
                messagebox.showerror("Error", f"Error: {e}")
                return False
            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()
        else:
            messagebox.showinfo("Warning",'Please enter both username and password')
    
    
  
            
 
    def open_admin(self):

        self.master.destroy()  # Close the login window
        admin_app = Tk()
        from admin import dashboard_app
        admin_dashboard = dashboard_app(admin_app)
        admin_app.mainloop()
    
    def open_customer(self):
        self.master.destroy()
        customer_app = Tk()
        from customer import dashboard_customer
        dashboard_customer(customer_app)


    def open_staff(self):
        self.master.destroy()  # Close the login window
        admin_app = Tk()
        from staff import dashboard_app
        dashboard_app(admin_app)

    
    def open_chef(self):
        self.master.destroy() # Close the login window
        order_window= Tk()
        from chefforder import ChefOrder
        ChefOrder(order_window)
        

    def open_register_window(self):
        register_window=Toplevel(self.master)
        from customer_register import registerapp
        registerapp(register_window,bg_image=self.bg_image)

    
        
   
   

def main():
    root= Tk()
    login_app = login(root)
    root.mainloop()

if __name__ == '__main__':
    main()

