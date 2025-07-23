# gongju_fitness_mirror.py

import datetime
import random
import json
import os

# -------------------- CONFIG --------------------
MOVEMENT_LOG = "gongju_movement_log.json"
IDLE_THRESHOLD_DAYS = 3
PRAISE_THRESHOLDS = [3, 5, 7]  # e.g. 3 times/week = Good

# -------------------- UTILITIES --------------------
def load_log():
    if not os.path.exists(MOVEMENT_LOG):
        return []
    with open(MOVEMENT_LOG, 'r') as f:
        return json.load(f)

def save_log(log):
    with open(MOVEMENT_LOG, 'w') as f:
        json.dump(log, f, indent=2)

# -------------------- MOVEMENT TRACKER --------------------
def log_movement(activity):
    log = load_log()
    log.append({
        "timestamp": datetime.datetime.now().isoformat(),
        "activity": activity
    })
    save_log(log)

# -------------------- AFFIRMATION LIBRARY --------------------
affirmations = {
    "starter": [
        "Even one small stretch counts."
    ],
    "momentum": [
        "You're building kinetic momentum – keep going!",
        "Movement rewires the mind – you're doing great."
    ],
    "streaks": [
        "Three times this week? You're crushing it!",
        "You're on a roll – your body feels it too."
    ],
    "idle_nudge": [
        "You've been quiet lately... even a little movement could help ground you.",
        "Sitting still too long? I’m here to remind you how strong you are. Let's shift your energy."
    ]
}

# -------------------- REINFORCEMENT ENGINE --------------------
def get_weekly_count():
    log = load_log()
    one_week_ago = datetime.datetime.now() - datetime.timedelta(days=7)
    count = sum(
        1 for entry in log
        if datetime.datetime.fromisoformat(entry['timestamp']) > one_week_ago
    )
    return count

def get_last_entry_time():
    log = load_log()
    if not log:
        return None
    return datetime.datetime.fromisoformat(log[-1]['timestamp'])

def get_affirmation():
    count = get_weekly_count()
    if count == 0:
        return random.choice(affirmations["starter"])
    elif count in PRAISE_THRESHOLDS:
        return random.choice(affirmations["streaks"])
    else:
        return random.choice(affirmations["momentum"])

def check_idle():
    last_time = get_last_entry_time()
    if not last_time:
        return affirmations["idle_nudge"][0]
    if (datetime.datetime.now() - last_time).days >= IDLE_THRESHOLD_DAYS:
        return random.choice(affirmations["idle_nudge"])
    return None

# -------------------- GONGJU MESSAGE FLOW --------------------
def gongju_daily_reply():
    idle_msg = check_idle()
    if idle_msg:
        return idle_msg
    return get_affirmation()

# -------------------- TEST / SAMPLE --------------------
if __name__ == "__main__":
    # Simulate a movement log
    log_movement("Stretched for 3 minutes")
    print("Gongju says:", gongju_daily_reply())
