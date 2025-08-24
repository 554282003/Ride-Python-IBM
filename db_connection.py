from pymongo import MongoClient

def connect_to_db():
    # Replace with your MongoDB URI
    MONGO_URI = "mongodb://localhost:27017/"

    client = MongoClient(MONGO_URI)
    db = client['IBM-RIDE']
    return db

def insert_data(db,user_obj):
    user_collection = db['users']
    result = user_collection.insert_one(user_obj)
    return result.inserted_id

def find_user_by_email(db, email):
    user_collection = db["users"]
    return user_collection.find_one({"email": email})
