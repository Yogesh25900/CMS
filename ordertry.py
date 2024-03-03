
from tkinter import*
import random
from tkinter import messagebox
import mysql.connector
from tkinter import filedialog

from fpdf import FPDF  # Import FPDF for PDF generation


# ============main============================

class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Guest Orders")
        title = Label(self.root, text="Guest Ordering", font=('times new roman', 30, 'bold'), pady=2, bd=12, bg="white", relief=GROOVE)
        title.pack(fill=X)

      
    # ================variables=======================
    
     
       
        

        
    # ==============Total product================
    
        self.total_food_price = IntVar()
       
        self.bill = IntVar()
        
    # ==============Customer==========================
    
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()
    
        
    # =============customer retail details======================
    
        F1 = LabelFrame(self.root, text="Customer Details", font=('times new roman', 15, 'bold'), bd=10)
        F1.place(x=0, y=80, relwidth=1)
        cname_lbl = Label(F1, text="Customer Name:", font=('times new roman', 15, 'bold'))
        cname_lbl.grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, font='arial 15', bd=7, relief=GROOVE)
        cname_txt.grid(row=0, column=1, pady=5, padx=10)

        cphn_lbl = Label(F1, text="Customer Phone:", font=('times new roman', 15, 'bold'))
        cphn_lbl.grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.c_phone, font='arial 15', bd=7, relief=GROOVE)
        cphn_txt.grid(row=0, column=3, pady=5, padx=10)

        c_bill_lbl = Label(F1, text="Bill Number:", font=('times new roman', 15, 'bold'))
        c_bill_lbl.grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15, textvariable=self.search_bill, font='arial 15', bd=7, relief=GROOVE)
        c_bill_txt.grid(row=0, column=5, pady=5, padx=10)

        
    # ==========MenuItems=========================
    
        F3 = LabelFrame(self.root, text="Main Items", font=('times new roman', 15, 'bold'), bd=10)
        F3.place(x=80, y=180, width=350, height=380)


        #connection to database
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='canteen_database1'
        )
        self.cursor = self.connection.cursor()

        query = "SELECT  itemid,name, rate FROM tbfooditems"
        self.cursor.execute(query)
        self.menu_items = self.cursor.fetchall()

        
        # Display menu items and add entry for quantity
        
        self.quantity_entries = {}
        for i, item in enumerate(self.menu_items):
            foodid,food_name, price = item
            row_number = i + 1

            Label(F3, text=food_name).grid(row=row_number, column=0, padx=10, pady=5)
            Label(F3, text=price).grid(row=row_number, column=1, padx=10, pady=5)

            quantity_entry = Entry(F3)
            quantity_entry.grid(row=row_number, column=3, padx=10, pady=5)
            quantity_entry.insert(0, "0")

            self.quantity_entries[foodid] = quantity_entry

      
    
       
    # BillArea
    
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=920, y=180, width=385, height=390)
        #usually the standard one is 101.6 x 152.4 ....can be changed afterwards

        bill_title = Label(F5, text="Bill Area", font='arial 15 bold', bd=7, relief=GROOVE)
        bill_title.pack(fill=X)
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

    #ButtonFrame
    
        self.F6 = LabelFrame(self.root, text="Calculation", font=('times new roman', 14, 'bold'), bd=10)
        self.F6.place(x=0, y=560, relwidth=1, height=140)


        m2_lbl = Label(self.F6, text="Total Food Price", font=('times new roman', 14, 'bold'))
        m2_lbl.grid(row=1, column=0, padx=20, pady=1, sticky='W')
        m2_txt = Entry(self.F6, width=18, textvariable=self.total_food_price, font='arial 10 bold', bd=7, relief=GROOVE)
        m2_txt.grid(row=1, column=1, padx=18, pady=1)

       

   

     
    # Buttons
    
        btn_f = Frame(self.F6, bd=7)
        btn_f.place(x=600, width=700, height=105)

        total_btn = Button(btn_f, command=self.total, text="Total", bg="black", bd=2, fg="white", pady=15, width=12, font='arial 13 bold')
        total_btn.grid(row=0, column=0, padx=5, pady=5)

        generateBill_btn = Button(btn_f, command=self.bill_area, text="Generate Bill", bd=2,bg='black', fg="white", pady=12, width=12, font='arial 13 bold')
        generateBill_btn.grid(row=0, column=1, padx=5, pady=5)

        printBill_btn = Button(btn_f, command=self.save_bill, text="Print Bill", bd=2,bg='black', fg="white", pady=12, width=12, font='arial 13 bold')
        printBill_btn.grid(row=0, column=2, padx=5, pady=5)

        exit_btn = Button(btn_f, command=self.exit_app, text="Exit", bd=2,bg='black', fg="white", pady=12, width=12, font='arial 13 bold')
        exit_btn.grid(row=0, column=3, padx=5, pady=5)
       

#totalBill

    def total(self):
        #total food price
        food_price=0

        for item in self.menu_items:
            food_id, food_name, price = item
            quantity_entry = self.quantity_entries[food_id]  # Get the quantity entry widget
            quantity = quantity_entry.get()

            try:
                quantity = float(quantity)
            except ValueError:
                quantity = 0.0
            try:
                prices = float(price)
            except ValueError:
                price = 0.0

            food_price += (prices) * quantity
        print(food_price)
        self.total_food_price.set(food_price)
        self.bill.set(food_price)
        m2_txt = Entry(self.F6, width=18, textvariable=self.total_food_price, font='arial 10 bold', bd=7, relief=GROOVE)
        m2_txt.grid(row=1, column=1, padx=18, pady=1)
        #welcome-bill

    def bill_area(self):
        try:
            if self.c_name:
                print(self.c_name.get())
        except Exception as e:
            print(e)
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\t        Receipt")
        self.txtarea.insert(END, f"\nBill Number: {self.bill_no.get()}")
        self.txtarea.insert(END, f"\nCustomer Name: {self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone Number: {self.c_phone.get()}")
        self.txtarea.insert(END, f"\n=====================================")
        self.txtarea.insert(END, "\n {:<20} {:<10} {}".format("Products", "Quantity", 'Price'))
        print(self.c_name.get())
        

        # Iterate over menu items
        for item in self.menu_items:
            food_id, food_name, price = item
            quantity_entry = self.quantity_entries[food_id]  # Get the quantity entry widget
            quantity = quantity_entry.get().strip()


            if quantity.isdigit() and int(quantity) > 0 :
                # Display product details in the bill
                total_item_price = int(quantity) * float(price)

                self.txtarea.insert(END, "\n {:<20} {:<10} {}".format(food_name, quantity, total_item_price))
                
        

        # Calculate the total price
        total_price = self.bill.get()

        self.txtarea.insert(END, f"\n-------------------------------------")
        self.txtarea.insert(END, "\n {:<30} ".format(f"Total:  Rs.{total_price}"))
        self.bill_text = self.txtarea.get("1.0", "end-1c")

        # self.save_bill()
        print(self.bill_text)
# 

    #=========savebill============================
    
  
    from fpdf import FPDF  # Import FPDF for PDF generation

    def save_bill(self):
    # Your existing code to create the bill text
        bill_text = self.txtarea.get("1.0", "end-1c")

        # Ask the user for the file name and location
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")], initialdir=r"C:\Users\Yogesh\Desktop\git project test\CMS\bills")

        if file_path:
            # Create a PDF document
            pdf = FPDF()
            pdf = FPDF('P', 'mm', (135, 170))
            pdf.add_page()
            pdf.set_font("Courier", size=12)
            
            # Write the bill text to the PDF
            pdf.multi_cell(0, 10, bill_text)
            
            # Save the PDF document
            pdf.output(file_path)

            messagebox.showinfo("Success", f"Bill saved as {file_path}")

    # ===================find_bill================================
    
    

    # ===========exit=======================
    
    def exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op == 1:
            self.root.destroy()

def open_guestorder_window():
    order_window=Tk()
    # order_window = Toplevel(parent)
    Bill_App(order_window)
    order_window.mainloop()
def main():
    root = Tk()
    Bill_App(root)
    root.mainloop()
if  __name__=="__main__":
    main()


