import psycopg2

# Connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# Build a cursor object og the database
cursor = connection.cursor()

# Fetch the results (multiple)
results = cursor.fetchall()

# Fetch the result (single)
# results = cursor.fetchone()
