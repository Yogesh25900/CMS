from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector

class ChefOrder:
    def __init__(self, master):
        self.master = master
        self.master.title('Chef Order')
        self.master.geometry('920x550+0+2')

        # Create a frame to hold the order display
       
        rem_frame = Frame(self.master,bg='white',bd=2,relief=GROOVE)
        rem_frame.pack(side=LEFT)
        image = Image.open("chefbg.jpg")
        res_img = image.resize((425,550))
        self.bg_image=ImageTk.PhotoImage(res_img)

        label_img = Label(rem_frame,image=self.bg_image)
        label_img.pack()


        #lower left frame where menus are going to be displayed
        self.order_frame = Frame(self.master,bg= 'light grey',relief=GROOVE,bd=2)
        self.order_frame.pack()
       

        # Display headings

        # Fetch orders with NULL or 'Not Delivered' order status from tborder
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='canteen_database1'
        )
        self.cursor = self.connection.cursor()

        self.fetch_orders()  # Initial fetch and display orders

        # Refresh button
        refresh_button = Button(self.master, text='Refresh', command=self.fetch_orders)
        refresh_button.pack(pady=10)

    def fetch_orders(self):
        # Clear previous orders
        for widget in self.order_frame.winfo_children():
            widget.destroy()

        # Display headings again
        headings = ['Order ID', 'Food Names']
        for i, heading in enumerate(headings):
            label = Label(self.order_frame, text=heading,bg='light grey', font=('helvetica', 20, 'bold'))
            label.grid(row=0, column=i, padx=50, pady=20)

        # Fetch orders with NULL or 'Not Delivered' order status from tborder
        query = "SELECT orderid, GROUP_CONCAT(itemid) FROM tborder WHERE orderstatus IS NULL OR orderstatus = 'Undelivered' GROUP BY orderid"
        self.cursor.execute(query)
        orders = self.cursor.fetchall()

        # Display order details
        for i, order in enumerate(orders):
            order_id, food_names = order
            row_number = i + 1

            Label(self.order_frame,bg= 'light grey',font=('helvetica') ,text=order_id).grid(row=row_number, column=0, padx=10, pady=5)
            Label(self.order_frame,bg= 'light grey' ,font=('helvetica'),text=food_names).grid(row=row_number, column=1, padx=10, pady=5)



def main():
    root = Tk()
    ChefOrder(root)
    root.mainloop()

if __name__ == "__main__":
    main()
