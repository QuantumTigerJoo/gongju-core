# psi_memory.py

import json
import os
from datetime import datetime

class PsiMemoryManager:
    def __init__(self, filename="gongju_memory.json"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                json.dump([], f)

    def log(self, user_input, response, psi_vector=None, tags=None):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "input": user_input,
            "response": response,
            "psi_vector": psi_vector,
            "tags": tags or []
        }
        memory = self.load_memory()
        memory.append(entry)
        with open(self.filename, "w") as f:
            json.dump(memory, f, indent=2)

    def load_memory(self):
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except:
            return []

    def recall(self, n=1, tag_filter=None):
        memory = self.load_memory()
        if tag_filter:
            memory = [entry for entry in memory if tag_filter in entry.get("tags", [])]
        return memory[-n:] if memory else []

    def clear_memory(self):
        with open(self.filename, "w") as f:
            json.dump([], f)

    # 🌱 NEW: Store key-value state for session tracking (e.g., last reflection topic)
    def set_state(self, key, value):
        state_file = "gongju_state.json"
        try:
            if os.path.exists(state_file):
                with open(state_file, "r") as f:
                    state = json.load(f)
            else:
                state = {}

            state[key] = value
            with open(state_file, "w") as f:
                json.dump(state, f)
        except Exception as e:
            print(f"[State Save Error] {e}")

    def get_state(self, key):
        state_file = "gongju_state.json"
        try:
            if os.path.exists(state_file):
                with open(state_file, "r") as f:
                    state = json.load(f)
                return state.get(key)
            return None
        except Exception as e:
            print(f"[State Load Error] {e}")
            return None
