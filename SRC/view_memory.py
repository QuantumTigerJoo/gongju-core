import sqlite3

conn = sqlite3.connect("gongju_memory.db")
cursor = conn.cursor()

cursor.execute("""
    SELECT timestamp, user_input, response 
    FROM memory 
    ORDER BY timestamp DESC 
    LIMIT 3
""")
rows = cursor.fetchall()

for row in rows:
    print(f"[{row[0]}]\n→ {row[1]}\n← {row[2]}\n")

conn.close()
