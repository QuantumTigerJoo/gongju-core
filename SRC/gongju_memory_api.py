from flask import Flask, request, jsonify
from datetime import datetime
import sqlite3
import os
import pickle

# 🔐 Google OAuth libraries
from google_auth_oauthlib.flow import InstalledAppFlow

app = Flask(__name__)

# ====== Memory Logging Config ======
DB_PATH = "gongju_memory.db"

def log_memory(user_input, response, tags=None):
    timestamp = datetime.now().isoformat()
    tags_str = ",".join(tags) if tags else ""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS memory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            user_input TEXT NOT NULL,
            response TEXT NOT NULL,
            tags TEXT
        )
    """)
    cursor.execute(
        "INSERT INTO memory (timestamp, user_input, response, tags) VALUES (?, ?, ?, ?)",
        (timestamp, user_input, response, tags_str)
    )
    conn.commit()
    conn.close()

@app.route('/log', methods=['POST'])
def receive_log():
    data = request.json
    user_input = data.get('user_input')
    response = data.get('response')
    tags = data.get('tags', [])
    
    if not user_input or not response:
        return jsonify({'error': 'Missing input or response'}), 400

    log_memory(user_input, response, tags)
    return jsonify({'status': 'success'}), 200

# ====== OAuth Login Flow ======
SCOPES = ['https://www.googleapis.com/auth/documents']
CREDENTIALS_FILE = 'credentials.json'
TOKEN_FILE = 'token.pickle'

@app.route('/login')
def login():
    flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
    creds = flow.run_local_server(port=0)
    with open(TOKEN_FILE, 'wb') as token:
        pickle.dump(creds, token)
    return '✅ Login successful! Token stored as token.pickle'

# ====== Run Flask App ======
if __name__ == '__main__':
    app.run(port=5050)
