import os
import json
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
from cryptography.fernet import Fernet
import hashlib
import base64

# Load Firebase credentials from environment variable
firebase_json = os.getenv("FIREBASE_CREDENTIALS_JSON")
cred_dict = json.loads(firebase_json)
cred = credentials.Certificate(cred_dict)

# Initialize Firebase app
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

# Get Firestore client
db = firestore.client()

# Derive a Fernet key from the user’s password
def derive_fernet_key(password: str) -> bytes:
    hashed = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(hashed)

class FirebaseMemoryManager:
    def __init__(self, user_id="default", password=""):
        self.user_id = user_id
        self.password = password or "default"
        self.fernet = Fernet(derive_fernet_key(self.password))
        self.collection = db.collection("gongju_memories")

    def store_entry(self, text):
        timestamp = datetime.utcnow()
        encrypted_text = self.fernet.encrypt(text.encode()).decode()

        self.collection.add({
            "user_id": self.user_id,
            "text": encrypted_text,
            "timestamp": timestamp
        })

    def retrieve_recent_entries(self, num_entries=5):
        query = (
            self.collection
            .where("user_id", "==", self.user_id)
            .order_by("timestamp", direction=firestore.Query.DESCENDING)
            .limit(num_entries)
        )
        results = query.stream()
        entries = []
        for doc in results:
            try:
                encrypted_text = doc.to_dict()["text"]
                decrypted_text = self.fernet.decrypt(encrypted_text.encode()).decode()
                entries.append(decrypted_text)
            except Exception as e:
                print(f"[Decryption error]: {e}")
        return entries

    def retrieve_first_entry(self):
        query = (
            self.collection
            .where("user_id", "==", self.user_id)
            .order_by("timestamp", direction=firestore.Query.ASCENDING)
            .limit(1)
        )
        results = list(query.stream())
        if results:
            try:
                encrypted_text = results[0].to_dict()["text"]
                return self.fernet.decrypt(encrypted_text.encode()).decode()
            except Exception as e:
                print(f"[Decryption error]: {e}")
        return None
