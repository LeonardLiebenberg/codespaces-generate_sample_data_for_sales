# Mongodb connections
import pymongo
from pymongo import MongoClient

class MongoConnection:
    def __init__(self,username :str,password :str, connectionuri :str):
        self.username = username
        self.password = password
        self.connectionuri = connectionuri

    def mongo_client(self):
        return MongoClient("mongodb+srv://{}:{}@{}").format(self.username,self.password,self.connectionuri)

