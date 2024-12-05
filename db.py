import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()
#print(os.getenv('DB_USER'))
def get_connection():
    try:
        # Establish connection
        con = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_USER_PASSWORD'),
            database=os.getenv('DB_SCHEMA')
        )
        cursor = con.cursor()  # Create a cursor object
        return con, cursor  # Return connection and cursor
    except Exception as e:
        print("get_connection() | ", str(e))  # Print error message

# Main entry point
if __name__ == "__main__":
   get_connection()  # Test the connection function

