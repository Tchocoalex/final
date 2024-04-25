

import tkinter as tk 
from tkinter import messagebox
import sqlite3
import re
from PIL import ImageTk , Image
from sign_up_page import SignUpPage
from tkinter import Canvas



class LoginPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Zoo App Login")
        self.master.geometry("1300x1300")
        self.master.configure(background='#ffcc66')
        


       
        # Load the image file
        img = Image.open("images/desert.jpg")  # Replace with your image file path

        # Resize the image
        img = img.resize((900, 900), Image.LANCZOS)  # Resize to match your window size

        # Convert the image to a Tkinter-compatible photo image
        bg = ImageTk.PhotoImage(img)

        # Create a label with the image and add it to the window
        bg_label = tk.Label(master, image=bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Keep a reference to the image to prevent it from being garbage collected
        bg_label.image = bg

        
        
        def clear_placeholder(event):
            event.widget.delete(0, 'end')
        self.username_label = tk.Label(master, text="Email:")
        self.username_label.pack(pady=5)

        self.username_entry = tk.Entry(master)
        self.username_entry.insert(0, "Enter your email")
        self.username_entry.bind('<FocusIn>', clear_placeholder)

        self.username_entry.pack(pady=5)

        self.password_label = tk.Label(master, text="Password:")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.pack(pady=5)

        self.login_button = tk.Button(master, text="Login", command=self.login)
        self.login_button.pack(pady=10)

        self.sign_in_button = tk.Button(master, text="Sign In", command=self.show_sign_up)
        self.sign_in_button.pack(pady=10)

         # Load the image
        image = Image.open("images/desert.jpg")

         # Resize the image to fit the size of the page
        image = image.resize((800, 600), Image.ANTIALIAS)  # Replace (800, 600) with the size of your page

         # Convert the image to a Tkinter-compatible photo image
        self.image = ImageTk.PhotoImage(image)
        
        # Create a label with the image
        self.image_label = tk.Label(master, image=self.image)
        self.image_label.pack()


        self.page_frame = tk.Frame(master)
        self.page_frame.pack()

        self.page_label = tk.Label(self.page_frame, text="")
        self.page_label.pack()
   
    
    def login(self):
        try:
            email = self.username_entry.get()
            password = self.password_entry.get()

            def is_valid_email(email):
                return re.match(r"[^@]+@[^@]+\.[^@]+", email)
            if not is_valid_email(email):
                messagebox.showerror("Error", "Invalid email address")

            conn = sqlite3.connect('zoo_app.db')
            c = conn.cursor()

            # Query the database
            c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
            result = c.fetchone()

            # Close the connection
            conn.close()

            if result:
                messagebox.showinfo("Success", "Login successful!")
                self.master.destroy()
                root = tk.Tk()
                from customer_info import CustomerInfoPage
                app = CustomerInfoPage(root)
                root.mainloop()  # Close the login window
            else:
                messagebox.showerror("Login Failed", "Invalid username or password")
        except Exception as e:
            messagebox.showerror("Error", f"An error occured: {e}")
            
    def show_sign_up(self):
        self.master.destroy()  # Close the login window
        root = tk.Tk()  # create a new root window
        app = SignUpPage(root)  # open the sign-in page
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    LoginPage(root)
    root.mainloop()