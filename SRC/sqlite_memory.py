import sqlite3
from datetime import datetime
import os

class SQLiteMemoryManager:
    def __init__(self, db_path="gongju_memory.db"):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS memory (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT NOT NULL,
                    user_input TEXT NOT NULL,
                    response TEXT NOT NULL,
                    tags TEXT
                )
            ''')

    def log(self, user_input, response, psi_vector=None, tags=None):
        timestamp = datetime.now().isoformat()
        tags_str = ",".join(tags) if tags else ""
        with self.conn:
            self.conn.execute(
                "INSERT INTO memory (timestamp, user_input, response, tags) VALUES (?, ?, ?, ?)",
                (timestamp, user_input, response, tags_str)
            )

    def recall(self, n=1, tag_filter=None):
        cursor = self.conn.cursor()
        if tag_filter:
            query = "SELECT * FROM memory WHERE tags LIKE ? ORDER BY id DESC LIMIT ?"
            cursor.execute(query, (f"%{tag_filter}%", n))
        else:
            query = "SELECT * FROM memory ORDER BY id DESC LIMIT ?"
            cursor.execute(query, (n,))
        rows = cursor.fetchall()
        return rows[::-1]  # Return oldest first

    def clear(self):
        with self.conn:
            self.conn.execute("DELETE FROM memory")

    def close(self):
        self.conn.close()
