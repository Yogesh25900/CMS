from tkinter import *
import os 
from tkinter import messagebox,Toplevel
from PIL import Image,ImageTk
import mysql.connector
class feedback:
    def __init__(self,master,**kwargs):
        self.master = master
        self.master.geometry('560x360+0+2')
        self.master.resizable(False,False)
        self.master.title('Customer Feedback Dashboard')
        org =Image.open("feedback.jpg")
        resize = org.resize((560,360))
        self.bg_image=ImageTk.PhotoImage(resize)


        label_img = Label(self.master,image=self.bg_image)
        label_img.pack()
        
        self.frame = LabelFrame(self.master,text="Feedback",bd=7,relief=GROOVE,font=("Helvetica", 16, "bold"))
        self.frame.place(x=50,y=60)

        self.gettitle =StringVar()
        self.getcustomerid =StringVar()

        # Label and entry for Customer ID
        label_id = Label(self.frame, text="Enter your username:",font=("Helvetica", 12, "bold"))
        label_id.grid(row=0, column=0, padx=5, pady=5)

        entry_id = Entry(self.frame, width=30,font=("Helvetica", 12),textvariable=self.getcustomerid)
        entry_id.grid(row=0, column=1, padx=5, pady=5)

        # Label and entry for Title
        label_title = Label(self.frame, text="Title:",font=("Helvetica", 12, "bold"))
        label_title.grid(row=1, column=0, padx=5, pady=5)

        entry_title = Entry(self.frame, width=30, textvariable=self.gettitle,font=("Helvetica", 12))
        entry_title.grid(row=1, column=1, padx=5, pady=5)

        # Label and textbox for Feedback
        label_feedback = Label(self.frame, text="Feedback:",font=("Helvetica", 12, "bold"))
        label_feedback.grid(row=2, column=0, padx=5, pady=5)

        self.textbox_feedback = Text(self.frame, width=30, height=5,font=("Helvetica", 12))
        self.textbox_feedback.grid(row=2, column=1, padx=5, pady=5)

        # Submit button
        btn_submit = Button(self.frame, text="Submit Feedback", command=self.submit_feedback)
        btn_submit.grid(row=3, column=0, columnspan=2, pady=10)


    def submit_feedback(self):
        username_get= self.getcustomerid.get()
        title = self.gettitle.get()
        description = self.textbox_feedback.get("1.0", "end-1c")

        # Insert data into the table
        try:
            connection = mysql.connector.connect(
                host='localhost',
                port='3306',
                user='root',
                password='',
                database='canteen_database1',
            )
            cursor = connection.cursor()
            select_query =  "SELECT customerid from tbcustomer WHERE LOWER(username)  = LOWER(%s) "
            cursor.execute(select_query,(username_get,))
            fetch_id  =cursor.fetchone()
            query=("INSERT INTO tbfeedback (title, description,customerid) VALUES (%s,%s, %s)")
            values= (title,description,fetch_id[0])      
            cursor.execute(query,values)

            connection.commit()
            messagebox.showinfo("Success", "Feedback submitted successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error submitting feedback: {str(e)}")


        
       
def open_customerfeedback_window():
    feedback_window= Tk()
    win_instance=feedback(feedback_window)
    feedback_window.mainloop()


        
 

def open_main():
    master = Tk()
    object_name = feedback(master)
    master.mainloop()
if __name__ == "__main__":
    open_main()