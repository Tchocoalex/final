import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sqlite3
import re
from PIL import ImageTk , Image
import importlib





    
class BookingInfoPage:
    def __init__(self, master, email):
        self.master = master
        self.master.title("Booking Information")

        self.email_label = tk.Label(self.master, text=f"Email: {email}")
        self.email_label.pack(pady=5)

        # Fetch booking information from the database using the email
        conn = sqlite3.connect('zoo_app.db')
        c = conn.cursor()
        c.execute("SELECT * FROM bookings WHERE email=?", (email,))
        booking_info = c.fetchone()
        conn.close()

        if booking_info:
            self.booking_info_label = tk.Label(self.master, text=str(booking_info))
            self.booking_info_label.pack(pady=5)
        else:
            self.booking_info_label = tk.Label(self.master, text="No bookings found.")
            self.booking_info_label.pack(pady=5)

class ZooApp:
    def __init__(self, master):
        self.master = master
        master.title("RZA Website")
        master.geometry("1300x1300")
        master.configure(background='#ffcc66')
        master.resizable(width=False, height=False)
       
        
        
        # Create a frame for the header
        self.header_frame = tk.Frame(master, bg="#333")
        self.header_frame.pack(fill=tk.X)

        # Create header label
        self.header_label = tk.Label(self.header_frame, text="Welcome to Ridget Zoo Adventure ", fg="white", bg="#333", font=("Helvetica", 20))
        self.header_label.pack(pady=10)
        self.main_frame = tk.Frame(master)
        self.main_frame.label= tk.Label(self.main_frame, text="Welcome to the Zoo App", font=("Arial", 24))
        
        self.main_frame.pack()
       
        self.animals_button = tk.Button(self.main_frame, text="Animals", command=self.show_animals)
        self.animals_button.pack(side="left")

        self.tickets_button = tk.Button(self.main_frame, text="Tickets", command=self.show_tickets)
        self.tickets_button.pack(side="left")

        self.contact_button = tk.Button(self.main_frame, text="Contact", command=self.show_contact)
        self.contact_button.pack(side="left")

        self.login_button = tk.Button(self.main_frame, text="Login", command=self.show_login)
        self.login_button.pack(side="left")

        self.hotel_button = tk.Button(self.main_frame, text="Hotel", command=self.show_hotel)
        self.hotel_button.pack(side="left")

        self.logout_button = tk.Button(master, text="Logout", command=self.logout)
        self.logout_button.pack()

        self.facilities_button = tk.Button(self.main_frame, text="Facilities and attractions", command=self.show_facilities) 
        self.facilities_button.pack(side="left")

        # self.hotel_booking_form = HotelBookingForm(master)
        # self.client_form_page = ClientFormPage(master, self.hotel_booking_form)
        # self.client_form_page.tree.pack_forget()  # Hide the client form page initially


        
        # Load the image
        image = Image.open("images/girafe.jpg")

         # Resize the image to fit the size of the page
        image = image.resize((800, 800), Image.LANCZOS)  # Replace (800, 600) with the size of your page

         # Convert the image to a Tkinter-compatible photo image
        self.image = ImageTk.PhotoImage(image)
        
        # Create an outer frame that expands to fill the window
        outer_frame = tk.Frame(master)
        outer_frame.pack(expand=True)

        # Create an inner frame that doesn't expand
        inner_frame = tk.Frame(outer_frame)
        inner_frame.pack()

        # Create a label with the image and add it to the inner frame
        self.image_label = tk.Label(inner_frame, image=self.image)
        self.image_label.pack()

        


        # self.page_frame = tk.Frame(master)
        # self.page_frame.pack()

        # self.page_label = tk.Label(self.page_frame, text="Welcome to the Ridget Zoo Adventure!")
        # self.page_label.pack()

    
    def show_animals(self):
        self.master.destroy()
        root = tk.Tk()
        animal_module = importlib.import_module('animal_page')  # Import the animal page module
        app = animal_module.AnimalPage(root,self)  # open the animal page
        root.mainloop()
        
    def show_facilities(self):
        self.master.destroy()
        root = tk.Tk()
        facilities_module = importlib.import_module('facilities_page')
        app = facilities_module.ZooInfoPage(root) # open the facilities page 
        root.mainloop() 

    def show_tickets(self):
        # self.page_label.config(text="Welcome to the Tickets page!")
        self.master.destroy()
        ticket_module = importlib.import_module('ticket')  # Import the ticket module
        root = tk.Tk()
        app = ticket_module.ZooTicketBookingApp(root)
        root.mainloop()

    def show_contact(self):
        self.master.destroy()
        contact_module = importlib.import_module("contact_page")
        root = tk.Tk()
        app = contact_module.ContactPage(root)
        root.mainloop()
        

    def show_login(self):
        self.master.destroy()  # Close the main window
        root = tk.Tk()  # create a new root window
        login_module = importlib.import_module('login')  # Import the login module
        app = login_module.LoginPage(root)  # open the login page
        root.mainloop()

    def show_hotel(self):
        self.master.destroy()  # Close the main window
        root = tk.Tk()  # create a new root window
        hotel_module = importlib.import_module('hotel_booking')
        app = hotel_module.HotelBookingForm(root)  # open the hotel booking form page
        root.mainloop()
    
    def logout(self):
        self.master.destroy()  # close the home page window
        root = tk.Tk()  # create a new root window
        app = ZooApp(root)  # open the logout page
        root.mainloop()

    def show_sign_up(self):
        self.master.destroy()
        app = SignInPage(root)
        root = tk.Tk()
    
    def show(self):
        # Show the home page
        self.label.pack()
        self.button.pack()
        
root = tk.Tk()
app = ZooApp(root)
root.mainloop()