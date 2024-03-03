from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class CustomerMenu:
    def __init__(self, master):
        self.master = master
        self.master.title('Customer Menu')
        self.master.geometry('690x470')
        self.master.resizable(True,True)

        self.F1 = LabelFrame(self.master, text="Search Category", font=('times new roman', 15, 'bold'), bd=10)
        self.F1.pack(fill=X)
        cname_lbl = Label(self.F1, text="Food Category :", font=('times new roman', 15, 'bold'))
        cname_lbl.grid(row=0, column=0, padx=20, pady=5)
        self.combobox()
        self.category_combobox = ttk.Combobox(self.F1, state='readonly',values=self.categories)
        self.category_combobox.grid(row=0, column=1, padx=10, pady=5)
        self.category_combobox.bind("<<ComboboxSelected>>", self.display_menu_items)

        
        cname_lbl = Label(self.F1, text="Username:", font=('times new roman', 15, 'bold'))
        cname_lbl.grid(row=0, column=2, padx=20, pady=5)
        self.customer_id_entry = Entry(self.F1)
        self.customer_id_entry.grid(row=0, column=3, padx=10, pady=5)
        add_button = Button(self.F1, text='Add to Order', command=self.add_to_order)
        add_button.grid(row= 1, column=3, padx=10, pady=10)


        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='canteen_database1'
        )
        self.cursor = self.connection.cursor()

        self.display_frame =Frame(self.master)
        self.display_frame.pack()
    def combobox(self):
         try:
            connection = mysql.connector.connect(
                host='localhost',
                port='3306',
                user='root',
                password='',
                database='canteen_database1',
            )
            cursor = connection.cursor()
            

            cursor.execute("SELECT distinct name FROM tbfoodcategory")
            self.categories = [row[0] for row in cursor.fetchall()]
         except Exception as e:
            print(f"Error: {e}")
            messagebox.showerror("Error", f"Error: {e}")
            return False

    def display_menu_items(self, event=None):
        selected_category = self.category_combobox.get()
        if selected_category:
            query = "SELECT itemid, name, rate FROM tbfooditems WHERE categoryid = (SELECT categoryid FROM tbfoodcategory WHERE name = %s)"
            self.cursor.execute(query, (selected_category,))
            self.menu_items = self.cursor.fetchall()

            for widget in self.display_frame.winfo_children():
                widget.destroy()

            headings = ['S.N', 'Food Name', 'Price', 'Quantity']
            for i, heading in enumerate(headings):
                label = Label(self.display_frame, text=heading, font=('helvetica', 12, 'bold'))
                label.grid(row=0, column=i, padx=10, pady=5)

            self.quantity_entries = {}
            for i, item in enumerate(self.menu_items):
                food_id, food_name, price = item
                row_number = i + 1

                Label(self.display_frame, text=row_number).grid(row=row_number, column=0, padx=10, pady=5)
                Label(self.display_frame, text=food_name).grid(row=row_number, column=1, padx=10, pady=5)
                Label(self.display_frame, text=price).grid(row=row_number, column=2, padx=10, pady=5)

                quantity_entry = Entry(self.display_frame)
                quantity_entry.grid(row=row_number, column=3, padx=10, pady=5)
                self.quantity_entries[food_id] = quantity_entry

    def add_to_order(self):
        username_get = self.customer_id_entry.get()

        if not username_get:
            messagebox.showerror("Error", "Please enter a Customer ID.")
            return

        for item in self.menu_items:
            food_id, food_name, price = item
            quantity_entry = self.quantity_entries[food_id]  # Get the quantity entry widget
            quantity = quantity_entry.get()

            if quantity and quantity.isdigit() and int(quantity) > 0:
                quantity = int(quantity)
                total_price = float(price) * quantity
                try:
                    select_query =  "SELECT customerid from tbcustomer WHERE LOWER(username)  = LOWER(%s) "
                    self.cursor.execute(select_query,(username_get,))
                    fetch_id  =self.cursor.fetchone()
                    if not fetch_id:
                        messagebox.showerror("Error", "Invalid username")
                    else:
                        print(fetch_id)
                        insert_query = "INSERT INTO tborder(itemid, quantity, customerid, billamount) VALUES(%s, %s, %s, %s)"
                        values = (food_name, quantity, fetch_id[0], total_price)
                        self.cursor.execute(insert_query, values)
                        self.connection.commit()

                        messagebox.showinfo("Success", f"Added {food_name} to the order. Quantity: {quantity}, Total Price: Rs.{total_price}")
                except Exception as e:
                    print(f"Error: {e}")
                    messagebox.showerror("Error", f"Error: {e}")
                    return False

def main():
    root = Tk()
    app = CustomerMenu(root)
    root.mainloop()

if __name__ == "__main__":
    main()


     

