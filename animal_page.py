import tkinter as tk
from tkinter import ttk
import sqlite3
import re
import importlib
from PIL import ImageTk, Image

class AnimalPage:
    def __init__(self, master,ZooApp):
        self.master = master
        self.master.geometry("900x900")
        
        self.master.configure(background='#ffcc66')
        # Open the logo image file
        # Load the logo
        logo = Image.open("images/zoo activities.jpg")  # Replace "logo.png" with the path to your logo image file

        # Resize the logo
        logo = logo.resize((300, 300), Image.LANCZOS)  # Replace (100, 100) with the size you want

        # Convert the logo to a Tkinter-compatible photo image
        tk_logo = ImageTk.PhotoImage(logo)

        # Create a label and add the photo image to it
        logo_label = tk.Label(master, image=tk_logo)
        logo_label.image = tk_logo  # Keep a reference to the image
        logo_label.pack()

        master.title("Zoo App Animal Page")

        # Connect to the SQLite database
        conn = sqlite3.connect('zooAnimals.db')
        cursor = conn.cursor()

        # Execute a query to fetch all animals
        cursor.execute("SELECT id, name FROM animals")
        rows = cursor.fetchall()

        # Close the database connection
        conn.close()

        # Create a list of animal names
        self.animal_ids = [row[0] for row in rows]
        animal_names = [row[1] for row in rows]

        # Create a combobox for animal selection
        self.animal_var = tk.StringVar()
        self.animal_combobox = ttk.Combobox(master, textvariable=self.animal_var, values=animal_names)
        self.animal_combobox.pack()

        # Create a button to display the selected animal
        self.button = tk.Button(master, text="Display Animal", command=self.display_animal)
        self.button.pack()
        
        # Create a button to return to the home page
        # Create the "Back" button
        self.back_button = tk.Button(master, text="Back", command=self.go_back)
        self.back_button.pack()

   
    def display_animal(self):
        # Get the selected animal
        index = self.animal_combobox.current()
        animal_id = self.animal_ids[index]
        animal = Animal(animal_id)

        # Display the animal's attributes
        tk.Label(self.master, text="Name: " + animal.name).pack()
        tk.Label(self.master, text="Species: " + animal.species).pack()
        tk.Label(self.master, text="Habitat: " + animal.habitat).pack()
        
        # Load the image 
        img = Image.open(animal.image_path)
        # Resize the image
        img = img.resize((400, 500), Image.LANCZOS)
        # Convert the image to a Tkinter-compatible photo image  
        tk_img = ImageTk.PhotoImage(img)
        # Create a label with the image
        label = tk.Label(self.master, image=tk_img)
        label.image = tk_img
        label.pack()

    def go_back(self):
        # Destroy the current window
        self.master.destroy()

        from rza_website import ZooApp# Create a new instance of the main page
        main_page = ZooApp(tk.Tk())
        
class Animal:
    def __init__(self, animal_id):
        # Connect to the SQLite database
        conn = sqlite3.connect('zooAnimals.db')
        cursor = conn.cursor()

        # Execute a query to fetch the animal with the given ID
        cursor.execute("SELECT name, species, habitat , image_path FROM animals WHERE id = ?", (animal_id,))
        row = cursor.fetchone()

        # Close the database connection
        conn.close()

        # Set the animal's attributes
        if row is not None:
            self.name = row[0]
            self.species = row[1]
            self.habitat = row[2]
            self.image_path = row[3]
        else:
            self.name = ""
            self.species = ""
            self.habitat = ""
            self.image_path = ""



# Create the tkinter root widget
if __name__ == "__main__":
    root = tk.Tk()

    
     # Create an instance of ZooApp
    animal_page = AnimalPage(root,None)  # Pass the ZooApp instance to AnimalPage
    
    root.mainloop()