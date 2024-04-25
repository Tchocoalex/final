import tkinter as tk
import sqlite3
from PIL import ImageTk, Image

class ContactPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.master = master
        self.master.title("Contact")
        self.master.geometry("1300x1300")
        self.master.configure(background='#ffcc66')


        self.title_label = tk.Label(self, text="Contact Us", font=("Arial", 24), bg='tan')
        self.title_label.pack(pady=10)

        self.name_label = tk.Label(self, text="Name", bg='tan')
        self.name_label.pack()
        self.name_entry = tk.Entry(self)
        self.name_entry.pack()

        self.email_label = tk.Label(self, text="Email", bg='tan')
        self.email_label.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack()

        self.message_label = tk.Label(self, text="Message", bg='tan')
        self.message_label.pack()
        self.message_text = tk.Text(self, width=50, height=10)
        self.message_text.pack()

        self.submit_button = tk.Button(self, text="Submit", command=self.submit_message)
        self.submit_button.pack()
        image = Image.open("images/zoo activities.jpg")

         # Resize the image to fit the size of the page
        image = image.resize((600, 400), Image.LANCZOS)  # Replace (800, 600) with the size of your page

         # Convert the image to a Tkinter-compatible photo image
        self.image = ImageTk.PhotoImage(image)
        
        # Create a label with the image
        self.image_label = tk.Label(self.master, image=self.image)
        self.image_label.pack()


        self.page_frame = tk.Frame(self.master)
        self.page_frame.pack()

        self.page_label = tk.Label(self.page_frame, text="Fun day at the Zoo")
        self.page_label.pack()
    def submit_message(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        message = self.message_text.get("1.0", 'end-1c')

        # Connect to the database (or create it if it doesn't exist)
        conn = sqlite3.connect('contact_messages.db')

        # Create a cursor
        c = conn.cursor()

        # Create the table if it doesn't exist
        c.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                name TEXT,
                email TEXT,
                message TEXT
            )
        """)

        # Insert the message into the table
        c.execute("INSERT INTO messages VALUES (?, ?, ?)", (name, email, message))

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

        print(f"Name: {name}\nEmail: {email}\nMessage: {message}")

root = tk.Tk()
contact_page = ContactPage(root)
contact_page.pack()
root.mainloop()