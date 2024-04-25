import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox 

class CustomerInfoPage:
    def __init__(self, master):
        self.master = master
        master.title("Customer Information")
        master.geometry("900x900")

         # Connect to the SQLite database
        self.conn = sqlite3.connect('bookings.db')
        self.cursor = self.conn.cursor()
      

       
       
    def display_customer_info(self):
        """Display the customer information for the selected booking."""
        selected_item = self.tree.selection()[0]
        booking_id = self.tree.item(selected_item)['values'][0]

        self.cursor.execute('SELECT * FROM bookings WHERE id = ?', (booking_id,))
        booking = self.cursor.fetchone()

        customer_info_window = tk.Toplevel(self.master)
        customer_info_window.title("Customer Information")

        self.name_entry = tk.Entry(customer_info_window)
        self.name_entry.insert(0, booking[1])
        self.name_entry.pack()

        self.email_entry = tk.Entry(customer_info_window)
        self.email_entry.insert(0, booking[2])
        self.email_entry.pack()

        self.check_in_date_entry = tk.Entry(customer_info_window)
        self.check_in_date_entry.insert(0, booking[3])
        self.check_in_date_entry.pack()

        self.check_out_date_entry = tk.Entry(customer_info_window)
        self.check_out_date_entry.insert(0, booking[4])
        self.check_out_date_entry.pack()

        self.room_type_entry = tk.Entry(customer_info_window)
        self.room_type_entry.insert(0, booking[5])
        self.room_type_entry.pack()


    def display_bookings(self):
        """Display all bookings inthe main window."""
        self.cursor.execute('SELECT * FROM bookings')
        bookings = self.cursor.fetchall()

        self.info_label = tk.Label(self.master)
        self.info_label.pack()

        if not bookings:
            messagebox.showinfo("Info", "No bookings")
            return


        self.tree = ttk.Treeview(self.master, columns=('id', 'name', 'email', 'check_in_date', 'check_out_date', 'room_type'), show='headings')
        self.tree.heading('id', text='ID')
        self.tree.heading('name', text='Name')
        self.tree.heading('email', text='Email')
        self.tree.heading('check_in_date', text='Check-in Date')
        self.tree.heading('check_out_date', text='Check-out Date')
        self.tree.heading('room_type', text='Room Type')

        for booking in bookings:
            self.tree.insert('', 'end', values=booking)

        self.display_customer_info_button = tk.Button(self.master, text="Display Customer Info", command=self.display_customer_info)
        self.display_customer_info_button.pack(pady=10)

        self.tree.pack()

    def close(self):
        self.conn.close()
        self.master.destroy()

# Usage
root = tk.Tk()
page = CustomerInfoPage(root)
page.display_bookings()
root.mainloop()
page.close()

# def get_booking_info(customer_id):
#     # Fetch booking information from the database based on the customer_id
#     # This is just a placeholder. Replace it with your actual database query.
#     return {
#         'booking_id': '123',
#         'booking_date': '2022-01-01',
#         'booking_details': 'Details about the booking...'
#     }

# def show_customer_info(customer_id):
#     booking_info = get_booking_info(customer_id)

#     window = tk.Tk()
#     window.title("Customer Info")

#     ttk.Label(window, text="Booking ID:").grid(column=0, row=0)
#     ttk.Label(window, text=booking_info['booking_id']).grid(column=1, row=0)

#     ttk.Label(window, text="Booking Date:").grid(column=0, row=1)
#     ttk.Label(window, text=booking_info['booking_date']).grid(column=1, row=1)

#     ttk.Label(window, text="Booking Details:").grid(column=0, row=2)
#     ttk.Label(window, text=booking_info['booking_details']).grid(column=1, row=2)

#     window.mainloop()

# # Test the function with a customer_id
# show_customer_info(1)