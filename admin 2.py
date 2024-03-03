from tkinter import *
from tkinter import messagebox,Toplevel
from PIL import Image,ImageTk
class dashboard_app():
    def __init__(self,master):
        self.master = master
        self.master.geometry('830x500+0+2')
        self.master.resizable(False,False)
        self.master.title('Admin Dashboard')
        
        #Upper frame where title is going to be displayed
       
        self.upper_frame = LabelFrame(self.master, text="*"*900, font=('times new roman', 15, 'bold'), bd=10,bg='#c0dcc0')
        self.upper_frame .pack(side = TOP,fill=X)
        cname_lbl = Label(self.upper_frame , text="Welcome back Admin !!!", font=('times new roman', 30, 'bold'),bg='#c0dcc0')
        cname_lbl.pack()
       
        #lower left frame where menus are going to be displayed
        self.l_f_frame = Frame(self.master,bg= '#c0dcc0',width=220,height=500)
        self.l_f_frame.pack(side=LEFT,fill=Y)
        

        # creating buttons for the dashboard

    
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
        self.btn_staff = Button(self.l_f_frame,text="Staff",command=self.open_staff,
                                   width=9, height=2,  # Set width and height to make the button bigger
                       font=("Helvetica", 14, "bold"),  # Customize font
                       fg="white", bg="#8B4513")
        self.btn_staff.place(x=75,y=170)

        staff_img_path = "staff.png"
        org_img3= Image.open(staff_img_path)
        res_img3 = org_img3.copy()
        res_img3.thumbnail((60,60))
        self.staffIcon= ImageTk.PhotoImage(res_img3)
        self.label_ico_staff = Label(self.l_f_frame,image=self.staffIcon)
        self.label_ico_staff.place(x=10,y=170)


        #Bill button
        self.btn_cheff = Button(self.l_f_frame,text="Chef",command=self.open_chef,
                                  width=9, height=2,  # Set width and height to make the button bigger
                       font=("Helvetica", 14, "bold"),  # Customize font
                       fg="white", bg="#8B4513")
        self.btn_cheff.place(x=75,y=240)

        canteen_img_path = "chef.png"
        org_img4= Image.open(canteen_img_path)
        res_img4 = org_img4.copy()
        res_img4.thumbnail((60,60))
        self.cheffIcon= ImageTk.PhotoImage(res_img4)
        self.label_ico_canteen = Label(self.l_f_frame,image=self.cheffIcon)
        self.label_ico_canteen.place(x=10,y=240)


        # #Log out button
        self.btn_logout = Button(self.l_f_frame,text="Log out",command=self.logout,
                        width=9, height=2,  # Set width and height to make the button bigger
                       font=("Helvetica", 14, "bold"),  # Customize font
                       fg="white", bg="#8B4513")
        self.btn_logout.place(x=75,y=310)

        logout_img_path = "logout.png"
        org_img5= Image.open(logout_img_path)
        res_img5 = org_img5.copy()
        res_img5.thumbnail((60,60))
        self.logoutIcon= ImageTk.PhotoImage(res_img5)
        self.label_ico_logout = Label(self.l_f_frame,image=self.logoutIcon)
        self.label_ico_logout.place(x=10,y=310)

        
        


        #remaining frame where the background image as well as dashbaord contents is displayed
        rem_frame = Frame(self.master,bg='green')
        rem_frame.pack()
        bgimage = Image.open("admindasboard.jpg")
        self.bg_image=ImageTk.PhotoImage(bgimage)

        label_img = Label(rem_frame,image=self.bg_image)
        label_img.pack()

    def logout(self):
        self.master.destroy() 
        from login import login
        master= Tk()

        login_app = login(master)
        master.mainloop()
   
    def open_chef(self):
        cheff_window=Toplevel(self.master)
        from admincheff import crudchef
        crudchef(cheff_window,bg_image=self.bg_image) 

    def open_staff(self):
        staff_window=Toplevel(self.master)
        from adminStaff import crudstaff
        crudstaff(staff_window,bg_image=self.bg_image)

    def open_customer(self):
        customer_window=Toplevel(self.master)
        from customerCRUD import cruduser
        cruduser(customer_window,bg_image=self.bg_image)


def open_main():
    master = Tk()
    object_name = dashboard_app(master)
    master.mainloop()
if __name__ == "__main__":
    open_main()