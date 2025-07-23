# fitness_logger.py
import json
from datetime import datetime
import os

LOG_FILE = "gongju_fitness_log.json"

def log_fitness_pulse(trigger_text, reflex_flags):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "trigger": trigger_text,
        "reflex_flags": reflex_flags
    }

    # Append to log
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            log = json.load(f)
    else:
        log = []

    log.append(entry)

    with open(LOG_FILE, "w") as f:
        json.dump(log, f, indent=2)

    print("🌀 Gongju registered a fitness pulse 🌀")
