from tkinter import *
import os 
from tkinter import messagebox,Toplevel
from PIL import Image,ImageTk
import mysql.connector

class dahsboard_customer():

    def __init__(self,master):
        self.master = master
        self.master.geometry('900x600+0+2')
        self.master.title('Customer Dashboard')
        org =Image.open("customerapp.jpg")
        resize = org.resize((900,600))
        self.bg_image=ImageTk.PhotoImage(resize)


        label_img = Label(self.master,image=self.bg_image)
        label_img.pack()
        
        #Upper frame where title is going to be displayed

        #lower left frame where menus are going to be displayed
    #  ing buttons for the dashboard
    
        self.result = StringVar()
        self.label = Label(self.master)
        self.label.place(x=50,y=10)

        # #Menu button
        self.btn_Home = Button(self.master, text="Menu", command=self.open_customermenu_window,
                       width=15, height=3,  # Set width and height to make the button bigger
                       font=("Helvetica", 14, "bold"),  # Customize font
                       fg="white", bg="#8B4513")  # Customize foreground and background colors
        self.btn_Home.place(x=100, y=130)

        menu_img_path = "menu.jpg"
        org_img= Image.open(menu_img_path)
        res_img = org_img.copy()
        res_img.thumbnail((85,90))
        self.HomeIcon= ImageTk.PhotoImage(res_img)
        self.label_ico_menu = Label(self.master,image=self.HomeIcon)
        self.label_ico_menu.place(x=10,y=130)

        self.btn_order = Button(self.master, text="Order", command=self.open_customerorder_window,
                       width=15, height=3,  # Set width and height to make the button bigger
                       font=("Helvetica", 14, "bold"),  # Customize font
                       fg="white", bg="#8B4513")  # Customize foreground and background colors
        self.btn_order.place(x=100, y=228)

        order_img_path = "menu.jpg"
        org_img= Image.open(order_img_path)
        res_img = org_img.copy()
        res_img.thumbnail((85,90))
        self.HomeIcon= ImageTk.PhotoImage(res_img)
        self.label_ico_menu = Label(self.master,image=self.HomeIcon)
        self.label_ico_menu.place(x=10,y=228)

        self.btn_order = Button(self.master, text="Feedback", command=self.open_customerfeedback_window,
                       width=15, height=3,  # Set width and height to make the button bigger
                       font=("Helvetica", 14, "bold"),  # Customize font
                       fg="white", bg="#8B4513")  # Customize foreground and background colors
        self.btn_order.place(x=100, y=326)

        order_img_path = "menu.jpg"
        org_img= Image.open(order_img_path)
        res_img = org_img.copy()
        res_img.thumbnail((85,90))
        self.HomeIcon= ImageTk.PhotoImage(res_img)
        self.label_ico_menu = Label(self.master,image=self.HomeIcon)
        self.label_ico_menu.place(x=10,y=326)

        self.btn_order = Button(self.master, text="Logout", command=self.logout,
                       width=15, height=3,  # Set width and height to make the button bigger
                       font=("Helvetica", 14, "bold"),  # Customize font
                       fg="white", bg="#8B4513")  # Customize foreground and background colors
        self.btn_order.place(x=100, y=424)

        order_img_path = "menu.jpg"
        org_img= Image.open(order_img_path)
        res_img = org_img.copy()
        res_img.thumbnail((85,90))
        self.HomeIcon= ImageTk.PhotoImage(res_img)
        self.label_ico_menu = Label(self.master,image=self.HomeIcon)
        self.label_ico_menu.place(x=10,y=424)
        self.user = None
        self.password= None
        
    
    def set_credentials(self,username, pwd):
        self.user = username
        self.password = pwd
        print(f"{self.user,self.password} from tbcustomer")
        
    
    

    def displayname(self,username,password):
        
      
        username2 =username
        passwd = password
        try:
            connection = mysql.connector.connect(
                host='localhost',
                port='3306',
                user='root',
                password='',
                database='canteen_database1',
            )
            cursor = connection.cursor()
            

            cursor.execute("SELECT name FROM tbcustomer where username = %s and password = %s",(username2,passwd))
            self.result = cursor.fetchone()
            name = self.result[0].strip("()\"")

            if self.result is not None:
                print(name)
                self.label.config(text=name)
            else:
                print("No result")

        except Exception as e:
            print(f"Error: {e}")
            messagebox.showerror("Error", f"Error: {e}")
            return False


            
        
    
        
        
    def logout(self):
        self.master.destroy()
        from login import login
        master= Tk()

        login_app = login(master)
        master.mainloop()

    def open_order(self):
        from ordertry import Bill_App
        order_window=Tk()
        order_instance=Bill_App(order_window)
    def open_customer(self):
        from adminCustomer import customerDatabase
        customer_window=Tk()
        win_instance=customerDatabase(customer_window)  
    def open_staff(self):
        from adminStaff import staffDatabase
        staff_window=Tk()
        staff_instance=staffDatabase(staff_window)
    def open_customermenu_window(self):
        from customerMenu import CustomerMenu
        food_window= Tk()
        win_instance= CustomerMenu(food_window)
    def open_customerorder_window(self):
        from customerorder import CustomerOrder
        order_window= Tk()
        win_instance= CustomerOrder(order_window)

    def open_customerfeedback_window(self):
        register_window=Toplevel(self.master)
        from customerfeedback import feedback
        feedback(register_window,bg_image=self.bg_image)


def open_main():
    master = Tk()
    object_name = dahsboard_customer(master)
    
    master.mainloop()
if __name__ == "__main__":
    open_main()