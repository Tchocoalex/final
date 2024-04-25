import tkinter as tk 
from tkinter import messagebox
import sqlite3
import re
from PIL import ImageTk , Image
import re



class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

class SignUpPage:
    def __init__(self, master):
        self.master = master
        self.create_gui()

    def create_gui(self):
        self.master.title("Zoo App Sign Up")
        self.master.geometry("800x600")
        # Load the image file
        img = Image.open("images/jungle.jpg")  # Replace with your image file path

        # Resize the image
        img = img.resize((900, 900), Image.LANCZOS)  # Resize to match your window size

        # Convert the image to a Tkinter-compatible photo image
        bg = ImageTk.PhotoImage(img)

        # Create a label with the image and add it to the window
        bg_label = tk.Label(self.master, image=bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Keep a reference to the image to prevent it from being garbage collected
        bg_label.image = bg

        self.name_label = tk.Label(self.master, text="Name:")
        self.name_label.pack(pady=5)
        self.name_entry = tk.Entry(self.master)
        self.name_entry.pack(pady=5)

        self.username_label = tk.Label(self.master, text="Email:")
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(self.master)
        self.username_entry.pack(pady=5)

        self.password_label = tk.Label(self.master, text="Password:")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.pack(pady=5)

        self.confirm_password_label = tk.Label(self.master, text="Confirm Password:")
        self.confirm_password_label.pack(pady=5)
        self.confirm_password_entry = tk.Entry(self.master, show="*")
        self.confirm_password_entry.pack(pady=5)

        self.sign_up_button = tk.Button(self.master, text="Sign Up", command=self.sign_up)
        self.sign_up_button.pack(pady=10)

    def sign_up(self):
        name = self.name_entry.get()
        email = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        # Validate the name
        if not name:
            messagebox.showerror("Sign Up Failed", "Name cannot be empty")
            return
        
        # Validate the email
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror("Sign Up Failed", "Invalid email")
            return

        # Validate the password
        if len(password) < 8 or not re.search(r"\d", password):
            messagebox.showerror("Sign Up Failed", "Password must be at least 8 characters long and contain a number")
            return

        # Check if the password and confirm password match
        if password != confirm_password:
            messagebox.showerror("Sign Up Failed", "Passwords do not match")
            return


        # Create a new User instance
        user = User(name, email, password)

        # Perform sign-up logic here
        conn = sqlite3.connect('zoo_app.db')
        c = conn.cursor()

        # Create table if it doesn't exist
        c.execute('''CREATE TABLE IF NOT EXISTS users
                     (name text, email text, password text)''')

        # Insert a row of data
        c.execute("INSERT INTO users VALUES (?,?,?)",(user.name, user.email, user.password))


        # Save (commit) the changes
        conn.commit()

        # Close the connection
        conn.close()

        messagebox.showinfo("Sign Up Successful", "Account created successfully")
        # Open the account info page
        self.master.destroy()  # Close the current window
        root = tk.Tk()
        AccountInfoPage(root, email)
        root.mainloop()

class AccountInfoPage:
    def __init__(self, master, email):
        self.master = master
        self.email = email
        self.create_gui()

    def create_gui(self):
        self.master.title("Account Info")
        self.master.geometry("400x200")

        self.email_label = tk.Label(self.master, text="Email:")
        self.email_label.pack(pady=5)

        self.email_value_label = tk.Label(self.master, text=self.email)
        self.email_value_label.pack(pady=5)

        # self.change_password_button = tk.Button(self.master, text="Change Password", command=self.change_password)
        # self.change_password_button.pack(pady=10)

   


if __name__ == "__main__":
    root = tk.Tk()
    SignUpPage(root)
    root.mainloop()
