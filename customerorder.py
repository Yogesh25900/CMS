from tkinter import *
import mysql.connector
from tkinter import ttk
from tkinter import messagebox

class CustomerOrder:
    def __init__(self, master):
        self.master = master
        self.master.title('Customer Orders')
        self.master.geometry('800x600')
        self.total_price = 0

        # Customer ID entry and search button
        self.F1 = LabelFrame(self.master, text="Search your orders", font=('times new roman', 15, 'bold'), bd=10)
        self.F1.pack(fill=X)
        cname_lbl = Label(self.F1, text="USername :", font=('times new roman', 15, 'bold'))
        cname_lbl.grid(row=0, column=0, padx=20, pady=5)
        self.customer_id_entry = Entry(self.F1, width=15, font='arial 15', bd=7, relief=GROOVE)
        self.customer_id_entry.grid(row=0, column=1, pady=5, padx=10)

        search_button = Button(self.F1, text='Search', command=self.display_orders)
        search_button.grid(row=0, column=2, padx=10, pady=5)
         # Display total price


        # Connect to the database
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='canteen_database1'
        )
        self.cursor = self.connection.cursor()
        self.display_frame = Frame(self.master)
        self.display_frame.pack()
        # Display headings
        headings = ['Order ID', 'Food Name', 'Quantity', 'Price','Edit']
        for i,heading in enumerate(headings):
            label = Label(self.display_frame, text=heading, font=('helvetica', 12, 'bold'))
            label.grid(row=1, column=i, padx=50, pady=5)

    def display_orders(self):
        # Retrieve customer ID from the entry field
        username_get = self.customer_id_entry.get()

        # Clear existing entries in the display
        for widget in self.display_frame.winfo_children():
            if isinstance(widget, Label):
                widget.destroy()

        # Display headings again
        headings = ['Order ID', 'Food Name', 'Quantity', 'Price','Edit']
        for i, heading in enumerate(headings):
            label = Label(self.display_frame, text=heading, font=('helvetica', 12, 'bold'))
            label.grid(row=1, column=i, padx=50, pady=5)

      
        # Fetch orders for the specific customer
        select_query =  "SELECT customerid from tbcustomer WHERE LOWER(username)  = LOWER(%s) "
        self.cursor.execute(select_query,(username_get,))
        fetch_id  =self.cursor.fetchone()
        query = "SELECT orderid, itemid, quantity, billamount FROM tborder WHERE customerid = %s AND (orderstatus = 'Undelivered' or orderstatus is NULL)"
        self.cursor.execute(query, (fetch_id[0],))
        orders = self.cursor.fetchall()
        

        if not orders:
            messagebox.showinfo("Information", f"No orders found for Customer ID: {username_get}")
            return

        self.total_price=0

        for i, order in enumerate(orders):
            order_id, food_name, quantity, price = order
            orderid =order[0]
            row_number = i + 2

            Label(self.display_frame, text=order_id).grid(row=row_number, column=0, padx=10, pady=5)
            Label(self.display_frame, text=food_name).grid(row=row_number, column=1, padx=10, pady=5)
            Label(self.display_frame, text=quantity).grid(row=row_number, column=2, padx=10, pady=5)
            Label(self.display_frame, text=price).grid(row=row_number, column=3, padx=10, pady=5)

            self.delete_button = Button(self.display_frame, text='Delete', command=lambda order_id=order_id, row_number=row_number: self.delete_order(order_id, row_number))
            self.delete_button.grid(row=row_number, column=4, padx=10, pady=5)



            
            # Convert price to float before displaying
            price_float = float(price)

            
            self.total_price += price_float
        total_label = Label(self.F1, text=f'Total Price: Rs.{self.total_price:.2f}', font=('helvetica', 12, 'bold'))
        total_label.grid(row=0, column=3, padx=10, pady=5)

       
    def delete_order(self, order_id,row_number):
# Query to delete the order from the database
        query = "DELETE FROM tborder WHERE orderid = %s"
        self.cursor.execute(query, (order_id,))
        self.connection.commit()

        for widget in self.display_frame.grid_slaves():
            if int(widget.grid_info()["row"]) == row_number:
                widget.grid_forget()
        self.delete_button.grid_forget()

        self.delete_button.destroy()


def open_customerorder_window(self):
    from customerorder import CustomerOrder
    order_window= Tk()
    win_instance= CustomerOrder(order_window)
    order_window.mainloop()
def main():
    root = Tk()
    app = CustomerOrder(root)
    root.mainloop()

if __name__ == "__main__":
    main()
