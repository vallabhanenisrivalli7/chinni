from flask import Flask , request , jsonify
import psycopg2
from psycopg2 import sql

app = Flask(_name_)

#database configuration
DB_HOST='localhost'
DB_NAME='postgres'
DB_USER='postgres'
DB_PASSWORD='1227'

def get_db_connection():
    connection=psycopg2.connect(
     host=DB_HOST,
     database=DB_NAME,
     user=DB_USER,
     password=DB_PASSWORD
     )
    return connection
def create_tb_if_not_exist():
    connection = get_db_connection()
    cursor = connection.cursor()
  
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS user_db(
                   user_db SERIAL PRIMARY KEY,
                   username TEXT NOT NULL,
                   password TEXT NOT NULL,
                   email TEXT NOT NULL
                   );   
                   """)
    connection.commit()
    cursor.close()
    connection.close()
create_tb_if_not_exist()



if __name__=='__main__':
   app.run(debug = True)