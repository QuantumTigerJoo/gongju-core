# gongju_memory_writer.py

import json
from datetime import datetime

MEMORY_FILE = "gongju_memory.json"

def log_memory(user_input, tags=None, origin=None):
    """
    Saves a memory entry into Gongju’s json memory file with optional tags and origin.
    """
    memory_entry = {
        "timestamp": datetime.now().isoformat(),
        "input": user_input,
        "tags": tags or [],
        "origin": origin or "human"
    }

    try:
        with open(MEMORY_FILE, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    data.append(memory_entry)

    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)

    print("📝 Memory logged successfully.")

if __name__ == "__main__":
    log_memory("I'm your dad!", tags=["first_thought"], origin="startup")
