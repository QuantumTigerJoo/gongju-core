# gongju_user_memory.py

import json
import os

class UserMemoryControl:
    def __init__(self, filename="gongju_memory.json"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                json.dump([], f)

    def list_entries(self, limit=10):
        memory = self.load_memory()
        return memory[-limit:] if memory else []

    def forget_entry_by_id(self, entry_id):
        memory = self.load_memory()
        new_memory = [entry for entry in memory if entry.get("id") != entry_id]
        self._save_memory(new_memory)

    def forget_by_tag(self, tag):
        memory = self.load_memory()
        new_memory = [entry for entry in memory if tag not in entry.get("tags", [])]
        self._save_memory(new_memory)

    def clear_all_memory(self, confirm=False):
        if confirm:
            with open(self.filename, "w") as f:
                json.dump([], f)

    def export_memory(self, export_path="gongju_memory_export.json"):
        memory = self.load_memory()
        with open(export_path, "w") as f:
            json.dump(memory, f, indent=2)

    def _save_memory(self, memory):
        with open(self.filename, "w") as f:
            json.dump(memory, f, indent=2)

    def load_memory(self):
        with open(self.filename, "r") as f:
            return json.load(f)
