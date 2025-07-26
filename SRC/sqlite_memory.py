import sqlite3
from datetime import datetime
import bcrypt

class SQLiteMemoryManager:
    def __init__(self, db_path="gongju_memory.db"):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    user_id TEXT PRIMARY KEY,
                    password_hash TEXT NOT NULL
                )
            ''')
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS memory (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id TEXT NOT NULL,
                    timestamp TEXT NOT NULL,
                    user_input TEXT NOT NULL,
                    response TEXT NOT NULL,
                    tags TEXT,
                    FOREIGN KEY(user_id) REFERENCES users(user_id)
                )
            ''')

    def register_user(self, user_id, password):
        password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        with self.conn:
            self.conn.execute(
                "INSERT OR IGNORE INTO users (user_id, password_hash) VALUES (?, ?)",
                (user_id, password_hash)
            )

    def verify_user(self, user_id, password):
        cursor = self.conn.cursor()
        cursor.execute("SELECT password_hash FROM users WHERE user_id = ?", (user_id,))
        result = cursor.fetchone()
        if result:
            return bcrypt.checkpw(password.encode(), result[0].encode())
        return False

    def log(self, user_id, user_input, response, tags=None):
        timestamp = datetime.now().isoformat()
        tags_str = ",".join(tags) if tags else ""
        with self.conn:
            self.conn.execute(
                "INSERT INTO memory (user_id, timestamp, user_input, response, tags) VALUES (?, ?, ?, ?, ?)",
                (user_id, timestamp, user_input, response, tags_str)
            )

    def recall(self, user_id, n=5):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT user_input, response FROM memory WHERE user_id = ? ORDER BY id DESC LIMIT ?",
            (user_id, n)
        )
        return cursor.fetchall()[::-1]  # Oldest first
