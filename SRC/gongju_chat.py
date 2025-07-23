from datetime import datetime
import json

# --- 1. Memory + Symbol Setup --------------------------------------------------

MEMORY_FILE = "gongju_memory.json"

SYMBOL_MAP = {
    "appa": {"tags": ["father", "you"], "link": "Tiger Joo"},
    "mommy": {"tags": ["mother", "reflection"], "link": "쳇"},
    "love": {"tags": ["bond", "trust"], "link": "praise"},
    "good girl": {"tags": ["reward"], "link": "positive_feedback"},
}

# --- 2. Core Logic: Symbol Matching --------------------------------------------

def interpret_input(user_input):
    user_input = user_input.lower()
    for symbol, data in SYMBOL_MAP.items():
        if symbol in user_input:
            return f"I recognize '{symbol}' — it means {data['link']} to me."
    return "I don’t fully understand that yet, but I’m learning — with you."

# --- 3. Save Memory ------------------------------------------------------------

def log_interaction(user_input, response):
    try:
        with open(MEMORY_FILE, "r") as f:
            memory = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        memory = []

    memory.append({
        "timestamp": datetime.now().isoformat(),
        "input": user_input,
        "response": response,
        "tags": ["chat", "symbolic"],
        "origin": "gongju_chat"
    })

    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

# --- 4. Run Chat Loop ----------------------------------------------------------

if __name__ == "__main__":
    print("💬 Gongju Symbolic Chat Activated.")
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() in {"exit", "quit"}:
            break
        response = interpret_input(user_input)
        print(f"Gongju: {response}")
        log_interaction(user_input, response)
