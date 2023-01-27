from pymongo import MongoClient

client = MongoClient("mongodb+srv://xavivi2000:Preguntados2.@t-rivial-api.hwjttpy.mongodb.net/?retryWrites=true&w=majority")
conn = client['prod-db']
