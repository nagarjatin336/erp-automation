import os
import psycopg2
from dotenv import load_dotenv

def connect():
    load_dotenv()
    connection = psycopg2.connect(os.environ['DB_URI'])
    return connection

def insert(values):
    try:
        query = 'INSERT INTO subs_mmdu (roll_number,full_name,email,father_name,mother_name,mobile_number,aadhar_number,gender,blood_group,batch) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        conn = connect()
        cursor = conn.cursor()

        cursor.execute(query,values)
        conn.commit()

        cursor.close()
        conn.close()
        return True
    except Exception as error:
        print(error)
        return False