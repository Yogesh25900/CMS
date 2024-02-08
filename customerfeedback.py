from tkinter import *
import os 
from tkinter import messagebox,Toplevel
from PIL import Image,ImageTk
import mysql.connector
class feedback():
    def __init__(self,master):
        self.master = master
        self.master.geometry('1300x700+0+2')
        self.master.title('Customer Feedback Dashboard')
        
        self.frame = Frame(self.master,height=500,width=600,bd=7,relief=GROOVE)
        self.frame.pack()

        self.gettitle =StringVar()

        self.label = Label(self.frame,text="Feedback")
        self.label.pack()

        self.label1 = Label(self.frame,text="Title")
        self.label1.pack()

        self.entry = Entry(self.frame,width=30,textvariable=self.gettitle)
        self.entry.pack()

        self.textbox = Text(self.frame,width=30,height=5)
        self.textbox.pack()
        
       
        self.btn = Button(self.frame,text="Submit Feedback",command=self.submit_feedback)
        self.btn.pack()

    def submit_feedback(self):
        title = self.gettitle.get()
        description = self.textbox.get("1.0", "end-1c")

        # Insert data into the table
        try:
            connection = mysql.connector.connect(
                host='localhost',
                port='3306',
                user='master',
                password='',
                database='canteen_database1',
            )
            cursor = connection.cursor()
            query=("INSERT INTO tbfeedback (feedbackid,title, descrption) VALUES (%s,%s, %s)")
            values= ('1',title,description)      
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