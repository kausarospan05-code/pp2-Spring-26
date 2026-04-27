import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="postgres",      # Your DB Name
        user="postgres",        # Your Username
        password=12345678, # YOUR REAL PASSWORD
        host="localhost",
        port="5432"
    )