from tkinter import *
import os 
from tkinter import messagebox,Toplevel
from PIL import Image,ImageTk
class dahsboard_chef():
    def __init__(self,master):
        self.master = master
        self.master.geometry('1300x700+0+2')
        self.master.title('chef Dashboard')
        
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

        #me.place(x=60,y=32)

        menu_img_path = "menu.jpg"
        org_img= Image.open(menu_img_path)
        res_img = org_img.copy()
        res_img.thumbnail((30,30))
        self.HomeIcon= ImageTk.PhotoImage(res_img)
        self.label_ico_menu = Label(self.l_f_frame,image=self.HomeIcon)
        self.label_ico_menu.place(x=10,y=30)

       

       
     

      

        


        #remaining frame where the background image as well as dashbaord contents is displayed
        rem_frame = Frame(self.master,bg='green')
        rem_frame.pack()
        self.bg_image=ImageTk.PhotoImage(Image.open("HC_hero16x9.jpg"))

        label_img = Label(rem_frame,image=self.bg_image)
        label_img.pack()


def open_main():
    master = Tk()
    object_name = dahsboard_chef(master)
    master.mainloop()
if __name__ == "__main__":
    open_main()