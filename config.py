from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from dotenv import load_dotenv
import os
load_dotenv()

db_uri = os.getenv("DB_URI")
# Create a new client and connect to the server
client = MongoClient(db_uri, server_api=ServerApi('1'))

# Sending a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)



#create the database
db = client["mongofastapi"] 

#create the collection
student_collection = db["students"]