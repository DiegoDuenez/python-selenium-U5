import json
from os import pathsep

class Config:

    def __init__(self, path):
        self.path = path

    def load(self):
        f = open(self.path)
  
        # a dictionary
        data = json.load(f)
        
        # Iterating through the json
        # list
        #for i in data:
         #   print(i)
        
        # Closing file
        f.close()
        return data