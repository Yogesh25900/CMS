from tkinter import *
import mysql.connector
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk,Image

class staffMenu:
    def __init__(self,master,**kwargs):
        self.master = master
        self.master.title('Staff Menu')
        self.master.geometry('1000x700+0+2')
        
        self.host ="localhost"
        self.port ='3306'
        self.database='canteen_database1'
        self.user='root'
        self.password=''
        


        #assigning variable for food table
        self.foodid = StringVar()
        self.food_name =StringVar()
        self.mail =StringVar()
        self.rate =StringVar()
        self.address =StringVar()
        self.username =StringVar()
        self.key =StringVar()

   
        file ="foodmenubg.jpg"
        org =Image.open(file)
        resize = org.resize((1000,700))
        self.bg_image=ImageTk.PhotoImage(resize)

        label_img = Label(self.master,image=self.bg_image)
        label_img.pack()

         #new frame for registering foods
        self.register_frame = LabelFrame(self.master,text="Food Menu",bd=7,relief=GROOVE,width=400,height=450)
        self.register_frame.place(x=200,y=100)
       
        #frame for buttons
        

        label_id = Label(self.register_frame, text="Enter Food Name")
        label_id.place(x=2,y=235)
        self.searchid= StringVar()
        entry_search = Entry(self.register_frame, width=20,textvariable=self.searchid)
        entry_search.place(x=200,y=235)

        search_button = Button(self.register_frame, text="Search",command=self.search_foods)
        search_button.place(x=80,y=267)

        register_button = Button(self.register_frame, text="Add",command=self.add_food)  # Add a command to register new foods
        register_button.place(x=150,y=267)

        update_button = Button(self.register_frame, text="Update",command=self.update_food)
        update_button.place(x=200,y=267)

        delete_button = Button(self.register_frame, text="Delete", command=self.delete_food)  # Add a command to delete foods
        delete_button.place(x=280,y=267)

        

        

       

        self.label_cname= Label(self.register_frame, text="Food Name")
        self.label_cname.place(x=2,y=35)
        self.e2= Entry(self.register_frame, width=30,textvariable=self.food_name)
        self.e2.place(x=90,y=35)
        self.combobox()

        Label(self.register_frame, text="Food Category:").place(x=2,y=67)
        self.food_category_combobox = ttk.Combobox(self.register_frame, values=self.categories,state="readonly")
        self.food_category_combobox.place(x=90,y=67)
        self.food_category_combobox.set("Select Category")

        
        # Populate combobox with food categories

        self.label_rate=Label(self.register_frame, text="Rate")
        self.label_rate.place(x=2,y=99)
        self.e3=Entry(self.register_frame, width=30,textvariable=self.rate)
        self.e3.place(x=90,y=99)

       
    def combobox(self):
         try:
            connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database,
            )
            cursor = connection.cursor()
            

            cursor.execute("SELECT distinct name FROM tbfoodcategory")
            self.categories = [row[0] for row in cursor.fetchall()]
         except Exception as e:
            print(f"Error: {e}")
            messagebox.showerror("Error", f"Error: {e}")
            return False
        
    
    #add new food to DB
    def add_food(self):
        name= self.food_name.get()
        category_name= self.food_category_combobox.get()
        rate=self.rate.get()
        
        try:
            connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database,
            )
            cursor = connection.cursor()
            
            cursor.execute("SELECT categoryid from tbfoodcategory WHERE name = %s",(category_name,))
            category_id = cursor.fetchone()[0]
            query ="INSERT INTO tbfooditems(name,rate,categoryid) VALUES (%s,%s,%s)"
            values =(name,rate,category_id)
            cursor.execute(query,values)
            connection.commit()
            messagebox.showinfo("Success","food registered Successfully")
        except Exception as e:
            print(f"Error: {e}")
            messagebox.showerror("Error", f"Error: {e}")
            return False
        finally:
            
            cursor.close()
            connection.close()
    #edit food
    def update_food(self):
        c_id =self.searchid.get()
        name= self.food_name.get()
        category_name= self.food_category_combobox.get()

        rate=self.rate.get()
        
        try:
            connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database,
            )
            cursor = connection.cursor()

            cursor.execute("SELECT itemid from tbfooditems WHERE LOWER(name)= %s",(c_id,))
            id = cursor.fetchone()[0]

            cursor.execute("SELECT categoryid from tbfoodcategory WHERE name = %s",(category_name,))
            category_id = cursor.fetchone()[0]
            
            query ="UPDATE tbfooditems SET name=%s,rate=%s,categoryid =%s where itemid=%s "
            values =(name,rate,category_id,id)

            cursor.execute(query, values)
            connection.commit()
            messagebox.showinfo("Success", "food details updated successfully!")

        except Exception as e:
            print(f"Error: {e}")
            messagebox.showerror("Error", f"Error: {e}")
            return False
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    #deleting the food
    def delete_food(self):
        name =self.searchid.get()

        try:
            connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database,
            )
            cursor = connection.cursor()
            
            

            query = "DELETE FROM tbfooditems WHERE LOWER(name)=LOWER(%s)"
            values = (name,)

            cursor.execute(query, values)
            connection.commit()
            messagebox.showinfo("Success", "food deleted successfully!")
            self.e2.delete(0, END)
            self.e3.delete(0, END)
            self.food_category_combobox.set("Select Category")

           


        except Exception as e:
            print(f"Error: {e}")
            messagebox.showerror("Error", f"Error: {e}")
            return False
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    def search_foods(self):
        c_id =self.searchid.get()


        try:
            connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database,
            )
            cursor=connection.cursor()


            query = "SELECT * FROM tbfooditems WHERE itemid=%s or LOWER(name)= LOWER(%s)"
            values = (c_id,c_id)
            cursor.execute(query, values)
            self.rows = cursor.fetchall()


            if self.rows:
                messagebox.showinfo("Success", "Found")

                food_data = self.rows[0]  # Assuming you are fetching a single food

                # Update Entry widgets with the data from the database
                
                self.e2.delete(0, END)  # Clear the existing value
                self.e2.insert(0, food_data[1])  # Assuming the third column is rate
                
                self.e3.delete(0, END)  # Clear the existing value
                self.e3.insert(0, food_data[2])  # Assuming the third column is rate

                category_id = food_data[3]  # Assuming the fourth column is categoryid
                if category_id is not None:
                    cursor.execute("SELECT name FROM tbfoodcategory WHERE categoryid = %s", (category_id,))
                    category_row = cursor.fetchone()
               
                    category_name = category_row[0]  # Assuming category name is in the first column
                    self.food_category_combobox.set(category_name)
                else:
                    self.food_category_combobox.set("")


            else: 
                messagebox.showinfo("OOps", "Not Found")
 


                
            connection.commit()

        except Exception as e:
            print(f"Error: {e}")
            messagebox.showerror("Error", f"Error: {e}")
            return False
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()


        
        
        
       


def open_foodmenu_window():
    food_window= Tk()
    win_instance= staffMenu(food_window)
    food_window.mainloop()

def main():
    master =Tk()
    instance = staffMenu(master)
    master.mainloop()
if __name__ == '__main__':
    main()