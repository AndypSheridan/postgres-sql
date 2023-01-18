import psycopg2


# connect to chinook db
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database
cursor = connection.cursor()