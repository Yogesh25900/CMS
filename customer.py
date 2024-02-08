from tkinter import *
import os 
from tkinter import messagebox,Toplevel
from PIL import Image,ImageTk
class dahsboard_customer():
    def __init__(self,master):
        self.master = master
        self.master.geometry('1300x700+0+2')
        self.master.title('Customer Dashboard')
        
        #Upper frame where title is going to be displayed
        self.upper_frame = Frame(self.master,bd= 10,bg='white')
        self.upper_frame.pack(side=TOP,fill=X)
        self.upper_label = Label(self.upper_frame,text="This is the upper frame")
        self.upper_label.pack()
        #lower left frame where menus are going to be displayed
        self.l_f_frame = Frame(self.master,bg= '#c0dcc0',width=130,height=500)
        self.l_f_frame.pack(side=LEFT,fill=Y)
        self.label = Label(self.l_f_frame,text="This is the lower left frame")
        self.label.pack()

        # creating buttons for the dashboard

        #Menu button
        self.btn_Home = Button(self.l_f_frame,text="Menu")
        self.btn_Home.place(x=60,y=32)

        menu_img_path = "menu.jpg"
        org_img= Image.open(menu_img_path)
        res_img = org_img.copy()
        res_img.thumbnail((30,30))
        self.HomeIcon= ImageTk.PhotoImage(res_img)
        self.label_ico_menu = Label(self.l_f_frame,image=self.HomeIcon)
        self.label_ico_menu.place(x=10,y=30)

       

        #Staff button
        self.btn_Customer = Button(self.l_f_frame,text="Order")
        self.btn_Customer.place(x=60,y=80)

        customer_img_path = "staf.jpg"
        org_img= Image.open(customer_img_path)
        res_img = org_img.copy()
        res_img.thumbnail((30,30))
        self.customerIcon= ImageTk.PhotoImage(res_img)
        self.label_ico_customer = Label(self.l_f_frame,image=self.customerIcon)
        self.label_ico_customer.place(x=10,y=80)

        self.btn_Staff = Button(self.l_f_frame,text="Feedback")
        self.btn_Staff.place(x=60,y=128)

        #Log out button
        self.btn_Staff = Button(self.l_f_frame,text="Log out")
        self.btn_Staff.place(x=60,y=170)

        staff_img_path = "lgout.jpg"
        org_img= Image.open(staff_img_path)
        res_img = org_img.copy()
        res_img.thumbnail((30,30))
        self.staffIcon= ImageTk.PhotoImage(res_img)
        self.label_ico_staff = Label(self.l_f_frame,image=self.staffIcon)
        self.label_ico_staff.place(x=10,y=128)

        


        #remaining frame where the background image as well as dashbaord contents is displayed
        rem_frame = Frame(self.master,bg='green')
        rem_frame.pack()
        self.bg_image=ImageTk.PhotoImage(Image.open("HC_hero16x9.jpg"))

        label_img = Label(rem_frame,image=self.bg_image)
        label_img.pack()

   
    #     self.master.destroy()
    #     master=Tk()
    #     app = Bill_App(master)
    #     master.mainloop()
    
        

def open_main():
    master = Tk()
    object_name = dahsboard_customer(master)
    master.mainloop()
if __name__ == "__main__":
    open_main()