import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3
from tkinter import messagebox
from rza_website import ZooApp

class ZooInfoPage:
    def __init__(self, master):
        self.master = master
        master.title("Facilities and attarctions")
        master.geometry("1300x1300")
        master.configure(background='#ffcc66')
        self.message_label = tk.Label(master, text="Facilities and attractions informations!", font=("Arial", 20), bg='light blue', fg='black', width=50, height=2)
        self.message_label.pack(pady=10)


        
        # Load the map image
        img = Image.open("images\safari map.jpeg")
        photo_img = ImageTk.PhotoImage(img)

        # Create a canvas for the map
        self.map_canvas = tk.Canvas(master, width=img.width, height=img.height)
        self.map_canvas.create_image(0, 0, image=photo_img, anchor='nw')
        self.map_canvas.image = photo_img  # Keep a reference to the image
        self.map_canvas.pack(pady=10)
        

        # Attractions
        self.attractions_label = tk.Label(master, text="Attractions:", font=("Arial", 16))
        self.attractions_label.pack(pady=10)

        self.attractions = ttk.Treeview(master, columns=('name', 'species'), show='headings')
        self.attractions.heading('name', text='Name')
        self.attractions.heading('species', text='Species')
        self.attractions.pack()

        # # Add some attractions
        # self.attractions.insert('', 'end', values=("Lion's Den", "Lion"))
        # self.attractions.insert('', 'end', values=("Elephant Ride", "Elephant"))

        # Facilities
        self.facilities_label = tk.Label(master, text="Facilities:", font=("Arial", 16))
        self.facilities_label.pack(pady=10)

        self.facilities = ttk.Treeview(master, columns=('name', 'description'), show='headings')
        self.facilities.heading('name', text='Name')
        self.facilities.heading('description', text='Description')
        self.facilities.pack()

        self.details_button = tk.Button(master, text="Show Details", command=self.show_details)
        self.details_button.pack(pady=10)


        # Add some facilities
        self.facilities.insert('', 'end', values=("Cafeteria", "Food and drinks"))
        self.facilities.insert('', 'end', values=("Gift Shop", "Souvenirs and gifts"))
        # Fetch attractions from the database and add them to the treeview
        conn = sqlite3.connect('attraction.db')
        c = conn.cursor()
        c.execute("SELECT name, species FROM attractions")
        for row in c.fetchall():
            self.attractions.insert('', 'end', values=row)
        conn.close()

          # Create a back button
        self.back_button = tk.Button(master, text="Back to Main Page", command=self.go_back)
        self.back_button.pack(pady=10)


    def go_back(self):
        # Destroy the current window
        self.master.destroy()

        # Create a new instance of the main page
        main_page = ZooApp(tk.Tk())
       

    def add_marker(self, x, y, text):
        marker = self.map.create_oval(x-5, y-5, x+5, y+5, fill="red")
        marker_radius = 10
        marker_color = 'light blue'
        marker_outline_color = 'green'

        marker = self.map_canvas.create_oval(
            x - marker_radius, 
            y - marker_radius, 
            x + marker_radius, 
            y + marker_radius, 
            fill=marker_color, 
            outline=marker_outline_color
        )

        # Add a binding for the <Button-1> event (left mouse button click)
        self.map_canvas.tag_bind(marker, "<Button-1>", lambda e: self.show_marker_details(text))

    def show_marker_details(self, attraction_name):
        # Show a messagebox with the marker's text
        messagebox.showinfo("Marker", attraction_name)

        # Create a new window
        details_window = tk.Toplevel(self.master)
        details_window.title("Attraction Details")
        details_window.geometry("300x200")

        # Fetch the details about the specific attraction from the database
        conn = sqlite3.connect('attraction.db')
        c = conn.cursor()

        # Use the attraction name to fetch details about the attraction
        c.execute("SELECT * FROM attractions WHERE name = ?", (attraction_name,))

        # Fetch the first row of the results
        row = c.fetchone()

        if row is not None:
            # Display the details in the new window
            details_label = tk.Label(details_window, text=f"Name: {row[0]}\nSpecies: {row[1]}")
            details_label.pack(pady=10)
        else:
            # Display a message saying that no details were found
            details_label = tk.Label(details_window, text="No details found.")
            details_label.pack(pady=10)

        conn.close()

    def show_details(self):
        # Get the selected item from the attractions Treeview
        selected_item = self.attractions.selection()

        # Check if an item is selected
        if selected_item:
            # Get the item's values
            item_values = self.attractions.item(selected_item, 'values')

            # Create a new window
            details_window = tk.Toplevel(self.master)
            details_window.title("Attraction Details")
            details_window.geometry("300x200")

            # Fetch the details about the specific attraction from the database
            conn = sqlite3.connect('attraction.db')
            c = conn.cursor()

            # Use the first value (name) to fetch details about the attraction
            c.execute("SELECT * FROM attractions WHERE name = ?", (item_values[0],))

            # Fetch the first row of the results
            row = c.fetchone()

            if row is not None:
                # Display the details in the new window
                details_label = tk.Label(details_window, text=f"Name: {row[0]}\nSpecies: {row[1]}")
                details_label.pack(pady=10)
            else:
                # Display a message saying that no details were found
                details_label = tk.Label(details_window, text="No details found.")
                details_label.pack(pady=10)

            conn.close()
        else:
            messagebox.showinfo("No Selection", "Please select an attraction to show details.")


if __name__ == "__main__":
    root = tk.Tk()
    ZooInfoPage(root)
    # main_page = ZooApp(root)
    root.mainloop()