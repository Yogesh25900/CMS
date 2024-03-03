from tkinter import *
from tkinter import Toplevel
from PIL import Image,ImageTk
class dashboard_app():
    def __init__(self,master,**kwargs):
        self.master = master
        self.master.geometry('1300x700+0+2')
        self.master.title('Staff Dashboard')
        
        #Upper frame where title is going to be displayed

        self.upper_frame = LabelFrame(self.master, text="*"*900, font=('times new roman', 15, 'bold'), bd=10,bg='#c0dcc0')
        self.upper_frame .pack(side = TOP,fill=X)
        cname_lbl = Label(self.upper_frame , text="Welcome back !!!", font=('times new roman', 30, 'bold'),bg='#c0dcc0')
        cname_lbl.pack()
        
        
        #lower left frame where menus are going to be displayed
        self.l_f_frame = Frame(self.master,bg= '#c0dcc0',width=220,height=500)
        self.l_f_frame.pack(side=LEFT,fill=Y)
        

        # creating buttons for the dashboard

        #Menu button
        self.btn_Home = Button(self.l_f_frame,text="Menu",command=self.open_foodmenu_window,
                               width=9, height=2,  # Set width and height to make the button bigger
                       font=("Helvetica", 14, "bold"),  # Customize font
                       fg="white", bg="#8B4513")
        self.btn_Home.place(x=75,y=30)

        menu_img_path = "menu.png"
        org_img1= Image.open(menu_img_path)
        res_img1 = org_img1.copy()
        res_img1.thumbnail((60,60))
        self.menuIcon= ImageTk.PhotoImage(res_img1)
        self.label_ico_menu = Label(self.l_f_frame,image=self.menuIcon)
        self.label_ico_menu.place(x=10,y=30)

        #Customer button
        self.btn_menu = Button(self.l_f_frame,text="Customer",command=self.open_customer,
                               width=9, height=2,  # Set width and height to make the button bigger
                       font=("Helvetica", 14, "bold"),  # Customize font
                       fg="white", bg="#8B4513")
        self.btn_menu.place(x=75,y=100)

        customer_img_path = "customer.jpg"
        org_img2= Image.open(customer_img_path)
        res_img2 = org_img2.copy()
        res_img2.thumbnail((60,60))
        self.customerIcon= ImageTk.PhotoImage(res_img2)
        self.label_ico_customer = Label(self.l_f_frame,image=self.customerIcon)
        self.label_ico_customer.place(x=10,y=100)

        #Staff button
        self.btn_Customer = Button(self.l_f_frame,text="Order",command=self.open_stafforder_window,
                                   width=9, height=2,  # Set width and height to make the button bigger
                       font=("Helvetica", 14, "bold"),  # Customize font
                       fg="white", bg="#8B4513")
        self.btn_Customer.place(x=75,y=170)

        staff_img_path = "staf.jpg"
        org_img3= Image.open(staff_img_path)
        res_img3 = org_img3.copy()
        res_img3.thumbnail((60,60))
        self.staffIcon= ImageTk.PhotoImage(res_img3)
        self.label_ico_staff = Label(self.l_f_frame,image=self.customerIcon)
        self.label_ico_staff.place(x=10,y=170)


        #Bill button
        self.btn_Canteen = Button(self.l_f_frame,text="Bill",command=self.open_guestorder_window,
                                  width=9, height=2,  # Set width and height to make the button bigger
                       font=("Helvetica", 14, "bold"),  # Customize font
                       fg="white", bg="#8B4513")
        self.btn_Canteen.place(x=75,y=240)

        canteen_img_path = "canteen.jpg"
        org_img4= Image.open(canteen_img_path)
        res_img4 = org_img4.copy()
        res_img4.thumbnail((60,60))
        self.canteenIcon= ImageTk.PhotoImage(res_img4)
        self.label_ico_canteen = Label(self.l_f_frame,image=self.canteenIcon)
        self.label_ico_canteen.place(x=10,y=240)


        #Log out button
        self.btn_Staff = Button(self.l_f_frame,text="Log out",command=self.logout,
                        width=9, height=2,  # Set width and height to make the button bigger
                       font=("Helvetica", 14, "bold"),  # Customize font
                       fg="white", bg="#8B4513")
        self.btn_Staff.place(x=75,y=310)

        logout_img_path = "logout.png"
        org_img= Image.open(logout_img_path)
        res_img = org_img.copy()
        res_img.thumbnail((60,60))
        self.staffIcon= ImageTk.PhotoImage(res_img)
        self.label_ico_logout = Label(self.l_f_frame,image=self.staffIcon)
        self.label_ico_logout.place(x=10,y=310)

        


        #remaining frame where the background image as well as dashbaord contents is displayed
        rem_frame = Frame(self.master,bg='green')
        rem_frame.pack()
        self.bg_image=ImageTk.PhotoImage(Image.open("staffbg.png"))

        label_img = Label(rem_frame,image=self.bg_image)
        label_img.pack()

    def logout(self):
        self.master.destroy()
        from login import login
        master= Tk()

        login_app = login(master)
        master.mainloop()
    #     self.master.destroy()
    #     master=Tk()
    #     app = Bill_App(master)
    #     master.mainloop()
    def open_order(self):
        from ordertry import Bill_App
        order_window=Tk()
        order_instance=Bill_App(order_window)
    def open_customer(self):
        register_window=Toplevel(self.master)
        from customerCRUD import cruduser
        cruduser(register_window,bg_image=self.bg_image)

    def open_staff(self):
        from adminStaff import staffDatabase
        staff_window=Tk()
        staff_instance=staffDatabase(staff_window)
    def open_foodmenu_window(self):
        food_window = Toplevel(self.master)
        from staffmenu import staffMenu
        staffMenu(food_window,bg_image = self.bg_image)
    def open_stafforder_window(self):
        from stafforder import StaffOrder
        order_window= Tk()
        win_instance= StaffOrder(order_window)
    def open_guestorder_window(self):
        from ordertry import Bill_App
        order_window = Toplevel(self.master)

        Bill_App(order_window)
      
    
        

def open_main():
    master = Tk()
    object_name = dashboard_app(master)
    master.mainloop()
if __name__ == "__main__":
    open_main()