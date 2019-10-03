"""
This module is for making the database connection
"""
import os
import psycopg2
from dotenv import load_dotenv
from .db_tables import set_up_tables, drop_table_if_exists, create_admin

load_dotenv()
db_url = os.environ.get('DATABASE_URL')




class DatabaseConnection():
    """ Handles the main connection to the database of the app setting """ 
    def __init__(self):
        """ initialize the class instance to take a database url as a parameter"""   
        try:
            global conn, cur       
            conn = psycopg2.connect(db_url)
            cur = conn.cursor()
        except Exception as error:
            print(error)  
    
    def connection(self):
        """ Returns connection for the models """
        return conn
        
    def create_tables_and_admin(self):
        """ creates all tables and puts the admin """
        all_tables_to_create = set_up_tables()
        # print('Success')
        for query in all_tables_to_create:
            cur.execute(query)
            conn.commit()
        print('Tables created')
        create_admin(conn)  
        print('Admin created')
    
    def drop_all_tables(self):
        """ Deletes all tables in the app """
        tables_to_drop = drop_table_if_exists()
        for query in tables_to_drop:
            cur.execute(query)
            conn.commit() 
        print('Tables dropped')
    
    def fetch_single_data_row(self, query):
        """ retreives a single row of data from a table """
        cur.execute(query)
        fetchedRow = cur.fetchone()
        return fetchedRow  

    def save_incoming_data_or_updates(self, query):
        """ saves data passed as a query to the stated table """
        cur.execute(query)
        conn.commit()  
        
    def fetch_all_tables_rows(self, query):
        """ fetches all rows of data store """
        cur.execute(query)
        all_data_rows = cur.fetchall()
        return all_data_rows



# def db_con():
#     """Making the connection to the database"""
#     try:
#         con = psycopg2.connect(DATABASE_URL)

#     except Exception:
#         print("Unable to make database connection")

#     return con
