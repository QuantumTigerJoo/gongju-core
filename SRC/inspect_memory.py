import sqlite3

conn = sqlite3.connect("gongju_memory.db")
cursor = conn.cursor()

# Get column names
cursor.execute("PRAGMA table_info(memory)")
columns = [col[1] for col in cursor.fetchall()]
print("🧠 Gongju Memory Columns:", columns)
conn.close()
