from tkinter import *
import os 
from tkinter import messagebox,Toplevel
from PIL import Image,ImageTk
import mysql.connector

class dashboard_customer():

    def __init__(self,master,**kwargs):
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

        menu_img_path = "menu.png"
        org_img1= Image.open(menu_img_path)
        res_img1 = org_img1.copy()
        res_img1.thumbnail((85,90))
        self.menuIcon= ImageTk.PhotoImage(res_img1)
        self.label_ico_menu = Label(self.master,image=self.menuIcon)
        self.label_ico_menu.place(x=10,y=130)

        self.btn_order = Button(self.master, text="Order", command=self.open_customerorder_window,
                       width=15, height=3,  # Set width and height to make the button bigger
                       font=("Helvetica", 14, "bold"),  # Customize font
                       fg="white", bg="#8B4513")  # Customize foreground and background colors
        self.btn_order.place(x=100, y=228)

        order_img_path = "order.png"
        org_img2= Image.open(order_img_path)
        res_img2 = org_img2.copy()
        res_img2.thumbnail((85,90))
        self.orderIcon= ImageTk.PhotoImage(res_img2)
        self.label_ico_order = Label(self.master,image=self.orderIcon)
        self.label_ico_order.place(x=10,y=228)

        self.btn_order = Button(self.master, text="Feedback", command=self.open_customerfeedback_window,
                       width=15, height=3,  # Set width and height to make the button bigger
                       font=("Helvetica", 14, "bold"),  # Customize font
                       fg="white", bg="#8B4513")  # Customize foreground and background colors
        self.btn_order.place(x=100, y=326)

        fdback_img_path = "feedback.png"
        org_img3= Image.open(fdback_img_path)
        res_img3 = org_img3.copy()
        res_img3.thumbnail((85,90))
        self.fdIcon= ImageTk.PhotoImage(res_img3)
        self.label_ico_feedback = Label(self.master,image=self.fdIcon)
        self.label_ico_feedback.place(x=10,y=326)

        self.btn_order = Button(self.master, text="Logout", command=self.logout,
                       width=15, height=3,  # Set width and height to make the button bigger
                       font=("Helvetica", 14, "bold"),  # Customize font
                       fg="white", bg="#8B4513")  # Customize foreground and background colors
        self.btn_order.place(x=100, y=424)

        logout_img_path = "logout.png"
        org_img4= Image.open(logout_img_path)
        res_img4 = org_img4.copy()
        res_img4.thumbnail((85,90))
        self.logoutIcon= ImageTk.PhotoImage(res_img4)
        self.label_ico_lgout = Label(self.master,image=self.logoutIcon)
        self.label_ico_lgout.place(x=10,y=424)
        self.user = None
        self.password= None
        
    
   

            
        
    
        
        
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
    # def open_customer(self):
    #     from adminCustomer import customerDatabase
    #     customer_window=Tk()
    #     win_instance=customerDatabase(customer_window)  
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
    object_name = dashboard_customer(master)
    
    master.mainloop()
if __name__ == "__main__":
    open_main()