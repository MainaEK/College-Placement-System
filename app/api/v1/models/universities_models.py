from datetime import datetime

from .base_models import BaseModels


class UniversityModel(BaseModels):
    def __init__(self):
        super().__init__('universities')
        
        
    def get_all(self):
        self.db = BaseModels(db = 'universities')
        response = self.db.return_data()
        return response



    def register_university(self, university):
        university = {
            'university_id' : university['university_id'],
            'university_name' : university['university_name'],
        }
        response = self.save(university)
        return response
    