import os
from datetime import datetime
from supabase import create_client, Client
from cryptography.fernet import Fernet
import hashlib
import base64

# Setup
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def derive_fernet_key(password: str) -> bytes:
    hashed = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(hashed)

class SupabaseMemoryManager:
    def __init__(self, user_id="default", password=""):
        self.user_id = user_id
        self.password = password or "default"
        self.fernet = Fernet(derive_fernet_key(self.password))

    def store_entry(self, text):
        timestamp = datetime.utcnow().isoformat()
        encrypted_text = self.fernet.encrypt(text.encode()).decode()

        print(f"📝 Supabase | Storing entry for {self.user_id}: {text}")

        supabase.table("gongju_memories").insert({
            "user_id": self.user_id,
            "text": encrypted_text,
            "timestamp": timestamp
        }).execute()

    def retrieve_recent_entries(self, num_entries=5):
        response = supabase.table("gongju_memories") \
            .select("text") \
            .eq("user_id", self.user_id) \
            .order("timestamp", desc=True) \
            .limit(num_entries) \
            .execute()

        entries = []
        for record in response.data:
            try:
                decrypted = self.fernet.decrypt(record["text"].encode()).decode()
                entries.append(decrypted)
            except Exception as e:
                print(f"[❌ Decryption error for {self.user_id}]: {e}")
        return entries

    def retrieve_first_entry(self):
        response = supabase.table("gongju_memories") \
            .select("text") \
            .eq("user_id", self.user_id) \
            .order("timestamp") \
            .limit(1) \
            .execute()

        if response.data:
            try:
                return self.fernet.decrypt(response.data[0]["text"].encode()).decode()
            except Exception as e:
                print(f"[❌ Decryption error for {self.user_id}]: {e}")
        return None
