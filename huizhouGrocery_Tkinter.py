import tkinter as tk
import sqlite3
from tkinter import filedialog, messagebox

import ttkbootstrap as ttk 

import datetime

currentDateTime = datetime.datetime.today()


def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData


class DatabaseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SQLite Database Huizhou Grocery")
        self.root.geometry("900x600")

        # Create a database or connect to an existing one
        self.conn = sqlite3.connect(r"Your database working directory\test.db")
        self.cursor = self.conn.cursor()

        # Create a table if it doesn't exist
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS new_order (id INTEGER PRIMARY KEY, date TEXT,image BLOB, time TEXT)''')
        self.conn.commit()

        # Create GUI elements
        self.date_label = ttk.Label(root, text="Date:")
        self.date_label.pack()
        self.date_label.place(x=250, y=155, width=60, height=40)

        self.date_entry = ttk.Entry(root)
        self.date_entry.pack()
        self.date_entry.place(x=350, y=155, width=200, height=30)

        self.image_label = ttk.Label(root, text="Image:")
        self.image_label.pack()
        self.image_label.place(x=250, y=205, width=60, height=40)


      # Add button

        self.add_button = ttk.Button(root, text="Upload", command=self.add_date)
        self.add_button.pack(pady = 10)
        self.add_button.place(x=350, y=205, width=100, height=40)


    def add_date(self):
        date = self.date_entry.get()
        image = convertToBinaryData(filedialog.askopenfilename())
        time = currentDateTime
     
        if date:
            self.cursor.execute("INSERT INTO new_order (date,image,time) VALUES (?,?,?)", (date,image,time))
         
            self.conn.commit()

            messagebox.showinfo("showinfo", "You have inserted data") 
    
            
        else:
            messagebox.showwarning("Warning", "Please input a date.")


if __name__ == "__main__":
 
    root = tk.Tk()
    app = DatabaseApp(root)
    root.mainloop()
