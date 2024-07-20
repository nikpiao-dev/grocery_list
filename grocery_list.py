import sqlite3

# Connect to the database
con = sqlite3.connect('groceries.db')
cur = con.cursor()

groceries = [
    'Pasta',
    'Rice',
    'Bread',
    'All-purpose flour',
    'Breakfast cereal',
    'Butter',
    'Cooking oil',
    'Milk',
    'Eggs',
    'Cheese',
    'Yogurt',
    'Onions',
    'Chicken',
    'Pork Chop',
    'NY Strip',
    'Garlic',
    'Chopped Tomato',
    'Banana',
    'Apples',
    'Salt',
    'Pepper',
    'Stock Cubes',
    'Honey',
    'Vinegar',
    'Sugar',
    'Basil',
    'Oregano',
    'Unsweetened granola',
    'Red kidney beans'
]

# Sort the list 
groceries.sort()


cur.execute('''
CREATE TABLE IF NOT EXISTS grocery (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL DEFAULT 'item'
)
''')

# Insert items into the table

# cur.executemany('INSERT INTO grocery (name) VALUES (?)', [(item), for item in groceries])

# Commit the changes
# con.commit()

# Fetch and print items from table
cur.execute('SELECT * FROM grocery')
grocery_items = cur.fetchall()
for item in grocery_items:
    print(item)

#close the connection (!Important)
con.close()