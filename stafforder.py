from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class StaffOrder:
    def __init__(self, master):
        self.master = master
        self.master.title('Staff Order')
        self.master.geometry('800x600')

        # Create a frame to hold the staff order display
        self.order_frame = Frame(self.master)
        self.order_frame.pack(expand=True, fill='both')

        # Display headings
        headings = ['Customer ID', 'Order ID', 'Total Price', 'Payment Status', 'Order Status', 'Actions']
        for i, heading in enumerate(headings):
            label = Label(self.order_frame, text=heading, font=('helvetica', 12, 'bold'))
            label.grid(row=1, column=i, padx=10, pady=5)

        # Payment status ComboBox
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='canteen_database1'
        )
        self.cursor = self.connection.cursor()

        # Fetch undelivered orders initially
        self.fetch_undelivered_orders()

    def fetch_undelivered_orders(self):
        # Fetch undelivered orders from tborder
        query = "SELECT customerid, GROUP_CONCAT(orderid), SUM(billamount), MAX(paymentstatus), MAX(orderstatus) FROM tborder WHERE orderstatus is Null or orderstatus = 'Undelivered' GROUP BY customerid"
        self.cursor.execute(query)
        orders = self.cursor.fetchall()

        # Display order details
        for i, order in enumerate(orders):
            customer_id, order_ids, total_price, payment_status, order_status = order
            row_number = i + 2  # Start from row 2 to leave space for headings

            Label(self.order_frame, text=customer_id).grid(row=row_number, column=0, padx=10, pady=5)
            Label(self.order_frame, text=order_ids).grid(row=row_number, column=1, padx=10, pady=5)
            Label(self.order_frame, text=f"${float(total_price):.2f}").grid(row=row_number, column=2, padx=10, pady=5)

            # Payment status ComboBox under the "Payment Status" column
            payment_status_combobox = ttk.Combobox(self.order_frame, values=['Not Paid', 'Paid'], state='readonly')
            payment_status_combobox.grid(row=row_number, column=3, padx=10, pady=5)

            if payment_status:  # Check if payment_status is not None or empty
                payment_status_combobox.set(payment_status)  # Set the initial value

            # Order status ComboBox under the "Order Status" column
            order_status_combobox = ttk.Combobox(self.order_frame, values=['Undelivered', 'Delivered'], state='readonly')
            order_status_combobox.grid(row=row_number, column=4, padx=10, pady=5)

            if order_status:  # Check if order_status is not None or empty
                order_status_combobox.set(order_status)  # Set the initial value

            # Button to update payment and order status
            update_button = Button(self.order_frame, text='Update', command=lambda id=customer_id, payment_cb=payment_status_combobox, order_cb=order_status_combobox: self.update_status(id, payment_cb, order_cb))
            update_button.grid(row=row_number, column=5, padx=10, pady=5)

    def update_status(self, customer_id, payment_status_combobox, order_status_combobox):
        # Update payment status in tborder table
        payment_status = payment_status_combobox.get()
        update_payment_query = "UPDATE tborder SET paymentstatus = %s WHERE customerid = %s"
        self.cursor.execute(update_payment_query, (payment_status, customer_id))

        # Update order status in tborder table
        order_status = order_status_combobox.get()
        update_order_query = "UPDATE tborder SET orderstatus = %s WHERE customerid = %s"
        self.cursor.execute(update_order_query, (order_status, customer_id))

        self.connection.commit()
        messagebox.showinfo("Success", f"Status updated for Customer ID: {customer_id}")

def open_stafforder_window():
    food_window= Tk()
    win_instance= StaffOrder(food_window)
    food_window.mainloop()
def main():
    root = Tk()
    app = StaffOrder(root)
    root.mainloop()

if __name__ == "__main__":
    main()
