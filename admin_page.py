import tkinter as tk
from tkinter import ttk
import sqlite3
from rza_website import ZooApp


class AdminPage:
    def __init__(self, master):
        self.master = master

        # Attractions
        self.attractions_label = tk.Label(master, text="Attractions:", font=("Arial", 16))
        self.attractions_label.pack(pady=10)

        self.attractions = ttk.Treeview(master, columns=('id', 'name', 'species'), show='headings')
        self.attractions.heading('id', text='ID')
        self.attractions.heading('name', text='Name')
        self.attractions.heading('species', text='Species')
        self.attractions.pack()

        # Add attraction
        self.add_attraction_name = tk.Entry(master)
        self.add_attraction_name.pack()
        self.add_attraction_species = tk.Entry(master)
        self.add_attraction_species.pack()
        self.add_attraction_button = tk.Button(master, text="Add Attraction", command=self.add_attraction)
        self.add_attraction_button.pack(pady=10)

        # Facilities
        self.facilities_label = tk.Label(master, text="Facilities:", font=("Arial", 16))
        self.facilities_label.pack(pady=10)

        self.facilities = ttk.Treeview(master, columns=('id', 'name', 'description'), show='headings')
        self.facilities.heading('id', text='ID')
        self.facilities.heading('name', text='Name')
        self.facilities.heading('description', text='Description')
        self.facilities.pack()

        # Add facility
        self.add_facility_name = tk.Entry(master)
        self.add_facility_name.pack()
        self.add_facility_description = tk.Entry(master)
        self.add_facility_description.pack()
        self.add_facility_button = tk.Button(master, text="Add Facility", command=self.add_facility)
        self.add_facility_button.pack(pady=10)
         # Delete attraction button
        self.delete_attraction_button = tk.Button(master, text="Delete Attraction", command=self.delete_attraction)
        self.delete_attraction_button.pack(pady=10)

        # Delete facility button
        class AdminPage:
            def __init__(self, master):
                self.master = master
                self.controller = None  # Define the controller variable

                # ...

                button = tk.Button(self, text="Go to RZA Website",
                                   command=lambda: self.controller.show_frame(ZooApp))  # Use self.controller instead of controller
                button.pack()
    def add_attraction(self):
        name = self.add_attraction_name.get()
        species = self.add_attraction_species.get()
        conn = sqlite3.connect('attraction.db')
        c = conn.cursor()
        c.execute("INSERT INTO attractions (name, species) VALUES (?, ?)", (name, species))
        conn.commit()
        conn.close()

        # Refresh the attractions treeview
        self.refresh()

    def add_facility(self):
        name = self.add_facility_name.get()
        description = self.add_facility_description.get()
        conn = sqlite3.connect('attraction.db')
        c = conn.cursor()
        c.execute("INSERT INTO facilities (name, description) VALUES (?, ?)", (name, description))
        conn.commit()
        conn.close()

        # Refresh the facilities treeview
        self.refresh()

    def delete_attraction(self):
        selected_item = self.attractions.selection()[0]  # get selected item
        id_to_delete = self.attractions.item(selected_item)['values'][0]
        conn = sqlite3.connect('zoo.db')
        c = conn.cursor()
        c.execute("DELETE FROM attractions WHERE id=?", (id_to_delete,))
        conn.commit()
        conn.close()

        # Refresh the attractions treeview
        self.refresh()

    def delete_facility(self):
        selected_item = self.facilities.selection()[0]  # get selected item
        id_to_delete = self.facilities.item(selected_item)['values'][0]
        conn = sqlite3.connect('zoo.db')
        c = conn.cursor()
        c.execute("DELETE FROM facilities WHERE id=?", (id_to_delete,))
        conn.commit()
        conn.close()

        # Refresh the facilities treeview
        self.refresh()

    def refresh(self):
        # Clear the treeviews
        for i in self.attractions.get_children():
            self.attractions.delete(i)
        for i in self.facilities.get_children():
            self.facilities.delete(i)

        # Fetch data from the database and add it to the treeviews
        conn = sqlite3.connect('attraction.db')
        c = conn.cursor()
        c.execute("SELECT id, name, species FROM attractions")
        for row in c.fetchall():
            self.attractions.insert('', 'end', values=row)
        c.execute("SELECT id, name, description FROM facilities")
        for row in c.fetchall():
            self.facilities.insert('', 'end', values=row)
        conn.close()

root = tk.Tk()
admin_page = AdminPage(root)
root.mainloop()