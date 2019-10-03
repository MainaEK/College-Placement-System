from flask import Flask
from .database import DatabaseConnection
from .base_models import BaseModels


class UniversityModel(BaseModels):
    def __init__(self):
        super().__init__('universities')
        

    def create_university(self, university):
        """Function that creates a university in the universities table"""
        
        query = """INSERT INTO universities (uni_id,uni_name,email)\
        VALUES ('{}','{}','{}');""".format(university['uni_id'], university['uni_name'], university['email'])
        DatabaseConnection().save_incoming_data_or_updates(query)



    # def register_university(self, university):
    #     university = {
    #         'university_id' : university['university_id'],
    #         'university_name' : university['university_name'],
    #     }
    #     response = self.save(university)
    #     return response
    