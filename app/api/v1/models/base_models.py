from flask import Flask
from psycopg2.extras import DictCursor
from .database import DatabaseConnection

class BaseModels(DatabaseConnection):
    def __init__(self, tablename):
        self.table = tablename
        DatabaseConnection()
        self.connect = DatabaseConnection().connection()
        self.cur = self.connect.cursor(cursor_factory=DictCursor)

    def check_exists(self, key, value):
            """Checks where a particular item exists within the
            database given the table name, column name(key) and 
            the value to be checked"""
            query = """SELECT * FROM {} WHERE {} = {};""".format(
                self.table, key, value)
            result = DatabaseConnection().fetch_all_tables_rows(query)
            return len(result) > 0
    
    def return_data(self):
        """Returns all data from a table"""
        query = """SELECT * FROM {};""".format(self.table)
        result = DatabaseConnection().fetch_all_tables_rows(query)
        return result
    
    def find(self, key, value):
        query = """SELECT * FROM {} WHERE {} = {};""".format(
                self.table, key, value)
        result = DatabaseConnection().fetch_single_data_row(query)
        return result
    
    def delete(self, key, value):
        query = """DELETE FROM {} WHERE {} = {};""".format(
                self.table, key, value)
        DatabaseConnection().save_incoming_data_or_updates(query)

    # def check_db(self):
    #     if self.db == 'students':
    #         return students_list
    #     elif self.db == 'users':
    #         return users_list
    #     elif self.db == 'courses':
    #         return courses_list
    #     elif self.db == 'universities':
    #         return uni_list


    # def check_exists(self, key, value):
    #     db = self.check_db()
    #     items = [item for item in db if item[key] == value]
    #     return len(items) 

    # def find(self, key, value):
    #     db = self.check_db()
    #     items = [item for item in db if item[key] == value]
    #     return items[0]

    # def return_data(self):
    #     db = self.check_db()
    #     return db

    # def save(self,data):
    #     db = self.check_db()
    #     db.append(data)
    #     return data 
    
    # def delete(self, key, value):
    #     """ Function to delete item """
    #     item = self.find(key, value)
    #     db = self.check_db()
    #     db.remove(item)
        