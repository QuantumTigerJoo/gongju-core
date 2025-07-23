import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

# Initialize Firebase app if not already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate("firebase_credentials.json")
    firebase_admin.initialize_app(cred)

# Get Firestore client
db = firestore.client()

class FirebaseMemoryManager:
    def __init__(self, user_id="default"):
        self.user_id = user_id
        self.collection = db.collection("gongju_memories")

    def store_entry(self, text):
        timestamp = datetime.utcnow()
        self.collection.add({
            "user_id": self.user_id,
            "text": text,
            "timestamp": timestamp
        })

    def retrieve_recent_entries(self, num_entries=5):
        query = self.collection.where("user_id", "==", self.user_id).order_by("timestamp", direction=firestore.Query.DESCENDING).limit(num_entries)
        results = query.stream()
        return [doc.to_dict()["text"] for doc in results]

    def retrieve_first_entry(self):
        query = self.collection.where("user_id", "==", self.user_id).order_by("timestamp", direction=firestore.Query.ASCENDING).limit(1)
        results = list(query.stream())
        if results:
            return results[0].to_dict()["text"]
        return None
