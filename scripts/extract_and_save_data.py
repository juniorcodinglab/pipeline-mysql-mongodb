import requests

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://silvio:pK1o8i1WvtQ2Gm4K@alura.2c3hcde.mongodb.net/?retryWrites=true&w=majority&appName=Alura"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    

db = client["db_produtos"]
collection = db["produtos"]

product = {"produto": "Computador", "quantidade": 77}
collection.insert_one(product)

response = requests.get("https://labdados.com/produtos")
response.json()[0]

docs = collection.insert_many(response.json())

client.close()