import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('attraction.db')

# Create a cursor object
c = conn.cursor()

# Create the attractions table
c.execute('''
    CREATE TABLE attractions (
        id INTEGER PRIMARY KEY,
        name TEXT,
        species TEXT
    )
''')

# Insert some attractions
c.execute("INSERT INTO attractions (name, species) VALUES (?, ?)", ("Lion's Den", "Lion"))
c.execute("INSERT INTO attractions (name, species) VALUES (?, ?)", ("Elephant Ride", "Elephant"))

# Create the facilities table
c.execute('''
    CREATE TABLE facilities (
        id INTEGER PRIMARY KEY,
        name TEXT,
        description TEXT
    )
''')

# Insert some facilities
c.execute("INSERT INTO facilities (name, description) VALUES (?, ?)", ("Cafeteria", "Food and drinks"))
c.execute("INSERT INTO facilities (name, description) VALUES (?, ?)", ("Gift Shop", "Souvenirs and gifts"))

# Commit the changes and close the connection
conn.commit()
conn.close()