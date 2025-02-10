from pymongo.mongo_client import MongoClient

class Client:
    def __init__(self, url: str, db_name: str):
        self.client = MongoClient(url)
        self.db = self.client.get_database(db_name)

    def push_data(self, ip: str, timestamp: str, data: dict):
        db_data = self.db.chats.find_one({"ip": ip})
        if db_data:
            db_data["data"][timestamp] = data
            self.db.chats.update_one({"ip": ip}, {"$set": db_data})
        else:
            self.db.chats.insert_one({"ip": ip, "data": {timestamp: data}})
