# from flask import Flask, jsonify

students_list = []
users_list = []
courses_list = []
uni_list = []


class BaseModels(object):
    def __init__(self, db):
        self.db = db


    def check_db(self):
        if self.db == 'students':
            return students_list
        elif self.db == 'users':
            return users_list
        elif self.db == 'courses':
            return courses_list
        elif self.db == 'universities':
            return uni_list


    def check_exists(self, key, value):
        db = self.check_db()
        items = [item for item in db if item[key] == value]
        return len(items) 

    def find(self, key, value):
        db = self.check_db()
        items = [item for item in db if item[key] == value]
        return items[0]

    def return_data(self):
        db = self.check_db()
        return db

    def save(self,data):
        db = self.check_db()
        db.append(data)
        return data 
    
    def delete(self, key, value):
        """ Function to delete item """
        item = self.find(key, value)
        db = self.check_db()
        db.remove(item)
        