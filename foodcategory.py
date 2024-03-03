from tkinter import *
from tkinter import messagebox,Toplevel
from PIL import Image,ImageTk
import mysql.connector
class foodcategory():
    def __init__(self,master):
        self.master = master
        self.master.geometry('600x400')
        self.master.title('Food Category')
        self.master.resizable(False, False)

        self.host ="localhost"
        self.port ='3306'
        self.database='canteen_database1'
        self.user='root'
        self.password=''

        self.bg_image=ImageTk.PhotoImage(Image.open("foodcat.jpg"))
        label_img = Label(self.master,image=self.bg_image)
        label_img.pack()

        self.frame = Frame(self.master, bd=0, highlightthickness=0, width=250, height=300)
        self.frame.place(relx=0.5, rely=0.5, anchor=CENTER)  # Center the frame

        # Add widgets or elements inside the transparent frame
        label =Label(self.frame, text="Food Category", font=("Helvetica", 16))
        label.place(x=2,y=3)
        
        


        #assigning variable for food table
        self.categoryname =StringVar()
    

        label_id = Label(self.frame, text="Enter Food Id OR Food Name")
        label_id.place(x=2,y=131)
        self.searchid= StringVar()
        entry_search = Entry(self.frame, width=20,textvariable=self.searchid)
        entry_search.place(x=2,y=162)

        search_button = Button(self.frame, text="Search",command=self.search_foods)
        search_button.place(x=140,y=158)

        register_button = Button(self.frame, text="Add",command=self.add_food)  # Add a command to register new foods
        register_button.place(x=90,y=99)

        update_button = Button(self.frame, text="Update",command=self.update_food)
        update_button.place(x=10,y=198)

        delete_button = Button(self.frame, text="Delete", command=self.delete_food)  # Add a command to delete foods
        delete_button.place(x=80,y=198)

        

        


        self.label_cname= Label(self.frame, text="Category Name")
        self.label_cname.place(x=2,y=67)
        self.e2= Entry(self.frame, width=25,textvariable=self.categoryname)
        self.e2.place(x=90,y=67)

        

       
        

    
    #add new food to DB
    def add_food(self):
        name= (self.categoryname.get())
        
        try:
            connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database,
            )
            cursor = connection.cursor()
            

            query ="INSERT INTO tbfoodcategory(name) VALUES (%s)"
            values =(name,)
            cursor.execute(query,values)
            connection.commit()
            messagebox.showinfo("Success","food registered Successfully")
        except Exception as e:
            print(f"Error: {e}")
            messagebox.showerror("Error", f"Error: {e}")
            return False
        # finally:
            
        #     self.cursor.close()
        #     connection.close()
    #edit food
    def update_food(self):
        c_id =self.searchid.get()
        name= self.categoryname.get()
        
        try:
            connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database,
            )
            cursor = connection.cursor()
            
            query ="UPDATE tbfoodcategory SET name=%s where itemid=%s "
            values =(name,c_id,)

            cursor.execute(query, values)
            connection.commit()
            messagebox.showinfo("Success", "food details updated successfully!")

        except Exception as e:
            print(f"Error: {e}")
            messagebox.showerror("Error", f"Error: {e}")
            return False
        # finally:
        #     if connection.is_connected():
        #         self.cursor.close()
        #         connection.close()
    #deleting the food
    def delete_food(self):
        c_id =self.searchid.get()

        try:
            connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database,
            )
            cursor = connection.cursor()
            
            

            query = "DELETE FROM tbfoodcategory WHERE categoryid=%s"
            values = (c_id,)

            cursor.execute(query, values)
            connection.commit()
            messagebox.showinfo("Success", "food deleted successfully!")
            self.e1.delete(0, END)
            self.e2.delete(0, END)
           


        except Exception as e:
            print(f"Error: {e}")
            messagebox.showerror("Error", f"Error: {e}")
            return False
        # finally:
        #     if connection.is_connected():
        #         self.cursor.close()
        #         connection.close()
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


            query = "SELECT * FROM tbfoodcategory WHERE  LOWER(name)= LOWER(%s)"
            values = (c_id,)
            cursor.execute(query, values)
            self.rows = cursor.fetchall()


            if self.rows:
                messagebox.showinfo("Success", "Found")

                food_data = self.rows[0]  # Assuming you are fetching a single food

                # Update Entry widgets with the data from the database
                
                self.e2.delete(0, END)  # Clear the existing value
                self.e2.insert(0, food_data[1])  # Assuming the third column is rate
                
               
               


            else: 
                messagebox.showinfo("OOps", "Not Found")
 


                
            connection.commit()

        except Exception as e:
            print(f"Error: {e}")
            messagebox.showerror("Error", f"Error: {e}")
            return False
        # finally:
        #     if connection.is_connected():
        #         self.cursor.close()
        #         connection.close()


        
        
        
       


def open_foodcategory_window():
    food_window= Tk()
    win_instance= foodcategory(food_window)
    food_window.mainloop()
      

   
def open_main():
    master = Tk()
    object_name = foodcategory(master)
    master.mainloop()
if __name__ == "__main__":
    open_main()