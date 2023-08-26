import os
import psycopg2

connection = psycopg2.connect(os.environ['DB_URI'])
cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS subs_mmdu, subs_form, subs_newsletter')

cursor.execute('CREATE TABLE subs_mmdu('
               'roll_number VARCHAR(8),'
               'full_name TEXT NOT NULL,'
               'email TEXT NOT NULL,'
               'father_name TEXT,'
               'mother_name TEXT,'
               'mobile_number CHAR(10),'
               'aadhar_number CHAR(12),'
               'gender CHAR(1),'
               'blood_group VARCHAR(3),'
               'dob CHAR(8),'
               'batch CHAR(4) NOT NULL,'
               'PRIMARY KEY (roll_number)'
               ')')

connection.commit()
cursor.close()
connection.close()