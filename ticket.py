
import tkinter as tk 
from tkinter import messagebox
import sqlite3
from PIL import ImageTk, Image

class ZooTicketBookingApp:
    def __init__(self, master):
        self.master = master
        master.title("Zoo Ticket Booking System")
        master.geometry("900x900")
        master.configure(background='#ffcc66')

       
        # Create a database connection and cursor
        self.conn = sqlite3.connect("zoo_tickets.db")
        self.cursor = self.conn.cursor()

        # Create a table if it doesn't exist
        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS bookings 
               (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, ticket_type TEXT, quantity INTEGER)'''
        )
        self.conn.commit()

        # Create a frame for the header
        self.header_frame = tk.Frame(master, bg="#333")
        self.header_frame.pack(fill=tk.X)

        # Create header label
        self.header_label = tk.Label(self.header_frame, text="Zoo Ticket Booking System", fg="white", bg="#333", font=("Helvetica", 20))
        self.header_label.pack(pady=10)

        # Create a frame for the content
        self.content_frame = tk.Frame(master)
        self.content_frame.pack(pady=20)

        # Create labels and entry widgets for ticket booking
        self.name_label = tk.Label(self.content_frame, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.name_entry = tk.Entry(self.content_frame)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.ticket_type_label = tk.Label(self.content_frame, text="Ticket Type:")
        self.ticket_type_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.ticket_type_var = tk.StringVar()
        self.ticket_type_var.set("Adult")  # Default ticket type
        self.ticket_type_optionmenu = tk.OptionMenu(self.content_frame, self.ticket_type_var, "Adult", "Child", "Senior")
        self.ticket_type_optionmenu.grid(row=1, column=1, padx=10, pady=5)

        self.quantity_label = tk.Label(self.content_frame, text="Quantity:")
        self.quantity_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.quantity_spinbox = tk.Spinbox(self.content_frame, from_=1, to=10)
        self.quantity_spinbox.grid(row=2, column=1, padx=10, pady=5)

        # Create a button to book tickets
        self.book_button = tk.Button(self.content_frame, text="Book Tickets", command=self.book_tickets)
        self.book_button.grid(row=3, columnspan=2, pady=10)

        image = Image.open("images/jungle.jpg")

         # Resize the image to fit the size of the page
        image = image.resize((600, 400), Image.ANTIALIAS)  # Replace (800, 600) with the size of your page

         # Convert the image to a Tkinter-compatible photo image
        self.image = ImageTk.PhotoImage(image)
        
        # Create a label with the image
        self.image_label = tk.Label(self.master, image=self.image)
        self.image_label.pack()


        self.page_frame = tk.Frame(self.master)
        self.page_frame.pack()

        self.page_label = tk.Label(self.page_frame, text="suite")
        self.page_label.pack()
        # Create a frame for the footer
        self.footer_frame = tk.Frame(master, bg="#333")
        self.footer_frame.pack(fill=tk.X, side=tk.BOTTOM)

        # Create footer label
        self.footer_label = tk.Label(self.footer_frame, text="© 2023 Zoo Ticket Booking System", fg="white", bg="#333")
        self.footer_label.pack(pady=10)

    def book_tickets(self):
        name = self.name_entry.get()
        ticket_type = self.ticket_type_var.get()
        quantity = int(self.quantity_spinbox.get())

        if name and quantity > 0:
            # Insert the booking into the database
            self.cursor.execute("INSERT INTO bookings (name, ticket_type, quantity) VALUES (?, ?, ?)",
                                (name, ticket_type, quantity))
            self.conn.commit()

            booking_message = f"Tickets booked for {name} ({quantity} {ticket_type} tickets)!"
            messagebox.showinfo("Booking Confirmation", booking_message)
        else:
            messagebox.showerror("Booking Error", "Please provide a valid name and quantity!")
root = tk.Tk()

# Create the sign up page
zoo_ticket= ZooTicketBookingApp(root)

# Start the Tkinter event loop
root.mainloop()  # ... other code ...