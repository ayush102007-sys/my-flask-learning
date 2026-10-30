from pymongo import MongoClient
import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Creating Database using MongoDB
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["quiz-db"]
collection = db["quiz-collection"]


def add_user(name):  # sign-up process
    collection.insert_one({
        "_id": f"user_{name}",
        "name": name
    })

def user_check(user_name):  # logged-in user check
    rec = collection.find({"_id" : f"user_{user_name}"}, {"name": 1, "_id": 0})  # Returns Cursor instance, not any list/dict
    username = ""
    for x in rec:
        username = x["name"]
    return username

def add_score(my_name, my_score, my_percentage):
    collection.update_one({
        "name": my_name},
        {
            "$set":
            {
                "score": my_score,
                "percentage": f"{my_percentage}%"
            }
        })

if __name__ == "__main__":
    print("Database connection testing")