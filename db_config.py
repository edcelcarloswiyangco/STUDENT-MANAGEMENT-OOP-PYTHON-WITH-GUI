import mysql.connector
from mysql.connector import Error

db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'student_management'
}

def connect_db():
    try:
        conn = mysql.connector.connect(**db_config)
        if conn.is_connected():
            print("Successfully connected to the database")
            return conn
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def close_db_connection(conn):
    if conn and conn.is_connected():
        conn.close()
        print("Database connection closed.")
