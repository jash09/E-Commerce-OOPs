from uuid import uuid1
import json

class User():
    def __init__(self, userName, name, age, gender):
        self.id = str(uuid1())
        self.userName = userName
        self.name = name
        self.age = age
        self.gender = gender
    
    def display(self):
        print(json.dumps(self, indent=5, default=lambda o: o.__dict__))