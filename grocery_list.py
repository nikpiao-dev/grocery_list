import sqlite3

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

cur.execute('')
