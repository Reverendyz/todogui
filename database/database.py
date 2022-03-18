import os
from dotenv import load_dotenv
import MySQLdb as s

def createconnection():
    load_dotenv()
    try:
        conn = s.connect(
            host=os.getenv('HOST'),
            user=os.getenv('USERW'),
            passwd=os.getenv('PASSWORD'),
            db=os.getenv('DATABASE')
        )
        print("Database Connected")
        print("Creating cursor")
        cursor = conn.cursor()
        print("Cursor created")
        sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        val = ("John", "Highway 21")
        cursor.execute(sql, val)
        print("Cursor executed")
        print("Commiting...")
        conn.commit()
        print("Commited")

    except:
        print("Connection was not successful")

    return conn