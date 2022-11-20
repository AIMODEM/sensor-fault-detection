import pymongo
from sensor.constant.database import DATABASE_NAME
#from sensor.constant.env_variable import MONGODB_URL_KEY
import certifi
import os
ca = certifi.where()
import urllib

class MongoDBClient:
    client = None
    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = "mongodb+srv://ironfist:" + urllib.parse.quote_plus("Ironfist@945") + "@cluster0.tz5o3rr.mongodb.net/?retryWrites=true&w=majority"
                #os.getenv(MONGODB_URL_KEY)
               # mongo_db_url  = "mongodb+srv://ironfist:Ironfist@945@cluster0.tz5o3rr.mongodb.net/?retryWrites=true&w=majority"
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
        except Exception as e:
            raise e