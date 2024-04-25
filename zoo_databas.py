import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('zooAnimals.db')
cursor = conn.cursor()

# Create the animals table
cursor.execute("""
    CREATE TABLE animals (
        id INTEGER PRIMARY KEY,
        name TEXT,
        species TEXT,
        habitat TEXT,
        image_path TEXT       
    )
""")

# Insert some animals into the table
animals = [
    (1, 'Lion', 'Panthera leo', 'Grasslands, scrub, and open woodlands', 'images/lions.jpg'),
    (2, 'Tiger', 'Panthera tigris', 'Grasslands, mixed grassland-forests, and deciduous forests', 'images/tiger.jpg'),
    (3, 'Elephant', 'Elephas maximus', 'Forests, grasslands, and wetlands', 'images/elephant.jpg'),
]
# for animal in animals:
#     cursor.execute(
#         "INSERT INTO animals (name, species, habitat, image_path) VALUES (?, ?, ?, ?)", animal)


cursor.executemany("""
    INSERT INTO animals (id, name, species, habitat, image_path) VALUES (?, ?, ?, ?,?)
""", animals)

# Commit the changes and close the connection
conn.commit()
conn.close()