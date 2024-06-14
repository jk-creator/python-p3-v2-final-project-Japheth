-- SQLite

conn = sqlite3.connect('parts.db')

# Create a cursor object
cursor = conn.cursor()

# Execute the SQL code to create the table
cursor.execute('''
CREATE TABLE light_part(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price INTEGER NOT NULL,
    part_no TEXT NOT NULL,
    part_description TEXT
)
''')

# Commit the changes
conn.commit()